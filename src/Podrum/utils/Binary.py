"""
*  ____           _
* |  _ \ ___   __| |_ __ _   _ _ __ ___
* | |_) / _ \ / _` | '__| | | | '_ ` _ \
* |  __/ (_) | (_| | |  | |_| | | | | | |
* |_|   \___/ \__,_|_|   \__,_|_| |_| |_|
*
* This program is free software: you can redistribute it and/or modify
* it under the terms of the GNU Lesser General Public License as published by
* the Free Software Foundation, either version 3 of the License, or
* (at your option) any later version.
"""
from struct import unpack, pack, calcsize
import sys

class Binary:

    def strlen(x):
        return len(x)
    
    def checkLength(string, expect):
        len = Binary.strlen(string)
        assert (len == expect), 'Expected ' + str(expect) + 'bytes, got ' + str(len)

    @staticmethod
    def readTriad(string):
        Binary.checkLength(string, 3)
        return unpack('>L', b'\x00' + string)[0]

    @staticmethod
    def writeTriad(value):
        return pack('>L', value)[1:]

    @staticmethod
    def readLTriad(string):
        Binary.checkLength(string, 3)
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
        Binary.checkLength(c, 1)
        if signed:
            return pack(">b", c)
        else:
            return pack(">B", c)

    @staticmethod
    def writeByte(c):
        return chr(c)
    
    @staticmethod
    def readShort(string):
        Binary.checkLength(string, 2)
        return unpack('>H', string)[0]

    @staticmethod
    def writeShort(value):
        return pack('>H', value)
    
    @staticmethod
    def readLShort(string):
        Binary.checkLength(string, 2)
        return unpack('<H', string)[0]

    @staticmethod
    def writeLShort(value):
        return pack('<H', value)
    
    @staticmethod
    def readInt(string):
        Binary.checkLength(string, 4)
        return unpack('>L', string)[0]

    @staticmethod
    def writeInt(value):
        return pack('>L', value)

    @staticmethod
    def readLInt(string):
        Binary.checkLength(string, 4)
        return unpack('<L', string)[0]

    @staticmethod
    def writeLInt(value):
        return pack('<L', value)

    @staticmethod
    def readFloat(string):
        Binary.checkLength(string, 4)
        return unpack('>f', string)[0]

    @staticmethod
    def writeFloat(value):
        return pack('>f', value)

    @staticmethod
    def readLFloat(string):
        Binary.checkLength(string, 4)
        return unpack('<f', string)[0]

    @staticmethod
    def writeLFloat(value):
        return pack('<f', value)

    @staticmethod
    def readDouble(string):
        Binary.checkLength(string, 8)
        return unpack('>d', string)[0]

    @staticmethod
    def writeDouble(value):
        return pack('>d', value)

    @staticmethod
    def readLDouble(string):
        Binary.checkLength(string, 8)
        return unpack('<d', string)[0]

    @staticmethod
    def writeLDouble(value):
        return pack('<d', value)

    @staticmethod
    def readLong(string):
        Binary.checkLength(string, 8)
        return unpack('>l', string)[0]

    @staticmethod
    def writeLong(value):
        return pack('>l', value)

    @staticmethod
    def readLLong(string):
        Binary.checkLength(string, 8)
        return unpack('<l', string)[0]

    @staticmethod
    def writeLLong(value):
        return pack('<l', value)
   
    @staticmethod
    def readUnsignedVarInt(stream, offset):
        value = 0;
        i = 0
        for i in range(0, 35):
            offset += 1
            b = ord(stream[offset])
            value |= ((b & 0x7f) << i)
            i += 7
            if (b & 0x80) == 0:
                return value
            elif (len(stream) - 1) < int(offset):
                raise TypeError('Expected more bytes, none left to read')
        raise TypeError('Varint did not terminate after 5 bytes!')

    @staticmethod
    def readVarInt(stream, offset):
        intsize = calcsize("P") == 8
        shift = intsize if 63 != None else 31
        raw = Binary.readUnsignedVarInt(stream, offset)
        temp = (((raw << shift) >> shift) ^ raw) >> 1
        return temp ^ (raw & (1 << shift))
    
    @staticmethod
    def writeUnsignedVarInt(value):
        buf = ""
        value = value & 0xffffffff
        i = 1
        for i in range(0, 5):
            i = i + 1
            if (value >> 7) != 0:
                buf += chr(value | 0x80)
                raise TypeError('Varint did not terminate after 5 bytes!')
            else:
                buf += chr(value & 0x7f)
                return buf
            value = ((value >> 7) & (sys.maxsize >> 6))  
        raise TypeError('Value too large to be encoded as a varint')
    
    @staticmethod
    def writeVarInt(v):
        intsize = calcsize("P") == 8
        return Binary.writeUnsignedVarInt((v << 1) ^ (v >> (intsize if 63 != None else 31)))
