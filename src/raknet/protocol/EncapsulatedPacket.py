"""
PyRakLib networking library.
   This software is not affiliated with RakNet or Jenkins Software LLC.
   This software is a port of PocketMine/RakLib <https://github.com/PocketMine/RakLib>.
   All credit goes to the PocketMine Project (http://pocketmine.net)
 
   Copyright (C) 2015  PyRakLib Project

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
from pyraklib.Binary import Binary


class EncapsulatedPacket:
    reliability = None
    hasSplit = False
    length = 0
    messageIndex = None
    orderIndex = None
    orderChannel = None
    splitCount = None
    splitID = None
    splitIndex = None
    buffer = bytearray()
    needACK = False
    identifierACK = None

    @staticmethod
    def fromBinary(binary, internal = False, offset = None):
        if isinstance(binary, str):
            binary = bytes(binary, "UTF-8")
        packet = EncapsulatedPacket()
        flags = binary[0]
        packet.reliability = (flags & 0b11100000) >> 5
        packet.hasSplit = (flags & 0b00010000) > 0
        if internal:
            length = Binary.readInt(binary[1:5])
            packet.identifierACK = Binary.readInt(binary[5:9])
            offset = 9
        else:
            length = int(Binary.readShort(binary[1:3]) / 8)
            offset = 3
            packet.identifierACK = None

        if packet.reliability > 0:
            if (packet.reliability > 2 or packet.reliability == 2) and packet.reliability is not 5:
                packet.messageIndex = Binary.readLTriad(binary[offset:offset+3])
                offset += 3

            if (packet.reliability < 4 or packet.reliability == 4) and packet.reliability is not 2:
                packet.orderIndex = Binary.readLTriad(binary[offset:offset+3])
                offset += 3
                packet.orderChannel = Binary.readByte(binary[offset:offset+1])
                offset += 1

        if packet.hasSplit:
            packet.splitCount = Binary.readInt(binary[offset:offset+4])
            offset += 4
            packet.splitID = Binary.readShort(binary[offset:offset+2])
            offset += 2
            packet.splitIndex = binary.readInt(binary[offset:offset+4])
            offset += 4

        packet.buffer = binary[offset:offset+length]
        offset += length

        return packet, offset

    def getTotalLength(self):
        length = 3 + len(self.buffer)
        if self.messageIndex is not None:
            length += 3
        if self.orderIndex is not None:
            length += 4
        if self.hasSplit:
            length += 10

        return length

    def toBinary(self, internal = False):
        payload = bytearray()
        if self.hasSplit:
            payload += (Binary.writeByte((self.reliability << 5) | 0b00010000))
        else :
            payload += (Binary.writeByte(self.reliability << 5))

        if internal:
            payload += (Binary.writeInt(len(self.buffer)))
            payload += (Binary.writeInt(self.identifierACK))
        else:
            payload += (Binary.writeShort(len(self.buffer) << 3))

        if self.reliability > 0:
            if (self.reliability > 2 or self.reliability == 2) and self.reliability is not 5:
                payload += (Binary.writeLTriad(self.messageIndex))
            if (self.reliability < 4 or self.reliability == 4) and self.reliability is not 2:
                payload += (Binary.writeLTriad(self.orderIndex))
                payload += (Binary.writeByte(self.orderChannel))

        if self.hasSplit:
            payload += (Binary.writeInt(self.splitCount))
            payload += (Binary.writeShort(self.splitID))
            payload += (Binary.writeInt(self.splitIndex))

        payload += (self.buffer)

        return payload