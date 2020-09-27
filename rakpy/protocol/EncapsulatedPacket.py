from binutilspy.Binary import Binary
from rakpy.protocol.BitFlags import BitFlags
from rakpy.protocol.Reliability import Reliability

class EncapsulatedPacket:
    buffer = b""
    reliability = None
    messageIndex = None
    sequenceIndex = None
    orderIndex = None
    orderChannel = None
    split = None
    splitCount = None
    splitIndex = None
    splitId = None
    needAck = False
    identifierAck = None
    
    def fromBinary(self, buffer):
        offset = 0
        packet = EncapsulatedPacket()
        header = Binary.readByte(buffer[offset])
        offset += 1
        packet.reliability = (header & 224) >> 5
        packet.split = (header & BitFlags.Split) > 0
        length = Binary.readShort(buffer[offset:offset + 2])
        length >>= 3
        offset += 2
        if length == 0:
            raise Exception("Got an empty encapsulated packet")
        if Reliability.isReliable(packet.reliability):
            packet.messageIndex = Binary.readLTriad(buffer[offset:offset + 3])
            offset += 3
        if Reliability.isSequenced(packet.reliability):
            packet.sequenceIndex = Binary.readLTriad(buffer[offset:offset + 3])
            offset += 3
        if Reliability.isSequencedOrOrdered(packet.reliability):
            packet.orderIndex = Binary.readLTriad(buffer[offset:offset + 3])
            offset += 3
            packet.orderChannel = Binary.readByte(buffer[offset:offset + 1])
            offset += 1
        if packet.split:
            packet.splitCount = Binary.readInt(buffer[offset:offset + 4])
            offset += 4
            packet.splitId = Binary.readShort(buffer[offset:offset + 2])
            offset += 2
            packet.splitIndex = Binary.readInt(buffer[offset:offset + 4])
            offset += 4
        packet.buffer = buffer[offset:offset + length]
        offset += length
        return packet
    
    def toBinary(self):
        buffer = b""
        header = self.reliability << 5
        if self.split:
            header |= BitFlags.Split
        buffer += Binary.writeByte(header)
        buffer += Binary.writeShort(len(self.buffer) << 3)
        if Reliability.isReliable(self.reliability):
            buffer += Binary.writeLTriad(self.messageIndex)
        if Reliability.isSequenced(self.reliability):
            buffer += Binary.writeLTriad(self.sequenceIndex)
        if Reliability.isSequencedOrOrdered(self.reliability):
            buffer += Binary.writeLTriad(self.orderIndex)
            buffer += Binary.writeByte(self.orderChannel)
        if self.split:
            buffer += Binary.writeInt(self.splitCount)
            buffer += Binary.writeShort(self.splitId)
            buffer += Binary.writeInt(self.splitIndex)
        return buffer + self.buffer
    
    def getTotalLength(self):
        value = 3
        value += len(self.buffer)
        value += 3 if self.messageIndex != None else 0
        value += 4 if self.orderIndex != None else 0
        value += 10 if self.split else 0
        
