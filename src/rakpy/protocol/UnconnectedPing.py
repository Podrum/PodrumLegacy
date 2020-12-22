from rakpy.protocol.OfflinePacket import OfflinePacket
from rakpy.protocol.PacketIdentifiers import PacketIdentifiers

class UnconnectedPing(OfflinePacket):
    id = PacketIdentifiers.UnconnectedPing
    
    time = None
    clientId = None
    
    def encodePayload(self):
        self.putLong(self.time)
        self.putMagic()
        try:
            self.putLong(self.clientId)
        except:
            pass
        
    def decodePayload(self):
        self.time = self.getLong()
        self.magic = self.getMagic()
        try:
            self.clientId = self.getLong()
        except:
            pass
    
