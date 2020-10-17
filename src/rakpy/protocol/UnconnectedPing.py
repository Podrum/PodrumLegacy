from rakpy.protocol.OfflinePacket import OfflinePacket
from rakpy.protocol.PacketIdentifiers import PacketIdentifiers

class UnconnectedPing(OfflinePacket):
    id = PacketIdentifiers.UnconnectedPing
    
    time = None
    clientId = None
    
    def encodePayload(self):
        self.putLong(self.time)
        self.putMagic()
        self.putLong(self.clientId)
        
    def decodePayload(self):
        self.time = self.getLong()
        self.magic = self.getMagic()
        self.clientId = self.getLong()
    
