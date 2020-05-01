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

from threading import Thread
import time
#from ..pyraklib.server import PyRakLibServer
#from ..pyraklib.server import ServerHandler

from .utils import logger, fs
from .network import ipAddr

logo = """  ____           _                      
 |  _ \ ___   __| |_ __ _   _ _ __ ___  
 | |_) / _ \ / _` | '__| | | | '_ ` _ \ 
 |  __/ (_) | (_| | |  | |_| | | | | | |
 |_|   \___/ \__,_|_|   \__,_|_| |_| |_|"""


class Server(Thread):
    def __init__(self, path):
        super().__init__()
        self.path = path
        fs.checkAllFiles(path)
        port = 19132
        print(logo)
        logger.log('info', f'Starting server on {ipAddr.getIpPublicAddr()}:{str(port)}')
        logger.log('info', 'Podrum is licensed under the GPLv3 license')
        #server = PyRakLibServer(port)


        ticking = True
        while ticking:
            time.sleep(0.002)


if __name__ == '__main__':
    server = Server()
