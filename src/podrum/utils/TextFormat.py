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

import os
from re import M
from podrum.utils.Utils import Utils

class TextFormat:

    def __init__(self):
        if Utils.getOS() == 'windows':
            from ctypes import windll
            kernel = windll.kernel32
            kernel.SetConsoleMode(kernel.GetStdHandle(-11), 7)
        self.BOLD = '\x1b[1m'
        self.OBFUSCATED = ''
        self.ITALIC = '\x1b[3m'
        self.UNDERLINE = '\x1b[4m'
        self.STRIKETHROUGH = '\x1b[9m'
        self.RESET = '\x1b[m'
        self.BLACK = '\x1b[38;5;16m'
        self.DARKBLUE = '\x1b[38;5;19m'
        self.DARKGREEN = '\x1b[38;5;34m'
        self.DARKAQUA = '\x1b[38;5;37m'
        self.DARKRED = '\x1b[38;5;124m'
        self.PURPLE = '\x1b[38;5;127m'
        self.GOLD = '\x1b[38;5;214m'
        self.GRAY = '\x1b[38;5;145m'
        self.DARKGRAY = '\x1b[38;5;59m'
        self.BLUE = '\x1b[38;5;63m'
        self.GREEN = '\x1b[38;5;83m'
        self.AQUA = '\x1b[38;5;87m'
        self.RED = '\x1b[38;5;203m'
        self.LIGHTPURPLE = '\x1b[38;5;207m'
        self.YELLOW = '\x1b[38;5;227m'
        self.WHITE = '\x1b[38;5;231m'
