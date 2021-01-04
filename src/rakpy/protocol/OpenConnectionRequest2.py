from rakpy.protocol.OfflinePacket import OfflinePacket
from rakpy.protocol.PacketIdentifiers import PacketIdentifiers
from rakpy.utils.InternetAddress import InternetAddress

class OpenConnectionRequest2(OfflinePacket):
    id = PacketIdentifiers.OpenConnectionRequest2
    
    serverAddress = InternetAddress("127.0.0.1", 0, 4)
    mtu = 0
    clientId = 0
    
    def encodePayload(self):
        self.putMagic()
        self.putAddress(self.serverAddress)
        self.putShort(self.mtu)
        self.putLong(self.clientId)
        
    def decodePayload(self):
        self.magic = self.getMagic()
        self.serverAddress = self.getAddress()
        self.mtu = self.getShort()
        self.clientId = self.getLong()
