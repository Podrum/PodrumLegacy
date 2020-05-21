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
import sys
import signal

class Utils:

    def getOS():
        if sys.platform == 'linux' or sys.platform == 'linux2':
            return 'linux'
        elif sys.platform == 'darwin':
            return 'osx'
        elif sys.platform == 'win32' or sys.platform == 'win64':
            return 'windows'
