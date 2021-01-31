"""
*  ____           _
* |  _ \ ___   __| |_ __ _   _ _ __ ___
* | |_) / _ \ / _` | '__| | | | '_ ` _ \
* |  __/ (_) | (_| | |  | |_| | | | | | |
* |_|   \___/ \__,_|_|   \__,_|_| |_| |_|
*
* Licensed under the Mozilla Public License, Version 2.
* Permissions of this weak copyleft license are conditioned on making
* available source code of licensed files and modifications of those files 
* under the same license (or in certain cases, one of the GNU licenses).
* Copyright and license notices must be preserved. Contributors
* provide an express grant of patent rights. However, a larger work
* using the licensed work may be distributed under different terms and without 
* source code for files added in the larger work.
"""

import struct

class BinaryStream:
    buffer = b""
    offset = 0
    
    def __init__(self, buffer = b"", offset = 0):
        self.buffer = buffer
        self.offset = offset
        
    def get(self, length):
        self.offset += length
        return self.buffer[self.offset - length:self.offset]

    def put(self, data):
        self.buffer += data
        
    def getByte(self):
        return struct.unpack("B", self.get(1))[0]
    
    def getSignedByte(self):
        return struct.unpack("b", self.get(1))[0]

    def putByte(self, value):
        self.put(bytes([value & 0xff]))
        
    def getBool(self):
        return self.getByte() != 0
    
    def putBool(self, value):
        self.putByte(1 if value else 0)
        
    def getShort(self):
        return struct.unpack(">H", self.get(2))[0]
    
    def getSignedShort(self):
        return struct.unpack(">h", self.get(2))[0]
    
    def putShort(self, value):
        self.put(struct.pack(">H", value))
        
    def getLShort(self):
        return struct.unpack("<H", self.get(2))[0]
    
    def getSignedLShort(self):
        return struct.unpack("<h", self.get(2))[0]
    
    def putLShort(self, value):
        self.put(struct.pack("<h", value))
        
    def getTriad(self):
        return struct.unpack(">i", b"\x00" + self.get(3))[0]
    
    def putTriad(self, value):
        self.put(struct.pack(">i", value)[1:])
        
    def getLTriad(self):
        return struct.unpack("<I", self.get(3) + b"\x00")[0]
    
    def putLTriad(self, value):
        self.put(struct.pack("<I", value)[:-1])
        
    def getInt(self):
        return struct.unpack(">i", self.get(4))[0]
    
    def putInt(self, value):
        self.put(struct.pack(">i", value))
        
    def getLInt(self):
        return struct.unpack("<i", self.get(4))[0]
    
    def putLInt(self, value):
        self.put(struct.pack("<i", value))

    def getFloat(self):
        return struct.unpack(">f", self.get(4))[0]
    
    def getRoundedFloat(self):
        return round(self.getFloat())
    
    def putFloat(self, value):
        self.put(struct.pack(">f", value))
        
    def getLFloat(self):
        return struct.unpack("<f", self.get(4))[0]
    
    def getRoundedLFloat(self):
        return round(self.getLFloat())
    
    def putLFloat(self, value):
        self.put(struct.pack("<f", value))

    def getDouble(self):
        return struct.unpack(">d", self.get(8))[0]
    
    def putDouble(self, value):
        self.put(struct.pack(">d", value))
        
    def getLDouble(self):
        return struct.unpack("<d", self.get(8))[0]
    
    def putLDouble(self, value):
        self.put(struct.pack("<d", value))

    def getLong(self):
        return struct.unpack(">q", self.get(8))[0]
    
    def putLong(self, value):
        self.put(struct.pack(">q", value))
        
    def getLLong(self):
        return struct.unpack("<q", self.get(8))[0]
    
    def putLLong(self, value):
        self.put(struct.pack("<q", value))
        
    def getVarInt(self):
        raw = self.getUnsignedVarInt()
        temp = -(raw >> 1) - 1 if (raw & 1) else raw >> 1
        return temp
    
    def getUnsignedVarInt(self):
        value = 0
        i = 0
        while i <= 28:
            if self.feof():
                raise Exception("No bytes left in the buffer")
            b = self.getByte()
            value |= ((b & 0x7f) << i)
            if (b & 0x80) == 0:
                return value
            i += 7
        raise Exception("VarInt did not terminate after 5 bytes!")
        
    def putVarInt(self, value):
        return self.putUnsignedVarInt(value << 1 if value >= 0 else (-value - 1) << 1 | 1)
    
    def putUnsignedVarInt(self, value):
        stream = BinaryStream()
        value &= 0xffffffff
        i = 0
        while i < 5:
            if (value >> 7) != 0:
                stream.putByte(value | 0x80)
            else:
                stream.putByte(value & 0x7f)
                self.put(stream.buffer)
                return
            value >>= 7
            i += 1
        self.put(stream.buffer)
        
    def getVarLong(self):
        raw = self.getUnsignedVarLong()
        temp = -(raw >> 1) - 1 if (raw & 1) else raw >> 1
        return temp
    
    def getUnsignedVarLong(self):
        value = 0
        i = 0
        while i <= 63:
            if self.feof():
                raise Exception("No bytes left in the buffer")
            b = self.getByte()
            value |= ((b & 0x7f) << i)
            if (b & 0x80) == 0:
                return value
            i += 7
        raise Exception("VarInt did not terminate after 10 bytes!")
        
    def putVarLong(self, value):
        return self.putUnsignedVarLong(value << 1 if value >= 0 else (-value - 1) << 1 | 1)
    
    def putUnsignedVarLong(self, value):
        i = 0
        while i < 10:
            if (value >> 7) != 0:
                self.putByte(value | 0x80)
            else:
                self.putByte(value & 0x7f)
                break
            value >>= 7
            i += 1

    def feof(self):
        return len(self.buffer) <= self.offset or self.offset < 0
    
    def getRemaining(self):
        buffer = self.buffer[self.offset:]
        self.offset = len(self.buffer)
        return buffer

    def reset(self):
        self.buffer = b""
        self.offset = 0
