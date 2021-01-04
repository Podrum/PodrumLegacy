from rakpy.protocol.OfflinePacket import OfflinePacket
from rakpy.protocol.PacketIdentifiers import PacketIdentifiers

class UnconnectedPing(OfflinePacket):
    id = PacketIdentifiers.UnconnectedPing
    
    time = 0
    clientId = 0
    
    def encodePayload(self):
        self.putLong(self.time)
        self.putMagic()
        
    def decodePayload(self):
        self.time = self.getLong()
        self.magic = self.getMagic()
