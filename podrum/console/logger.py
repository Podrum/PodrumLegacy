#########################################################                        
#  ____           _                                     #
# |  _ \ ___   __| |_ __ _   _ _ __ ___                 #
# | |_) / _ \ / _` | '__| | | | '_ ` _ \                #
# |  __/ (_) | (_| | |  | |_| | | | | | |               #
# |_|   \___/ \__,_|_|   \__,_|_| |_| |_|               #
#                                                       #
# Copyright 2021 Podrum Team.                           #
#                                                       #
# This file is licensed under the GPL v2.0 license.     #
# The license file is located in the root directory     #
# of the source code. If not you may not use this file. #
#                                                       #
#########################################################

from console.text_format import text_format
from datetime import datetime
import inspect
import sys

class logger:
    def __init__(self):
        if sys.platform == "win32" or sys.platform == "win64":
            from ctypes import windll
            kernel: object = windll.kernel32
            kernel.SetConsoleMode(kernel.GetStdHandle(-11), 7)
        
    def log(self, log_type: str, content: str) -> None:
        date_time: object = datetime.now()
        if log_type.lower() == "info":
            color: str = text_format.blue
        elif log_type.lower() == "warn":
            color: str = text_format.yellow
        elif log_type.lower() == "error":
            color: str = text_format.red
        elif log_type.lower() == "success":
            color: str = text_format.green
        elif log_type.lower() == "emergency":
            color: str = text_format.gold
        elif log_type.lower() == "alert":
            color: str = text_format.light_purple
        elif log_type.lower() == "notice":
            color: str = text_format.aqua
        elif log_type.lower() == "critical":
            color: str = text_format.darkRed
        elif log_type.lower() == "debug":
            color: str = text_format.gray
        else:
            return
        print(text_format.minecraft_to_console_colors(f"{color}[{log_type.upper()}: {date_time.strftime('%H:%M')}]{text_format.white} {content}{text_format.reset}"))

    def info(self, content: str) -> None:
        self.log(inspect.stack()[0][3], content)

    def warn(self, content: str) -> None:
        self.log(inspect.stack()[0][3], content)

    def error(self, content: str) -> None:
        self.log(inspect.stack()[0][3], content)

    def success(self, content: str) -> None:
        self.log(inspect.stack()[0][3], content)

    def emergency(self, content: str) -> None:
        self.log(inspect.stack()[0][3], content)

    def alert(self, content: str) -> None:
        self.log(inspect.stack()[0][3], content)

    def notice(self, content: str) -> None:
        self.log(inspect.stack()[0][3], content)
              
    def critical(self, content: str) -> None:
        self.log(inspect.stack()[0][3], content)

    def debug(self, content: str) -> None:
        self.log(inspect.stack()[0][3], content)
