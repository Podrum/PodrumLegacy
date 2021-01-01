from rakpy.protocol.Packet import Packet
from rakpy.protocol.PacketIdentifiers import PacketIdentifiers

class ConnectedPong(Packet):
    id = PacketIdentifiers.ConnectedPong
    
    pingTime = None
    pongTime = None
    
    def encodePayload(self):
        self.putLong(self.pingTime)
        self.putLong(self.pongTime)
        
    def decodePayload(self):
        self.pingTime = self.getLong()
        self.pongTime = self.getLong()
