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
from podrum.network.raknet.RakNet import RakNet
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
        packet = Frame()
        flags = stream.getByte()
        packet.reliability = (flags & 224) >> 5
        packet.isFragmented = (flags & RakNet.flagFragment) > 0
        length = stream.getShort() >> 3
        if length == 0:
            raise Exception("Got empty frame!")
        if Reliability.isReliable(packet.reliability):
            packet.reliableIndex = stream.getLTriad()
        if Reliability.isSequenced(packet.reliability):
            packet.sequencedIndex = stream.getLTriad()
        if Reliability.isOrdered(packet.reliability):
            packet.orderedIndex = stream.getLTriad()
            packet.orderChannel = stream.getByte()
        if packet.isFragmented:
            packet.fragmentSize = stream.getInt()
            packet.fragmentId = stream.getShort()
            packet.fragmentIndex = stream.getInt()
        packet.body = stream.get(length)
        return packet
    
    def toStream(self):
        stream = BinaryStream()
        flags = self.reliability << 5
        if self.isFragmented:
            flags |= RakNet.flagFragment
        stream.putByte(flags)
        stream.putShort(len(self.body) << 3)
        if Reliability.isReliable(self.reliability):
            stream.putLTriad(self.reliableIndex)
        if Reliability.isSequenced(self.reliability):
            stream.putLTriad(self.sequencedIndex)
        if Reliability.isOrdered(self.reliability):
            stream.putLTriad(self.orderedIndex)
            stream.putByte(self.orderChannel)
        if self.isFragmented:
            stream.putInt(self.fragmentSize)
            stream.putShort(self.fragmentId)
            stream.putInt(self.fragmentIndex)
        stream.put(packet.body)
        return stream
    
    def getFrameLength(self):
        length = 0
        if Reliability.isReliable(self.reliability):
            length += 3
        if Reliability.isSequenced(self.reliability):
            length += 3
        if Reliability.isOrdered(self.reliability):
            length += 4
        if self.isFragmented:
            length += 10
        return length
