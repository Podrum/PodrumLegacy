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
from pyraklib.protocol.Packet import Packet


class CLIENT_HANDSHAKE_DataPacket(Packet):
    PID = 0x13

    address = None
    port = None

    systemAddresses = ()

    sendPing = None
    sendPong = None

    def _encode(self):
        self.putByte(self.PID)
        self.putAddress(self.address, self.port, 4) #TODO: Correct version
        for i in range(0, 10):
            addr = self.systemAddresses[i]
            self.putAddress(addr[0], addr[1], addr[2])
        self.putLong(self.sendPing)
        self.putLong(self.sendPong)

    def _decode(self):
        self.get()
        self.address, self.port = self.getAddress()
        for i in range(0, 10):
            self.systemAddresses[i] = self.getAddress()
        self.sendPing = self.getLong()
        self.sendPong = self.getLong()
