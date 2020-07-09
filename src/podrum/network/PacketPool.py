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

from podrum.network.protocol.AdventureSettingsPacket import AdventureSettingsPacket
from podrum.network.protocol.ClientToServerHandshakePacket import ClientToServerHandshakePacket
from podrum.network.protocol.DataPacket import DataPacket
from podrum.network.protocol.DisconnectPacket import DisconnectPacket
from podrum.network.protocol.LoginPacket import LoginPacket
from podrum.network.protocol.PlayStatusPacket import PlayStatusPacket
from podrum.network.protocol.ResourcePacksInfoPacket import ResourcePacksInfoPacket
from podrum.network.protocol.ServerToClientHandshakePacket import ServerToClientHandshakePacket

class PacketPool:
    packetPool = {}
    
    def __init__(self):
        self.registerPackets()
        
    def registerPacket(packet):
        self.pool[packet.NID] = packet.copy()
        
    def registerPackets(self):
        self.registerPacket(AdventureSettingsPacket)
        self.registerPacket(ClientToServerHandshakePacket)
        self.registerPacket(DisconnectPacket)
        self.registerPacket(LoginPacket)
        self.registerPacket(PlayStatusPacket)
        self.registerPacket(ResourcePacksInfoPacket)
        self.registerPacket(ServerToClientHandshakePacket)
        
