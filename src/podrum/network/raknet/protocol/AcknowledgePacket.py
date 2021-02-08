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
from podrum.utils.BinaryStream import BinaryStream

class AcknowledgePacket(Packet):
    sequenceNumbers = []
    
    def decodePayload(self):
        self.sequenceNumbers = []
        recordCount = self.getUnsignedShort()
        for i in range(0, recordCount):
            isSingle = self.getBool()
            if not isSingle:
                start = self.getUnsignedLTriad()
                end = self.getUnsignedLTriad()
                for sequenceNumber in range(start, end + 1):
                    self.sequenceNumbers.append(sequenceNumber)
                    if len(self.sequenceNumbers) > 4096:
                        raise Exception("Max sequence number count exceeded")
            else:
                self.sequenceNumbers.append(self.getLTriad())
                
    def encodePayload(self):
        self.sequenceNumbers.sort()
        recordCount = 0
        count = len(self.sequenceNumbers)
        stream = BinaryStream()
        if count > 0:
            start = self.sequenceNumbers[0]
            end = self.sequenceNumbers[0]
            for i in range(1, count):
                current = self.packets[i]
                if (current - end) == 1:
                    end = current
                elif (current - end) > 1:
                    if start == end:
                        stream.putByte(True)
                        stream.putUnsignedLTriad(start)
                        start = end = current
                    else:
                        stream.putByte(False)
                        stream.putUnsignedLTriad(start)
                        stream.putUnsignedLTriad(end)
                        start = end = current
                    recordCount += 1
            if start == end:
                stream.putByte(True)
                stream.putUnsignedLTriad(start)
            else:
                stream.putByte(False)
                stream.putUnsignedLTriad(start)
                stream.putUnsignedLTriad(end)
            recordCount += 1
        self.putUnsignedShort(recordCount)
        self.put(stream.buffer)
