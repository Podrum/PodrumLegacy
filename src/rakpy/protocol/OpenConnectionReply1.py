from rakpy.protocol.OfflinePacket import OfflinePacket
from rakpy.protocol.PacketIdentifiers import PacketIdentifiers

class OpenConnectionReply1(OfflinePacket):
    id = PacketIdentifiers.OpenConnectionReply1
    
    serverId = 0
    useSecurity = 0
    mtu = 0
    
    def encodePayload(self):
        self.putMagic()
        self.putLong(self.serverId)
        self.putBool(self.useSecurity)
        self.putShort(self.mtu)
        
    def decodePayload(self):
        self.magic = self.getMagic()
        self.serverId = self.getLong()
        self.useSecurity = self.getBool()
        self.mtu = self.getShort()
