################################################################################
#                                                                              #
#  ____           _                                                            #
# |  _ \ ___   __| |_ __ _   _ _ __ ___                                        #
# | |_) / _ \ / _` | '__| | | | '_ ` _ \                                       #
# |  __/ (_) | (_| | |  | |_| | | | | | |                                      #
# |_|   \___/ \__,_|_|   \__,_|_| |_| |_|                                      #
#                                                                              #
# Copyright 2021 Podrum Studios                                                #
#                                                                              #
# Permission is hereby granted, free of charge, to any person                  #
# obtaining a copy of this software and associated documentation               #
# files (the "Software"), to deal in the Software without restriction,         #
# including without limitation the rights to use, copy, modify, merge,         #
# publish, distribute, sublicense, and/or sell copies of the Software,         #
# and to permit persons to whom the Software is furnished to do so,            #
# subject to the following conditions:                                         #
#                                                                              #
# The above copyright notice and this permission notice shall be included      #
# in all copies or substantial portions of the Software.                       #
#                                                                              #
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR   #
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,     #
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE  #
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER       #
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING      #
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS #
# IN THE SOFTWARE.                                                             #
#                                                                              #
################################################################################

class text_format:
    bold: str = "\x1b[1m"
    obfuscated: str = ""
    italic: str = "\x1b[3m"
    underline: str = "\x1b[4m"
    strike_through: str = "\x1b[9m"
    reset: str = "\x1b[m"
    black: str = "\x1b[38;5;16m"
    dark_blue: str = "\x1b[38;5;19m"
    dark_green: str = "\x1b[38;5;34m"
    dark_aqua: str = "\x1b[38;5;37m"
    dark_red: str = "\x1b[38;5;124m"
    purple: str = "\x1b[38;5;127m"
    gold: str = "\x1b[38;5;214m"
    gray: str = "\x1b[38;5;145m"
    dark_gray: str = "\x1b[38;5;59m"
    blue: str = "\x1b[38;5;63m"
    green: str = "\x1b[38;5;83m"
    aqua: str = "\x1b[38;5;87m"
    red: str = "\x1b[38;5;203m"
    light_purple: str = "\x1b[38;5;207m"
    yellow: str = "\x1b[38;5;227m"
    white: str = "\x1b[38;5;231m"
