from rakpy.protocol.Packet import Packet
from rakpy.protocol.PacketIdentifiers import PacketIdentifiers

class ConnectionRequest(Packet):
    id = PacketIdentifiers.ConnectionRequest
    
    clientId = None
    time = None
    useSecure = None
    
    def encodePayload(self):
        self.putLong(self.clientId)
        self.putLong(self.time)
        self.putByte(self.useSecure)
        
    def decodePayload(self):
        self.clientId = self.getLong()
        self.time = self.getLong()
        self.useSecure = self.getByte()
