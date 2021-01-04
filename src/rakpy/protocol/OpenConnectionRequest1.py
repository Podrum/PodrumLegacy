from rakpy.protocol.OfflinePacket import OfflinePacket
from rakpy.protocol.PacketIdentifiers import PacketIdentifiers

class OpenConnectionRequest1(OfflinePacket):
    id = PacketIdentifiers.OpenConnectionRequest1
    
    protocolVersion = 0
    mtu = 0
    
    def encodePayload(self):
        self.putMagic()
        self.putByte(self.protocolVersion)
        self.buffer.ljust(self.mtu, b"\x00")
        
    def decodePayload(self):
        self.magic = self.getMagic()
        self.protocolVersion = self.getByte()
        self.mtu = len(self.buffer)
