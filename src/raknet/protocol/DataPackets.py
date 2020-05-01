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
from pyraklib.protocol.DataPacket import DataPacket


class DATA_PACKET_0(DataPacket):
    @staticmethod
    def getPID(): return 0x80

class DATA_PACKET_1(DataPacket):
    @staticmethod
    def getPID(): return 0x81

class DATA_PACKET_2(DataPacket):
    @staticmethod
    def getPID(): return 0x82

class DATA_PACKET_3(DataPacket):
    @staticmethod
    def getPID(): return 0x83

class DATA_PACKET_4(DataPacket):
    @staticmethod
    def getPID(): return 0x84

class DATA_PACKET_5(DataPacket):
    @staticmethod
    def getPID(): return 0x85

class DATA_PACKET_6(DataPacket):
    @staticmethod
    def getPID(): return 0x86

class DATA_PACKET_7(DataPacket):
    @staticmethod
    def getPID(): return 0x87

class DATA_PACKET_8(DataPacket):
    @staticmethod
    def getPID(): return 0x88

class DATA_PACKET_9(DataPacket):
    @staticmethod
    def getPID(): return 0x89

class DATA_PACKET_A(DataPacket):
    @staticmethod
    def getPID(): return 0x8A

class DATA_PACKET_B(DataPacket):
    @staticmethod
    def getPID(): return 0x8B

class DATA_PACKET_C(DataPacket):
    @staticmethod
    def getPID(): return 0x8C

class DATA_PACKET_D(DataPacket):
    @staticmethod
    def getPID(): return 0x8D

class DATA_PACKET_E(DataPacket):
    @staticmethod
    def getPID(): return 0x8E

class DATA_PACKET_F(DataPacket):
    @staticmethod
    def getPID(): return 0x8F