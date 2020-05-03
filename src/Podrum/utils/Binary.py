from struct import unpack, pack
import uuid

class Binary

    BIG_ENDIAN = 0x00
    LITTLE_ENDIAN = 0x01

    @staticmethod
    def strlen(x):
        return len(x)
    
    @staticmethod
    def checkLength(str, expect):
        len = self.strlen(str)
        assert (len == expect), f'Expected {str(expect)} bytes, got {str(len)}'

    @staticmethod
    def readTriad(str):
        self.checkLength(str, 3)
        return unpack('>L', b'\x00' + str)[0]

    @staticmethod
    def writeTriad(str):
        self.checkLength(str, 3)
        return pack('>L', str)[1:]

    @staticmethod
    def readLTriad(str):
        self.checkLength(str, 3)
        return unpack('<L', b'\x00' + str)[0]

    @staticmethod
    def writeLTriad(str):
        self.checkLength(str, 3)
        return pack('<L', value)[0:-1]
    
    @staticmethod
    def readBool(b):
        return unpack('?', b)[0]

    @staticmethod
    def writeBool(b):
        return b'\x01' if b else b'\x00'
    
    @staticmethod
    def readByte(b):
        return ord(b)

    @staticmethod
    def writeByte(b):
        return chr(b).encode()
