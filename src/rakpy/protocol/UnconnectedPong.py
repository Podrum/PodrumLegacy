from rakpy.protocol.OfflinePacket import OfflinePacket
from rakpy.protocol.PacketIdentifiers import PacketIdentifiers

class UnconnectedPong(OfflinePacket):
    id = PacketIdentifiers.UnconnectedPong
    
    time = 0
    serverId = 0
    serverName = ""
    
    def encodePayload(self):
        self.putLong(self.time)
        self.putLong(self.serverId)
        self.putMagic()
        self.putString(self.serverName)
        
    def decodePayload(self):
        self.time = self.getLong()
        self.serverId = self.getLong()
        self.magic = self.getMagic()
        self.serverName = self.getString()
