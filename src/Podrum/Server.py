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
from pyraklib.server import PyRakLibServer
from pyraklib.server import ServerHandler

from .utils import logger, fs


class Server(Thread):
    def __init__(self, path):
        super().__init__()
        fs.checkAllFiles(path)
        port = 19132
        logger.log('info', 'Starting server...')
        logger.log('info', '____           _\n|  _ \ ___   __| |_ __ _   _ _ __ ___ \n | |_) / _ \ / _` | '__| | | | '_ ` _ \ \n |  __/ (_) | (_| | |  | |_| | | | | | | \n |_|   \___/ \__,_|_|   \__,_|_| |_| |_|')
        logger.log('info', 'Podrum is licensed under the GPLv3 license')
        server = PyRakLibServer(port)
        logger.log('info', 'Starting server on *:' + str(port))

        ticking = True
        while ticking:
            time.sleep(0.002)
