from rakpy.protocol.OfflinePacket import OfflinePacket
from rakpy.protocol.PacketIdentifiers import PacketIdentifiers

class IncompatibleProtocol(OfflinePacket):
    id = PacketIdentifiers.IncompatibleProtocol
    
    protocol = None
    serverId = None
    
    def encodePayload(self):
        self.putByte(self.protocol)
        self.putMagic()
        self.putLong(self.serverId)
        
    def decodePayload(self):
        self.protocol = self.getByte()
        self.magic = self.getMagic()
        self.serverId = self.getLong()
