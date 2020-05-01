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

from .utils import logger, fs


class Server(Thread):
    def __init__(self, path):
        super().__init__()
        fs.checkAllFiles(path)
        logger.log('info', 'Starting server...')

        ticking = True
        while ticking:
            time.sleep(0.002)
