"""
*  ____           _
* |  _ \ ___   __| |_ __ _   _ _ __ ___
* | |_) / _ \ / _` | '__| | | | '_ ` _ \
* |  __/ (_) | (_| | |  | |_| | | | | | |
* |_|   \___/ \__,_|_|   \__,_|_| |_| |_|
*
* Licensed under the Apache License, Version 2.0 (the "License")
* you may not use this file except in compliance with the License.
* You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
"""

from copy import deepcopy

from podrum.network.PacketPool import PacketPool
from podrum.utils.Binary import Binary

from pyraklib.server.PyRakLibServer import PyRakLibServer
from pyraklib.server.ServerHandler import ServerHandler

class NetworkInterface:
    server = None
    players = []
    identifers = None
    identifiersACK = []
    interface = None
    tickTask = None
    upload = 0
    download = 0
    
    def __init__(self, server):
        self.server = server
        self.identifers = []
        
