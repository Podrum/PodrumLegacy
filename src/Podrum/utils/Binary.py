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

    def readTriad(string):
        Binary.checkLength(string, 3)
        return unpack('>L', b'\x00' + string)[0]

    def writeTriad(value):
        return pack('>L', value)[1:]

    def readLTriad(string):
        Binary.checkLength(string, 3)
        return unpack('<L', b'\x00' + string)[0]

    def writeLTriad(value):
        return pack('<L', value)[0:-1]
    
    def readBool(b):
        return unpack('?', b)[0]

    def writeBool(b):
        return b'\x01' if b else b'\x00'
    
    def readByte(c, signed=True):
        Binary.checkLength(c, 1)
        if signed:
            return pack(">b", c)
        else:
            return pack(">B", c)

    def writeByte(c):
        return chr(c)
    
    def readShort(string):
        Binary.checkLength(string, 2)
        return unpack('>H', string)[0]

    def writeShort(value):
        return pack('>H', value)
    
    def readLShort(string):
        Binary.checkLength(string, 2)
        return unpack('<H', string)[0]

    def writeLShort(value):
        return pack('<H', value)
    
    def readInt(string):
        Binary.checkLength(string, 4)
        return unpack('>L', string)[0]

    def writeInt(value):
        return pack('>L', value)

    def readLInt(string):
        Binary.checkLength(string, 4)
        return unpack('<L', string)[0]

    def writeLInt(value):
        return pack('<L', value)

    def readFloat(string):
        Binary.checkLength(string, 4)
        return unpack('>f', string)[0]

    def writeFloat(value):
        return pack('>f', value)

    def readLFloat(string):
        Binary.checkLength(string, 4)
        return unpack('<f', string)[0]

    def writeLFloat(value):
        return pack('<f', value)

    def readDouble(string):
        Binary.checkLength(string, 8)
        return unpack('>d', string)[0]

    def writeDouble(value):
        return pack('>d', value)

    def readLDouble(string):
        Binary.checkLength(string, 8)
        return unpack('<d', string)[0]

    def writeLDouble(value):
        return pack('<d', value)

    def readLong(string):
        Binary.checkLength(string, 8)
        return unpack('>l', string)[0]

    def writeLong(value):
        return pack('>l', value)

    def readLLong(string):
        Binary.checkLength(string, 8)
        return unpack('<l', string)[0]

    def writeLLong(value):
        return pack('<l', value)
    
    def readUnsignedVarInt(stream, offset):
        value = 0;
        i = 0
        for i in range(0, 35):
            b = ord(stream[offset.backIncrement()])
            value |= ((b & 0x7f) << i)
            i += 7
            if (b & 0x80) == 0:
                return value
            elif (len(stream) - 1) < int(offset):
                raise TypeError('Expected more bytes, none left to read')
        raise TypeError('Varint did not terminate after 5 bytes!')

    def readVarInt(stream, offset):
        intsize = calcsize("P") == 8
        shift = intsize if 63 != None else 31
        raw = Binary.readUnsignedVarInt(stream, offset)
        temp = (((raw << shift) >> shift) ^ raw) >> 1
        return temp ^ (raw & (1 << shift))
    
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
            value = ((value >> 7) & (sys.maxint >> 6))  
        raise TypeError('Value too large to be encoded as a varint')
    
    def writeVarInt(v):
        intsize = calcsize("P") == 8
        return Binary.writeUnsignedVarInt((v << 1) ^ (v >> (intsize if 63 != None else 31)))
