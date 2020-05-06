from struct import unpack, pack
import sys

class Binary:

    @staticmethod
    def strlen(x):
        return len(x)
    
    @staticmethod
    def checkLength(string, expect):
        len = self.strlen(string)
        assert (len == expect), 'Expected ' + str(expect) + 'bytes, got ' + str(len)

    @staticmethod
    def readTriad(string):
        self.checkLength(string, 3)
        return unpack('>L', b'\x00' + string)[0]

    @staticmethod
    def writeTriad(value):
        return pack('>L', value)[1:]

    @staticmethod
    def readLTriad(string):
        self.checkLength(string, 3)
        return unpack('<L', b'\x00' + string)[0]

    @staticmethod
    def writeLTriad(value):
        return pack('<L', value)[0:-1]
    
    @staticmethod
    def readBool(b):
        return unpack('?', b)[0]

    @staticmethod
    def writeBool(b):
        return b'\x01' if b else b'\x00'
    
    @staticmethod
    def readByte(c, signed=True):
        self.checkLength(c, 1)
        if signed:
            return pack(">b", c)
        else:
            return pack(">B", c)

    @staticmethod
    def writeByte(c):
        return chr(c)
    
    @staticmethod
    def readShort(string):
        self.checkLength(string, 2)
        return unpack('>H', string)[0]

    @staticmethod
    def writeShort(value):
        return pack('>H', value)
    
    @staticmethod
    def readLShort(string):
        self.checkLength(string, 2)
        return unpack('<H', string)[0]

    @staticmethod
    def writeLShort(value):
        return pack('<H', value)
    
    @staticmethod
    def readInt(string):
        self.checkLength(string, 4)
        return unpack('>L', string)[0]

    @staticmethod
    def writeInt(value):
        return pack('>L', value)

    @staticmethod
    def readLInt(string):
        self.checkLength(string, 4)
        return unpack('<L', string)[0]

    @staticmethod
    def writeLInt(value):
        return pack('<L', value)

    @staticmethod
    def readFloat(string):
        self.checkLength(string, 4)
        return unpack('>f', string)[0]

    @staticmethod
    def writeFloat(value):
        return pack('>f', value)

    @staticmethod
    def readLFloat(string):
        self.checkLength(string, 4)
        return unpack('<f', string)[0]

    @staticmethod
    def writeLFloat(value):
        return pack('<f', value)

    @staticmethod
    def readDouble(string):
        self.checkLength(string, 8)
        return unpack('>d', string)[0]

    @staticmethod
    def writeDouble(value):
        return pack('>d', value)

    @staticmethod
    def readLDouble(string):
        self.checkLength(string, 8)
        return unpack('<d', string)[0]

    @staticmethod
    def writeLDouble(value):
        return pack('<d', value)

    @staticmethod
    def readLong(string):
        self.checkLength(string, 8)
        return unpack('>l', string)[0]

    @staticmethod
    def writeLong(value):
        return pack('>l', value)

    @staticmethod
    def readLLong(string):
        self.checkLength(string, 8)
        return unpack('<l', string)[0]

    @staticmethod
    def writeLLong(value):
        return pack('<l', value)
    
    @staticmethod
    def readUnsignedVarint(stream):
        value = 0;
        i = 0
        while(true):
            if(i > 63):
                raise ValueError('Varint did not terminate after 10 bytes!')
            b = stream.encode()
            value |= (b << i)
            i += 7
            if(b & 0x80):
                break
    
        return value
    
    @staticmethod
    def writeUnsignedVarint(value):
        buf = ""
        for i in range(0, 10):
            if((value >> 7) != 0):
                buf = chr(value | 0x80)
                raise ValueError('Varint did not terminate after 10 bytes!')
            else:
                buf = chr(value & 0x7f)
                return buf
            value = ((value >> 7) & (sys.maxint >> 6))  
        raise ValueError('Value too large to be encoded as a varint')
        
    @staticmethod
    def readVarint(stream):
        intsize = sys.getsizeof(int()) == 8
        shift = intsize if 63 != None else 31
        raw = self.readUnsignedVarInt(stream)
        temp = (((raw << shift) >> shift) ^ raw) >> 1
        return temp ^ (raw & (1 << shift))
    
    @staticmethod
    def writeVarint(v):
        intsize = sys.getsizeof(int()) == 8
        return self.writeUnsignedVarInt((v << 1) ^ (v >> (intsize if 63 != None else 31)))
