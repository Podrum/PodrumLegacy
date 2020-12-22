import socket

from binutilspy.BinaryStream import BinaryStream
from rakpy.utils.InternetAddress import InternetAddress

class Packet(BinaryStream):
    id = -1
    
    sendTime = None
    
    def getString(self):
        return self.get(self.getShort())

    def putString(self, value):
        self.putShort(len(value))
        self.put(value.encode())
    
    def getAddress(self):
        ver = self.getByte()
        if ver == 4:
            addr = ".".join([
                str((~self.getByte()) & 0xff),
                str((~self.getByte()) & 0xff),
                str((~self.getByte()) & 0xff),
                str((~self.getByte()) & 0xff)
            ])
            port = self.getShort()
            return InternetAddress(addr, port, ver)
        elif ver == 6:
            self.getLShort()
            port = self.getShort()
            self.getInt()
            addr = socket.inet_ntop(socket.AF_INET6, self.get(16))
            self.getInt()
            return InternetAddress(addr, port, ver)
        else:
            raise Exception(f"Unknown address version {ver}")

    def putAddress(self, address: InternetAddress):
        ver = address.getVersion()
        addr = address.getAddress()
        port = address.getPort()
        self.putByte(ver)
        if ver == 4:
            parts = str(addr).split(".")
            partsLength = len(parts)
            assert partsLength == 4, f"Expected address length: 4, got {partsLength}"
            for part in parts:
                self.putByte((~(int(part))) & 0xff)
            self.putShort(port)
        elif ver == 6:
            self.putLShort(socket.AF_INET6)
            self.putShort(port)
            self.putInt(0)
            self.put(socket.inet_pton(socket.AF_INET6, addr))
            self.putInt(0)
        else:
            raise Exception(f"Unknown address version {ver}")
    
    def encodeHeader(self):
        self.putByte(self.id)
        
    def encodePayload(self): pass
        
    def encode(self):
        self.reset()
        self.encodeHeader()
        self.encodePayload()
        
    def decodePayload(self): pass
    
    def decodeHeader(self):
        return self.getByte()
    
    def decode(self):
        self.offset = 0
        self.decodeHeader()
        self.decodePayload()
