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
import binascii
import os
import signal
import sys
import socket
import time
import urllib

class Utils:

    def getOS():
        if sys.platform == 'linux' or sys.platform == 'linux2':
            return 'linux'
        elif sys.platform == 'darwin':
            return 'osx'
        elif sys.platform == 'win32' or sys.platform == 'win64':
            return 'windows'
        
    def killServer():
        os.kill(os.getpid(), signal.SIGTERM)
    
    def getPrivateIpAddress():
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        return ip
    
    def getPublicIpAddress():
        ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
        return ip
    
    def microtime(get_as_float = False) :
        if get_as_float:
            return time.time()
        else:
            return '%f %d' % math.modf(time.time())
        
    def substr(string, start, length = None):
        if start < 0:
            start = start + len(string)
        if not length:
            return string[start:]
        elif length > 0:
            return string[start:start + length]
        else:
            return string[start:length]
        
    def hex2bin(hexdec):
        if hexdec == 'x':
            return False
        dec = int(hexdec, 16)
        b = binascii.unhexlify('%x' % dec)
        return b
