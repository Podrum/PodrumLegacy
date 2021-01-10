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

from podrum.network.raknet.protocol.Packet import Packet
from podrum.network.raknet.protocol.PacketIdentifiers import PacketIdentifiers
from podrum.network.raknet.RakNet import RakNet

class ConnectionRequestAccepted(Packet):
    id = PacketIdentifiers.connectionRequestAccepted
    clientAddress = None
    systemIndex = None
    systemAddresses = []
    requestTimestamp = None
    timestamp = None
    
    def decodePayload(self):
        self.clientAddress = self.getAddress()
        self.systemIndex = self.getShort()
        for i in range(0, RakNet.systemAddressCount):
            self.systemAddresses.insert(i, self.getAddress())
        self.requestTimestamp = self.getLong()
        self.timestamp = self.getLong()
        
    def encodePayload(self):
        self.putAddress(self.clientAddress)
        self.putShort(self.systemIndex)
        for address in self.systemAddresses:
            self.putAddress(address)
        self.putLong(self.requestTimestamp)
        self.putLong(self.timestamp)
