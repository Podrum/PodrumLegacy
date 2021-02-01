"""
*  ____           _
* |  _ \ ___   __| |_ __ _   _ _ __ ___
* | |_) / _ \ / _` | '__| | | | '_ ` _ \
* |  __/ (_) | (_| | |  | |_| | | | | | |
* |_|   \___/ \__,_|_|   \__,_|_| |_| |_|
*
* Licensed under the Mozilla Public License, Version 2.
* Permissions of this weak copyleft license are conditioned on making
* available source code of licensed files and modifications of those files 
* under the same license (or in certain cases, one of the GNU licenses).
* Copyright and license notices must be preserved. Contributors
* provide an express grant of patent rights. However, a larger work
* using the licensed work may be distributed under different terms and without 
* source code for files added in the larger work.
"""

from podrum.network.mcbe.protocol.BatchPacket import BatchPacket
from podrum.network.mcbe.protocol.Info import Info
from podrum.network.mcbe.protocol.PlayStatusPacket import PlayStatusPacket
from podrum.network.mcbe.protocol.ResourcePacksInfoPacket import ResourcePacksInfoPacket
from podrum.network.raknet.protocol.Frame import Frame

class BedrockPlayer:
    connection = None
    address = None
    name = None
    locale = None
    randomId = None
    uuid = None
    xuid = None
    skin = None
    viewDistance = None
    gamemode = 0
    pitch = 0
    yaw = 0
    headYaw = 0
    onGround = False
    deviceOs = None
    deviceModel = None
    deviceId = None

    def __init__(self, connection, address):
        self.connection = connection
        self.address = address
        
    def handleDataPacket(self, packet):
        if packet.networkId == Info.LOGIN_PACKET:
            self.name = packet.displayName
            self.locale = packet.languageCode
            self.randomId = packet.clientRandomId
            self.uuid = packet.identity
            self.xuid = packet.xuid
            self.deviceId = packet.deviceId
            self.deviceOs = packet.deviceOs
            self.deviceModel = packet.deviceModel  
            self.skin = packet.skin
            self.sendPlayStatus(0)
            newPacket = ResourcePacksInfoPacket()
            self.sendDataPacket(newPacket)
            
    def sendPlayStatus(self, status):
        packet = PlayStatusPacket()
        packet.status = status
        self.sendDataPacket(packet)
            
    def sendDataPacket(self, packet):
        newPacket = BatchPacket()
        newPacket.addPacket(packet)
        newPacket.encode()
        frame = Frame()
        frame.reliability = 0
        frame.body = newPacket.buffer
        self.connection.addFrameToQueue(frame)
