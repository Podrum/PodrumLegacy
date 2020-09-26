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

from rakpy.server.Server import Server
from rakpy.server.ServerInterface import ServerInterface
from rakpy.utils.InternetAddress import InternetAddress
from rakpy.utils.MinecraftServerName import MinecraftServerName

class NetworkInterface(ServerInterface):
    raknetServer = None
    name = None
    players = {}

    def __init__():
        self.raknetServer = Server(InternetAddress("0.0.0.0", 19132), self)
        self.name = self.getServerName.toString()
        self.raknetServer.name = self.name
        
    @staticmethod
    def onOpenConnection(connection):
        address = connection.address
        self.players[f"{address.getAddress()}:{address.getPort()}"] = player
 
    def getServerName(self):
        serverName = MinecraftServerName()
        serverName.edition = "MCPE"
        serverName.name = "MyServer"
        serverName.motd = "MyServer"
        serverName.protocol = 408
        serverName.version = "1.16.20"
        serverName.players["online"] = 0
        serverName.players["max"] = 0
        serverName.gamemode = "Creative"
        serverName.serverId = 0
        return serverName
        
