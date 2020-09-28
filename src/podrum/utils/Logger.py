"""
*  ____           _
* |  _ \ ___   __| |_ __ _   _ _ __ ___
* | |_) / _ \ / _` | '__| | | | '_ ` _ \
* |  __/ (_) | (_| | |  | |_| | | | | | |
* |_|   \___/ \__,_|_|   \__,_|_| |_| |_|
*
* Licensed under the Apache License, Version 2.0 (the "License")
* you may not use this file except in compliance with the License.
* You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
"""

from datetime import datetime
from podrum.utils.TextFormat import TextFormat

TextFormat = TextFormat()

class Logger:

    @staticmethod
    def log(type_, content):
        time = datetime.now()
        if type_ == 'info':
            print(f'{TextFormat.BLUE}[INFO: {time.strftime("%H:%M")}]{TextFormat.WHITE} {content}')
        elif type_ == 'warn':
            print(f'{TextFormat.YELLOW}[WARNING: {time.strftime("%H:%M")}]{TextFormat.WHITE} {content}')
        elif type_ == 'error':
            print(f'{TextFormat.RED}[ERROR: {time.strftime("%H:%M")}]{TextFormat.WHITE} {content}')
        elif type_ == 'success':
            print(f'{TextFormat.GREEN}[SUCCESS: {time.strftime("%H:%M")}]{TextFormat.WHITE} {content}')
        elif type_ == "emergency":
            print(f'{TextFormat.GOLD}[EMERGENCY: {time.strftime("%H:%M")}]{TextFormat.WHITE} {content}')
        elif type_ == "alert":
            print(f'{TextFormat.PURPLE}[ALERT: {time.strftime("%H:%M")}]{TextFormat.WHITE} {content}')
        elif type_ == "notice":
            print(f'{TextFormat.AQUA}[NOTICE: {time.strftime("%H:%M")}]{TextFormat.WHITE} {content}')
        elif type_ == "critical":
            print(f'{TextFormat.RED}[CRITICAL: {time.strftime("%H:%M")}]{TextFormat.WHITE} {content}')
        elif type_ == "debug":
            print(f'{TTextFormat.GRAY}[DEBUG: {time.strftime("%H:%M")}]{TextFormat.WHITE} {content}')
        else:
            print(f'[{type_.upper()}: {time.strftime("%H:%M")}]{content}')
