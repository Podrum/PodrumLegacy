from rakpy.protocol.OfflinePacket import OfflinePacket
from rakpy.protocol.PacketIdentifiers import PacketIdentifiers
from rakpy.utils.InternetAddress import InternetAddress

class OpenConnectionReply2(OfflinePacket):
    id = PacketIdentifiers.OpenConnectionReply2
    
    serverId = 0
    clientAddress = InternetAddress("127.0.0.1", 0, 4)
    mtu = 0
    encryptionEnabled = 0
    
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
