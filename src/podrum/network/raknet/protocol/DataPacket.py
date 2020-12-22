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

from podrum.network.raknet.protocol.EncapsulatedPacket import EncapsulatedPacket
from podrum.network.raknet.protocol.Packet import Packet

class DataPacket(Packet):
    id = 0x80
    packets = []
    sequenceNumber = None
    
    def decodePayload(self):
        self.sequenceNumber = self.getLTriad()
        while not self.feof():
            self.packets.append(EncapsulatedPacket.fromBinary(self))

    def encodePayload(self):
        self.putLTriad(self.sequenceNumber)
        for packet in self.packets:
            self.put(packet.toBinary())
        
    def length(self):
        length = 4
        for packet in self.packets:
            length += packet.getTotalLength()
        return length
