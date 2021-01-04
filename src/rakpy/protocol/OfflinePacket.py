from rakpy.protocol.Packet import Packet

class OfflinePacket(Packet):
    raknetMagic = b"\x00\xff\xff\x00\xfe\xfe\xfe\xfe\xfd\xfd\xfd\xfd\x12\x34\x56\x78"
    magic = b""
    
    def getMagic(self):
        self.magic = self.get(16)
        
    def putMagic(self):
        self.put(self.raknetMagic)
        
    def isValid(self):
        return self.magic == self.raknetMagic
