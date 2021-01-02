"""
*  ____           _
* |  _ \ ___   __| |_ __ _   _ _ __ ___
* | |_) / _ \ / _` | '__| | | | '_ ` _ \
* |  __/ (_) | (_| | |  | |_| | | | | | |
* |_|   \___/ \__,_|_|   \__,_|_| |_| |_|
*
* Licensed under the Mozilla Public License, Version 2.
* Permissions of this weak copyleft license are conditioned on making
* available source code of licensed files and modifications of those files 
* under the same license (or in certain cases, one of the GNU licenses).
* Copyright and license notices must be preserved. Contributors
* provide an express grant of patent rights. However, a larger work
* using the licensed work may be distributed under different terms and without 
* source code for files added in the larger work.
"""

from datetime import datetime
import inspect
from podrum.utils.TextFormat import TextFormat

class Logger:
    @staticmethod
    def log(logType, content):
        dateTime = datetime.now()
        if logType.lower() == "info":
            color = TextFormat.blue
        elif logType.lower() == "warn":
            color = TextFormat.yellow
        elif logType.lower() == "error":
            color = TextFormat.red
        elif logType.lower() == "success":
            color = TextFormat.green
        elif logType.lower() == "emergency":
            color = TextFormat.gold
        elif logType.lower() == "alert":
            color = TextFormat.purple
        elif logType.lower() == "notice":
            color = TextFormat.aqua
        elif logType.lower() == "critical":
            color = TextFormat.darkRed
        elif logType.lower() == "debug":
            color = TextFormat.gray
        else:
            return
        print(f"{color}[{logType.upper()}: {dateTime.strftime('%H:%M')}]{TextFormat.white} {content}")

    @staticmethod
    def info(content):
        Logger.log(inspect.stack()[0][3], content)

    @staticmethod
    def warn(content):
        Logger.log(inspect.stack()[0][3], content)

    @staticmethod
    def error(content):
        Logger.log(inspect.stack()[0][3], content)

    @staticmethod
    def success(content):
        Logger.log(inspect.stack()[0][3], content)

    @staticmethod
    def emergency(content):
        Logger.log(inspect.stack()[0][3], content)

    @staticmethod
    def alert(content):
        Logger.log(inspect.stack()[0][3], content)

    @staticmethod
    def notice(content):
        Logger.log(inspect.stack()[0][3], content)

    @staticmethod
    def critical(content):
        Logger.log(inspect.stack()[0][3], content)

    @staticmethod
    def debug(content):
        Logger.log(inspect.stack()[0][3], content)