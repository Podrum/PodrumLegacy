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
from abc import abstractmethod
from pyraklib.Binary import Binary
from pyraklib.protocol.Packet import Packet


class AcknowledgePacket(Packet):

    seqNums = ()

    @staticmethod
    @abstractmethod
    def getPID(): pass

    def _encode(self):
        super().clean()
        payload = bytearray()
        self.seqNums = sorted(self.seqNums)
        count = len(self.seqNums)
        records = 0

        if count > 0:
            pointer = 1
            start = self.seqNums[0]
            last = self.seqNums[0]

            while pointer < count:
                pointer += 1
                if pointer == count: break
                current = self.seqNums[pointer]
                diff = current - last
                if diff == 1:
                    last = current
                elif diff > 1:
                    if start == last:
                        payload += bytes("\x01", "UTF-8")
                        payload += (Binary.writeLTriad(start))
                        start = last = current
                    else:
                        payload += bytes("\x01", "UTF-8")
                        payload += (Binary.writeLTriad(start))
                        payload += (Binary.writeLTriad(last))
                        start = last = current
                    records =+ 1

            if start == last:
                payload += bytes("\x01", "UTF-8")
                payload += (Binary.writeLTriad(start))
                start = last = current
            else:
                payload += bytes("\x01", "UTF-8")
                payload += (Binary.writeLTriad(start))
                payload += (Binary.writeLTriad(last))
                start = last = current

        self.putByte(self.getPID(), False)
        self.putShort(records)
        self.put(payload)

    def _decode(self):
        self.get()
        count = self.getShort()
        self.seqNums = ()
        cnt = 0
        i = 0
        while i < count and not self.feof() and cnt < 4096:
            if self.getByte() == 0:
                start = self.getLTriad()
                end = self.getLTriad()
                if (end - start) > 512:
                    end = start + 512
                c = start
                while c == end or c < end:
                    cnt =+ 1
                    self.seqNums[cnt] = c
                    c =+ 1
            else:
                cnt =+ 1
                self.seqNums[cnt] = self.getLTriad()
            i =+ 1

    def clean(self):
        super().clean()
        self.seqNums = ()