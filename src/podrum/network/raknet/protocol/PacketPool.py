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

from podrum.network.raknet.protocol.Ack import Ack
from podrum.network.raknet.protocol.AdvertiseSystem import AdvertiseSystem
from podrum.network.raknet.protocol.ConnectionRequest import ConnectionRequest
from podrum.network.raknet.protocol.ConnectionRequestAccepted import ConnectionRequestAccepted
from podrum.network.raknet.protocol.DisconnectNotification import DisconnectNotification
from podrum.network.raknet.protocol.FrameSetPacket import FrameSetPacket
from podrum.network.raknet.protocol.Nack import Nack
from podrum.network.raknet.protocol.NewIncomingConnection import NewIncomingConnection
from podrum.network.raknet.protocol.OfflinePing import OfflinePing
from podrum.network.raknet.protocol.OfflinePingOpenConnections import OfflinePingOpenConnections
from podrum.network.raknet.protocol.OfflinePong import OfflinePong
from podrum.network.raknet.protocol.OnlinePing import OnlinePing
from podrum.network.raknet.protocol.OnlinePong import OnlinePong
from podrum.network.raknet.protocol.OpenConnectionReply1 import OpenConnectionReply1
from podrum.network.raknet.protocol.OpenConnectionReply2 import OpenConnectionReply2
from podrum.network.raknet.protocol.OpenConnectionRequest1 import OpenConnectionRequest1
from podrum.network.raknet.protocol.OpenConnectionRequest2 import OpenConnectionRequest2

class PacketPool:
    pool = {}

    def __init__(self):
        self.registerPackets()
   
    def registerPacket(self, packet):
        self.pool[packet.id] = packet
        
    def registerPackets(self):
        self.registerPacket(Ack())
        self.registerPacket(AdvertiseSystem())
        self.registerPacket(ConnectionRequest())
        self.registerPacket(ConnectionRequestAccepted())
        self.registerPacket(DisconnectNotification())
        for identifier in range(0x80, 0x8f + 1):
            frameSetPacket = FrameSetPacket()
            frameSetPacket.id = identifier
            self.registerPacket(frameSetPacket)
        self.registerPacket(Nack())
        self.registerPacket(NewIncomingConnection())
        self.registerPacket(OfflinePing())
        self.registerPacket(OfflinePingOpenConnections())
        self.registerPacket(OfflinePong())
        self.registerPacket(OnlinePing())
        self.registerPacket(OnlinePong())
        self.registerPacket(OpenConnectionReply1())
        self.registerPacket(OpenConnectionReply2())
        self.registerPacket(OpenConnectionRequest1())
        self.registerPacket(OpenConnectionRequest2())
