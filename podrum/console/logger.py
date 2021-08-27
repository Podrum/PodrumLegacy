r"""
  ____           _
 |  _ \ ___   __| |_ __ _   _ _ __ ___
 | |_) / _ \ / _` | '__| | | | '_ ` _ \
 |  __/ (_) | (_| | |  | |_| | | | | | |
 |_|   \___/ \__,_|_|   \__,_|_| |_| |_|

 Copyright 2021 Podrum Team.

 This file is licensed under the GPL v2.0 license.
 The license file is located in the root directory
 of the source code. If not you may not use this file.
"""

import sys
from datetime import datetime
from typing import Callable, Dict

from podrum.console.text_format import text_format

LogMethod = Callable[[str], None]


class logger:

    __log_types: Dict[str, str] = {
        "info": text_format.blue,
        "warn": text_format.yellow,
        "error": text_format.red,
        "success": text_format.green,
        "emergency": text_format.gold,
        "notice": text_format.aqua,
        "critical": text_format.dark_red,
        "debug": text_format.gray
    }

    info: LogMethod
    warn: LogMethod
    error: LogMethod
    success: LogMethod
    emergency: LogMethod
    notice: LogMethod
    critical: LogMethod
    debug: LogMethod

    def __init__(self) -> None:
        if sys.platform in ["win32", "win64"]:
            from ctypes import windll

            kernel = windll.kernel32
            kernel.SetConsoleMode(kernel.GetStdHandle(-11), 7)

    def __getattr__(self, item: str) -> LogMethod:
        log_type = self.__log_types.get(item.lower())

        if not log_type:
            raise AttributeError

        return lambda content: self.__log(item, content)

    def __log(self, log_type: str, content: str) -> None:
        date_time: datetime = datetime.now()
        color: str = self.__log_types[log_type]

        print(
            text_format.minecraft_to_console_colors(
                f"{color}[{log_type.upper()}: "
                f"{date_time:%H:%M}]{text_format.white}"
                f" {content}{text_format.reset}"
            )
        )
