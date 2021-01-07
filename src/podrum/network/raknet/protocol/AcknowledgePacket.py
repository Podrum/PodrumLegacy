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

class AcknowledgePacket(Packet):
    sequenceNumbers = []
    
    def decodePayload(self):
        self.sequenceNumbers = []
        recordCount = self.getShort()
        for i in range(0, recordCount):
            isSingle = self.getBool()
            if not isSingle:
                start = self.getLTriad()
                end = self.getLTriad()
                for sequenceNumber in range(start, end + 1):
                    self.sequenceNumbers.append(sequenceNumber)
                    if len(self.sequenceNumbers) > 4096:
                        raise Exception("Max sequence number count exceeded")
            else:
                self.sequenceNumbers.append(self.getLTriad())
                
    def encodePayload(self):
        recordCount = len(self.sequenceNumbers)
        if recordCount > 0:
            self.putShort(recordCount)
            self.putBool(True if recordCount == 1 else False)
            self.putTriad(self.sequenceNumbers[0])
            if recordCount > 1:
                self.putTriad(self.sequenceNumbers[-1])
