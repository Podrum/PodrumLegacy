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
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
from abc import ABCMeta, abstractmethod
from pyraklib.protocol.EncapsulatedPacket import EncapsulatedPacket
from pyraklib.protocol.Packet import Packet


class DataPacket(Packet):
    __metaclass__ = ABCMeta

    packets = []
    seqNumber = None

    @staticmethod
    @abstractmethod
    def getPID() -> int: pass

    def _encode(self):
        self.putByte(self.getPID(), False)
        self.putLTriad(self.seqNumber)
        for packet in self.packets:
            if isinstance(packet, EncapsulatedPacket):
                self.put(packet.toBinary())
            else:
                self.put(packet)

    def length(self) -> int:
        length = 4
        for packet in self.packets:
            if isinstance(packet, EncapsulatedPacket):
                length += packet.getTotalLength()
            else:
                length += len(packet)

        return length

    def _decode(self):
        self.get()
        self.seqNumber = self.getLTriad()
        while not self.feof():
            offset = 0
            data = self.buffer[0:offset]
            packet, offsetReturned = EncapsulatedPacket.fromBinary(data, False, offset)
            self.offset += offsetReturned
            if len(packet.buffer) == 0:
                break
            self.packets.append(packet)

    def clean(self):
        super().clean()
        self.packets = []
        self.seqNumber = None
