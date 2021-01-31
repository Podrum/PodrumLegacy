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

from podrum.network.raknet.protocol.Frame import Frame
from podrum.network.raknet.protocol.Packet import Packet

class FrameSetPacket(Packet):
    id = 0x80
    sequenceNumber = None
    frames = []
    
    def decodePayload(self):
        self.sequenceNumber = self.getLTriad()
        while not self.feof():
            self.frames.append(Frame.fromStream(self))
                
    def encodePayload(self):
        self.putLTriad(self.sequenceNumber)
        for frame in self.frames:
            self.put(frame.toStream().buffer)
            
    def getLength(self):
        length = 3
        for frame in self.frames:
            length += frame.getFrameLength()
        return length
