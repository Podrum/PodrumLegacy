from copy import deepcopy
from rakpy.protocol.BitFlags import BitFlags
from rakpy.protocol.EncapsulatedPacket import EncapsulatedPacket
from rakpy.protocol.Packet import Packet
from rakpy.protocol.PacketIdentifiers import PacketIdentifiers

class DataPacket(Packet):
    id = BitFlags.Valid | 0
    
    packets = []
    sequenceNumber = None
    
    def encodePayload(self):
        self.putLTriad(self.sequenceNumber)
        for packet in self.packets:
            self.put(packet.toBinary() if isinstance(packet, EncapsulatedPacket) else packet)
        
    def decodePayload(self):
        self.sequenceNumber = self.getLTriad()
        while not self.feof():
            data = self.buffer[self.offset:]
            if data == b"":
                break
            packet = EncapsulatedPacket().fromBinary(data)
            self.packets.append(packet)
            self.offset += len(data)
            
    def length(self):
        length = 4
        for packet in self.packets:
            length += packet.getTotalLength() if isinstance(packet, EncapsulatedPacket) else len(packet.getBuffer())
        return length
