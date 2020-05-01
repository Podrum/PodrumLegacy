from re import M
from .checkOS import getOS

class TextFormat:
    def __init__(self):
        if getOS() == 'windows':
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
        elif getOS() == 'darwin' or getOS() == 'linux':
            self.BOLD = "\x1b[1m"
            self.OBFUSCATED = ""
	    self.ITALIC = "\x1b[3m"
	    self.UNDERLINE = "\x1b[4m"
	    self.STRIKETHROUGH = "\x1b[9m"
	    self.RESET = "\x1b[m"
	    self.BLACK = "\x1b[38;5;16m"
	    self.DARKBLUE = "\x1b[38;5;19m"
	    self.DARKGREEN = "\x1b[38;5;34m"
	    self.DARKAQUA = "\x1b[38;5;37m"
    	    self.DARKRED = "\x1b[38;5;124m"
    	    self.PURPLE = "\x1b[38;5;127m"
	    self.GOLD = "\x1b[38;5;214m"
	    self.GRAY = "\x1b[38;5;145m"
	    self.DARKGRAY = "\x1b[38;5;59m"
    	    self.BLUE = "\x1b[38;5;63m"
    	    self.GREEN = "\x1b[38;5;83m"
    	    self.AQUA = "\x1b[38;5;87m"
     	    self.RED = "\x1b[38;5;203m"
	    self.LIGHTPURPLE = "\x1b[38;5;207m"
	    self.YELLOW = "\x1b[38;5;227m"
	    self.WHITE = "\x1b[38;5;231m"
