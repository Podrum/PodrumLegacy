from rakpy.protocol.OfflinePacket import OfflinePacket
from rakpy.protocol.PacketIdentifiers import PacketIdentifiers

class OpenConnectionReply2(OfflinePacket):
    id = PacketIdentifiers.OpenConnectionReply2
    
    serverId = None
    clientAddress = None
    mtu = None
    encryptionEnabled = None
    
    def encodePayload(self):
        self.putMagic()
        self.putLong(self.serverId)
        self.putAddress(self.clientAddress)
        self.putShort(self.mtu)
        self.putBool(self.encryptionEnabled)
        
    def decodePayload(self):
        self.magic = self.getMagic()
        self.serverId = self.getLong()
        self.clientAddress = self.getAddress()
        self.mtu = self.getShort()
        self.encryptionEnabled = self.getBool()
