"""
*  ____           _                      
* |  _ \ ___   __| |_ __ _   _ _ __ ___  
* | |_) / _ \ / _` | '__| | | | '_ ` _ \ 
* |  __/ (_) | (_| | |  | |_| | | | | | |
* |_|   \___/ \__,_|_|   \__,_|_| |_| |_|
*
* This program is free software: you can redistribute it and/or modify
* it under the terms of the GNU Lesser General Public License as published by
* the Free Software Foundation, either version 3 of the License, or
* (at your option) any later version.
"""
from datetime import datetime
from .TextFormat import TextFormat


TextFormat = TextFormat()


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
        print(f'{TextFormat.GRAY}[DEBUG: {time.strftime("%H:%M")}]{TextFormat.WHITE} {content}')
    else:
        print(f'[{type_.upper()}: {time.strftime("%H:%M")}]{content}')
