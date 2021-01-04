from rakpy.utils.InternetAddress import InternetAddress
from rakpy.protocol.Packet import Packet
from rakpy.protocol.PacketIdentifiers import PacketIdentifiers

class NewIncomingConnection(Packet):
    id = PacketIdentifiers.NewIncomingConnection
    
    address = InternetAddress("127.0.0.1", 0, 4)
    systemAddresses = []
    pingTime = 0
    pongTime = 0
    
    def encodePayload(self):
        self.putAddress(self.address)
        for address in self.systemAddresses:
            self.putAddress(address)
        self.putLong(self.pingTime)
        self.putLong(self.pongTime)
        
    def decodePayload(self):
        self.address = self.getAddress()
        i = 0
        while i < 20:
            self.systemAddresses.append(self.getAddress())
            i += 1
        self.pingTime = self.getLong()
        self.pongTime = self.getLong()
