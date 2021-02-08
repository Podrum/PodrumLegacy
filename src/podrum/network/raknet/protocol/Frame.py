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

from podrum.network.raknet.protocol.Reliability import Reliability
from podrum.utils.BinaryStream import BinaryStream

class Frame:
    reliability = None
    isFragmented = None
    reliableIndex = None
    sequencedIndex = None
    orderedIndex = None
    orderChannel = None
    fragmentSize = None
    fragmentId = None
    fragmentIndex = None
    body = None

    @staticmethod
    def fromStream(stream):
        frame = Frame()
        flags = stream.getByte()
        frame.reliability = (flags & 224) >> 5
        frame.isFragmented = (flags & 0x10) > 0
        length = stream.getUnsignedShort() >> 3
        if length == 0:
            raise Exception("Got empty frame!")
        if Reliability.isReliable(frame.reliability):
            frame.reliableIndex = stream.getUnsignedLTriad()
        if Reliability.isSequenced(frame.reliability):
            frame.sequencedIndex = stream.getUnsignedLTriad()
        if Reliability.isOrdered(frame.reliability):
            frame.orderedIndex = stream.getUnsignedLTriad()
            frame.orderChannel = stream.getByte()
        if frame.isFragmented:
            frame.fragmentSize = stream.getInt()
            frame.fragmentId = stream.getUnsignedShort()
            frame.fragmentIndex = stream.getInt()
        frame.body = stream.get(length)
        return frame
    
    def toStream(self):
        stream = BinaryStream()
        flags = self.reliability << 5
        if self.isFragmented:
            flags |= 0x10
        stream.putByte(flags)
        stream.putUnsignedShort(len(self.body) << 3)
        if Reliability.isReliable(self.reliability):
            stream.putUnsignedLTriad(self.reliableIndex)
        if Reliability.isSequenced(self.reliability):
            stream.putUnsignedLTriad(self.sequencedIndex)
        if Reliability.isOrdered(self.reliability):
            stream.putUnsignedLTriad(self.orderedIndex)
            stream.putByte(self.orderChannel)
        if self.isFragmented:
            stream.putInt(self.fragmentSize)
            stream.putUnsignedShort(self.fragmentId)
            stream.putInt(self.fragmentIndex)
        stream.put(self.body)
        return stream
    
    def getFrameLength(self):
        length = 3
        if Reliability.isReliable(self.reliability):
            length += 3
        if Reliability.isSequenced(self.reliability):
            length += 3
        if Reliability.isOrdered(self.reliability):
            length += 4
        if self.isFragmented:
            length += 10
        length += len(self.body)
        return length
