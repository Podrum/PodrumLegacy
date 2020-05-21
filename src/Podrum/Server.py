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
import time
from ..pyraklib.server import PyRakLibServer
from ..pyraklib.server import ServerHandler

from .utils import logger, fs
from .network import ipAddr

logo = """
    ____           _                      
   |  _ \ ___   __| |_ __ _   _ _ __ ___  
   | |_) / _ \ / _` | '__| | | | '_ ` _ \ 
   |  __/ (_) | (_| | |  | |_| | | | | | |
   |_|   \___/ \__,_|_|   \__,_|_| |_| |_|"""

class Server:
    def __init__(self, path):
        super().__init__()
        self.path = path
        fs.checkAllFiles(path)
        port = 19132
        print(str(logo))
        logger.log('info', f'Starting server on {ipAddr.getPrivateIpAddr()}:{str(port)}')
        logger.log('info', f'This is your external ip: {ipAddr.getPublicIpAddr()}. If you want players that are not '
                           f'in your local network you must portforward')
        logger.log('info', 'Podrum is licensed under the GPLv3 license')
        server = PyRakLibServer(port=19132)
        handler = ServerHandler(server, None)
        handler.sendOption("name", "MCPE;Podrum powered server;390;1.14.60;0;0;0;PodrumPoweredServer;0")

        ticking = True
        while ticking:
            time.sleep(0.002)


def command(string, fromConsole):
    if string.lower() == 'stop':
        quit()
    else:
        logger.log('error', 'Invalid command')
