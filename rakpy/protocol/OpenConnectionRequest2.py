from rakpy.protocol.OfflinePacket import OfflinePacket
from rakpy.protocol.PacketIdentifiers import PacketIdentifiers

class OpenConnectionRequest2(OfflinePacket):
    id = PacketIdentifiers.OpenConnectionRequest2
    
    serverAddress = None
    mtu = None
    clientId = None
    
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
