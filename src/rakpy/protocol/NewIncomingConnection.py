from rakpy.utils.InternetAddress import InternetAddress
from rakpy.protocol.Packet import Packet
from rakpy.protocol.PacketIdentifiers import PacketIdentifiers

class NewIncomingConnection(Packet):
    id = PacketIdentifiers.NewIncomingConnection
    
    address = None
    systemAddresses = []
    pingTime = None
    pongTime = None
    
    def encodePayload(self):
        self.putAddress(self.address)
        for address in self.systemAddresses:
            self.putAddress(address)
        self.putLong(self.pingTime)
        self.putLong(self.pongTime)
        
    def decodePayload(self):
        self.address = self.getAddress()
        for i in range(0, 20):
            if self.getOffset >= len(self.getBuffer) - 16:
                self.systemAddresses.append(InternetAddress("0.0.0.0", 0, 4))
            else:
                self.systemAddresses.append(self.getAddress())
        self.pingTime = self.getLong()
        self.pongTime = self.getLong()
