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
        return ord(self.get(1))

    def putByte(self, value):
        self.put(bytes([value]))
        
    def getBool(self):
        return self.getByte() != 0
    
    def putBool(self, value):
        self.putByte(1 if value else 0)
        
    def getShort(self):
        return struct.unpack(">h", self.get(2))[0]
    
    def putShort(self, value):
        self.put(struct.pack(">h", value))
        
    def getLShort(self):
        return struct.unpack("<h", self.get(2))[0]
    
    def putLShort(self, value):
        self.put(struct.pack("<h", value))
        
    def getUnsignedShort(self):
        return struct.unpack(">H", self.get(2))[0]
    
    def putUnsignedShort(self, value):
        self.put(struct.pack(">H", value))
        
    def getUnsignedLShort(self):
        return struct.unpack("<H", self.get(2))[0]
    
    def putUnsignedLShort(self, value):
        self.put(struct.pack("<H", value))
        
    def getTriad(self):
        return struct.unpack(">i", b"\x00" + self.get(3))[0]
    
    def putTriad(self, value):
        self.put(struct.pack(">i", value)[1:])
        
    def getLTriad(self):
        return struct.unpack("<i", self.get(3) + b"\x00")[0]
    
    def putLTriad(self, value):
        self.put(struct.pack("<i", value)[:-1])
        
    def getUnsignedTriad(self):
        return struct.unpack(">I", b"\x00" + self.get(3))[0]
    
    def putUnsignedTriad(self, value):
        self.put(struct.pack(">I", value)[1:])
        
    def getUnsignedLTriad(self):
        return struct.unpack("<I", self.get(3) + b"\x00")[0]
    
    def putUnsignedLTriad(self, value):
        self.put(struct.pack("<I", value)[:-1])
        
    def getInt(self):
        return struct.unpack(">i", self.get(4))[0]
    
    def putInt(self, value):
        self.put(struct.pack(">i", value))
        
    def getLInt(self):
        return struct.unpack("<i", self.get(4))[0]
    
    def putLInt(self, value):
        self.put(struct.pack("<i", value))
        
    def getUnsignedInt(self):
        return struct.unpack(">I", self.get(4))[0]
    
    def putUnsignedInt(self, value):
        self.put(struct.pack(">I", value))
        
    def getUnsignedLInt(self):
        return struct.unpack("<I", self.get(4))[0]
    
    def putUnsignedLInt(self, value):
        self.put(struct.pack("<I", value))

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
        
    def getUnsignedLong(self):
        return struct.unpack(">Q", self.get(8))[0]
    
    def putUnsignedLong(self, value):
        self.put(struct.pack(">Q", value))
        
    def getUnsignedLLong(self):
        return struct.unpack("<Q", self.get(8))[0]
    
    def putUnsignedLLong(self, value):
        self.put(struct.pack("<Q", value))
        
    def getVarInt(self):
        raw = self.getUnsignedVarInt()
        temp = -(raw >> 1) - 1 if (raw & 1) else raw >> 1
        return temp
    
    def getUnsignedVarInt(self):
        numRead = 0
        result = 0
        while True:
            if self.feof():
                raise Exception("No bytes left in the buffer")
            read = self.getByte()
            value = (read & 0x7f)
            result |= (value << (7 * numRead))
            numRead += 1
            if numRead > 5:
                raise Exception("VarInt too big")
            if (read & 0x80) == 0:
                break
        return result
        
        
    def putVarInt(self, value):
        return self.putUnsignedVarInt(value << 1 if value >= 0 else (-value - 1) << 1 | 1)
    
    def putUnsignedVarInt(self, value):
        while True:
            temp = (value & 0x7f)
            value >>= 7
            if value != 0:
                temp |= 0x80
            self.putByte(temp)
            if value == 0:
                break
        
    def getVarLong(self):
        raw = self.getUnsignedVarLong()
        temp = -(raw >> 1) - 1 if (raw & 1) else raw >> 1
        return temp
    
    def getUnsignedVarLong(self):
        numRead = 0
        result = 0
        while True:
            if self.feof():
                raise Exception("No bytes left in the buffer")
            read = self.getByte()
            value = (read & 0x7f)
            result |= (value << (7 * numRead))
            numRead += 1
            if numRead > 10:
                raise Exception("VarLong too big")
            if (read & 0x80) == 0:
                break
        return result
        
    def putVarLong(self, value):
        return self.putUnsignedVarLong(value << 1 if value >= 0 else (-value - 1) << 1 | 1)
    
    def putUnsignedVarLong(self, value):
        while True:
            temp = (value & 0x7f)
            value >>= 7
            if value != 0:
                temp |= 0x80
            self.putByte(temp)
            if value == 0:
                break
        
    def feof(self):
        return len(self.buffer) <= self.offset or self.offset < 0
    
    def getRemaining(self):
        buffer = self.buffer[self.offset:]
        self.offset = len(self.buffer)
        return buffer

    def reset(self):
        self.buffer = b""
        self.offset = 0
