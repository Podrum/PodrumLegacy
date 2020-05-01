from re import M

from .checkOS import getOS
from datetime import datetime


class colors:
    def __init__(self):
        if getOS() == 'windows':
            self.WHITE = '\33[37m'
            self.RED = '\33[31m'
            self.GREEN = '\33[32m'
            self.YELLOW = '\33[33m'
            self.BLUE = '\33[34m'
            self.VIOLET = '\33[35m'
            self.BEIGE = '\33[36m'
            self.BLACK = '\33[30m'
        elif getOS() == 'osx' or getOS() == 'linux':
            # TODO: Add UNIX colors
            self.WHITE = ''
            self.RED = ''
            self.GREEN = ''
            self.YELLOW = ''
            self.BLUE = ''
            self.VIOLET = ''
            self.BEIGE = ''
            self.BLACK = ''


colors = colors()


def log(type_, content):
    time = datetime.now()
    if type_ == 'info':
        print(f'{colors.BLUE}[INFO: {time.strftime("%H:%M")}]{colors.WHITE} {content}')
    elif type_ == 'warn':
        print(f'{colors.YELLOW}[WARNING: {time.strftime("%H:%M")}]{colors.WHITE} {content}')
    elif type_ == 'error':
        print(f'{colors.RED}[ERROR: {time.strftime("%H:%M")}]{colors.WHITE} {content}')
    elif type_ == 'success':
        print(f'{colors.GREEN}[: {time.strftime("%H:%M")}]{colors.WHITE} {content}')