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
from re import match
import sys

class Binary:

    def checkLength(string, expect):
        len = len(string)
        assert (len == expect), 'Expected ' + str(expect) + 'bytes, got ' + str(len)

    @staticmethod
    def readTriad(str):
        Binary.checkLength(str, 3)
        return unpack('>L', b'\x00' + str)[0]

    @staticmethod
    def writeTriad(value):
        return pack('>L', value)[1:]

    @staticmethod
    def readLTriad(str):
        Binary.checkLength(str, 3)
        return unpack('<L', b'\x00' + str)[0]

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
    def readByte(c):
        Binary.checkLength(c, 1)
        return ord(c)
    
    @staticmethod
    def readSignedByte(c):
        Binary.checkLength(c, 1)
        b = ord(c)
        if calcsize("P") == 8:
            shift = << 56 >> 56
        else:
            shift = << 24 >> 24
        return b shift

    @staticmethod
    def writeByte(c):
        return chr(c)
    
    @staticmethod
    def readShort(str):
        Binary.checkLength(str, 2)
        return unpack('>H', str)[0]
    
    @staticmethod
    def readSignedShort(str):
        Binary.checkLength(str, 2)
        if calcsize("P") == 8:
            return unpack('>H', str)[0] << 48 >> 48
        else:
            return unpack('>H', str)[0] << 16 >> 16

    @staticmethod
    def writeShort(value):
        return pack('>H', value)
    
    @staticmethod
    def readLShort(str):
        Binary.checkLength(str, 2)
        return unpack('<H', str)[0]
    
    @staticmethod
    def readSignedLShort(str):
        Binary.checkLength(str, 2)
        if calcsize("P") == 8:
            return unpack('<H', str)[0] << 48 >> 48
        else:
            return unpack('<H', str)[0] << 16 >> 16

    @staticmethod
    def writeLShort(value):
        return pack('<H', value)
    
    @staticmethod
    def readInt(str):
        Binary.checkLength(str, 4)
        return unpack('>L', str)[0]

    @staticmethod
    def writeInt(value):
        return pack('>L', value)

    @staticmethod
    def readLInt(str):
        Binary.checkLength(str, 4)
        return unpack('<L', str)[0]

    @staticmethod
    def writeLInt(value):
        return pack('<L', value)

    @staticmethod
    def readFloat(str):
        Binary.checkLength(str, 4)
        return unpack('>f', str)[0]
    
    @staticmethod
    def readRoundedFloat(str, accuracy):
        return round(Binary.readFloat(str), accuracy)

    @staticmethod
    def writeFloat(value):
        return pack('>f', value)

    @staticmethod
    def readLFloat(str):
        Binary.checkLength(str, 4)
        return unpack('<f', str)[0]
    
    @staticmethod
    def readRoundedLFloat(str, accuracy):
        return round(Binary.readLFloat(str), accuracy)

    @staticmethod
    def writeLFloat(value):
        return pack('<f', value)
    
    
    @staticmethod
    def printFloat(value):
        return match(r"/(\\.\\d+?)0+$/", "" + value).group(1)

    @staticmethod
    def readDouble(str):
        Binary.checkLength(str, 8)
        return unpack('>d', str)[0]

    @staticmethod
    def writeDouble(value):
        return pack('>d', value)

    @staticmethod
    def readLDouble(str):
        Binary.checkLength(str, 8)
        return unpack('<d', str)[0]

    @staticmethod
    def writeLDouble(value):
        return pack('<d', value)

    @staticmethod
    def readLong(str):
        Binary.checkLength(str, 8)
        return unpack('>L', str)[0]

    @staticmethod
    def writeLong(value):
        return pack('>L', value)

    @staticmethod
    def readLLong(str):
        Binary.checkLength(str, 8)
        return unpack('<L', str)[0]

    @staticmethod
    def writeLLong(value):
        return pack('<L', value)
   
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
    
    @staticmethod
    def readUnsignedVarLong(buffer, offset):
        value = 0
        i = 0
        for i in range(0, 63):
            i += 7
            offset += 1
            b = ord(buffer[offset])
            value |= ((b & 0x7f) << i)

            if (b & 0x80) == 0:
                return value
            elif (len(buffer) - 1) < int(offset):
                raise TypeError("Expected more bytes, none left to read")

        raise TypeError("VarLong did not terminate after 10 bytes!")
        
    @staticmethod
    def readVarLong(buffer, offset):
        raw = Binary.readUnsignedVarLong(buffer, offset)
        temp = (((raw << 63) >> 63) ^ raw) >> 1
        return temp ^ (raw & (1 << 63))
    
    @staticmethod
    def write_unsigned_var_long(value):
        buffer = ""
        i = 1
        for i in range(0, 10):
            i = i + 1
            if (value >> 7) != 0:
                buffer += chr(value | 0x80)
            else:
                buffer += chr(value & 0x7f)
                return buffer
            value = ((value >> 7) & (sys.maxsize >> 6))

        raise TypeError("Value too large to be encoded as a VarLong")
    
    @staticmethod
    def flipShortEndianness(value):
        return Binary.readLShort(Binary.writeShort(value))

    @staticmethod
    def flipIntEndianness(value):
        return Binary.readLInt(Binary.writeInt(value))

    @staticmethod
    def flipLongEndianness(value):
        return Binary.readLLong(Binary.writeLong(value))
