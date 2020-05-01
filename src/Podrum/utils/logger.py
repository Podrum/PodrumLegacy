from .checkOS import getOS


class colors:
    def __init__(self):
        if getOS() == 'windows':
            self.WHITE  = '\33[37m'
            self.RED    = '\33[31m'
            self.GREEN  = '\33[32m'
            self.YELLOW = '\33[33m'
            self.BLUE   = '\33[34m'
            self.VIOLET = '\33[35m'
            self.BEIGE  = '\33[36m'
            self.BLACK  = '\33[30m'
        elif getOS() == 'osx' or getOS() == 'linux':
            # TODO: Add UNIX colors
            self.WHITE  = ''
            self.RED    = ''
            self.GREEN  = ''
            self.YELLOW = ''
            self.BLUE   = ''
            self.VIOLET = ''
            self.BEIGE  = ''
            self.BLACK  = ''
