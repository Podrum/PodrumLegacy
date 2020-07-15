"""
*  ____           _
* |  _ \ ___   __| |_ __ _   _ _ __ ___
* | |_) / _ \ / _` | '__| | | | '_ ` _ \
* |  __/ (_) | (_| | |  | |_| | | | | | |
* |_|   \___/ \__,_|_|   \__,_|_| |_| |_|
*
* Licensed under the Apache License, Version 2.0 (the "License")
* you may not use this file except in compliance with the License.
* You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
"""

from struct import pack, unpack, calcsize 
import sys

class Binary:
    BIG_ENDIAN = 0x00
    LITTLE_ENDIAN = 0x01
    ENDIANNESS = BIG_ENDIAN if sys.byteorder == "big" else LITTLE_ENDIAN
    
    @staticmethod
    def checkLength(data: bytes, expect: int):
        length = len(data)
        assert (length == expect), 'Expected ' + str(expect) + 'bytes, got ' + str(length)
        
    @staticmethod
    def signByte(value: int):
        if calcsize('P') == 8:
            return value << 56 >> 56
        else:
            return value << 24 >> 24
        
    @staticmethod
    def unsignByte(value: int):
        return value & 0xff
        
    @staticmethod
    def signShort(value: int):
        if calcsize('P') == 8:
            return value << 48 >> 48
        else:
            return value << 16 >> 16

    @staticmethod
    def unsignShort(value: int):
        return value & 0xffff
    
    @staticmethod
    def signInt(value: int):
        if calcsize('P') == 8:
            return value << 32 >> 32
        else:
            return value

    @staticmethod
    def unsignInt(value: int):
        return value & 0xffffffff
    
    @staticmethod
    def readTriad(data: bytes) -> int:
        Binary.checkLength(data, 3)
        return unpack('>L', b'\x00' + data)[0]
    
    @staticmethod
    def writeTriad(value: int) -> bytes:
        return pack('>L', value)[1:]
    
    @staticmethod
    def readLTriad(data: bytes) -> int:
        Binary.checkLength(data, 3)
        return unpack('<L', data + b'\x00')[0]

    @staticmethod
    def writeLTriad(value: int) -> bytes:
        return pack('<L', value)[0:-1]
    
    @staticmethod
    def readBool(data: bytes) -> bool:
        return unpack('?', data)[0]

    @staticmethod
    def writeBool(value: bool) -> bytes:
        return b'\x01' if value else b'\x00'
    
    @staticmethod
    def readByte(data: bytes) -> int:
        Binary.checkLength(data, 1)
        return ord(data)
    
    @staticmethod
    def readSignedByte(data: bytes) -> int:
        Binary.checkLength(data, 1)
        return Binary.signByte(Binary.readByte(data))

    @staticmethod
    def writeByte(value: int) -> bytes:
        return chr(value).encode()

    @staticmethod
    def writeSignedByte(value: int) -> bytes:
        return chr(Binary.signByte(value)).encode()
    
    @staticmethod
    def readShort(data: bytes) -> int:
        Binary.checkLength(data, 2)
        return unpack('>H', data)[0]
    
    @staticmethod
    def readSignedShort(data: bytes) -> int:
        Binary.checkLength(data, 2)
        return Binary.signShort(Binary.readShort(data))

    @staticmethod
    def writeShort(value: int) -> bytes:
        return pack('>H', value)
    
    @staticmethod
    def readLShort(data: bytes) -> int:
        Binary.checkLength(data, 2)
        return unpack('<H', data)[0]
    
    @staticmethod
    def readSignedLShort(data: bytes) -> int:
        Binary.checkLength(data, 2)
        return Binary.signShort(Binary.readLShort(data))

    @staticmethod
    def writeLShort(value: int) -> bytes:
        return pack('<H', value)
    
    @staticmethod
    def readInt(data: bytes) -> int:
        Binary.checkLength(data, 4)
        return unpack('>L', data)[0]

    @staticmethod
    def writeInt(value: int) -> bytes:
        return pack('>L', value)

    @staticmethod
    def readLInt(data: bytes) -> int:
        Binary.checkLength(data, 4)
        return unpack('<L', data)[0]

    @staticmethod
    def writeLInt(value: int) -> bytes:
        return pack('<L', value)
    
    @staticmethod
    def readFloat(data: bytes) -> int:
        Binary.checkLength(data, 4)
        return unpack('>f', data)[0]
    
    @staticmethod
    def readRoundedFloat(data, accuracy):
        return round(Binary.readFloat(data), accuracy)

    @staticmethod
    def writeFloat(value: int) -> bytes:
        return pack('>f', value)

    @staticmethod
    def readLFloat(data: bytes) -> int:
        Binary.checkLength(data, 4)
        return unpack('<f', data)[0]
    
    @staticmethod
    def readRoundedLFloat(data, accuracy):
        return round(Binary.readLFloat(data), accuracy)

    @staticmethod
    def writeLFloat(value: int) -> bytes:
        return pack('<f', value)
    
    @staticmethod
    def printFloat(value):
        return match(r"/(\\.\\d+?)0+$/", "" + value).group(1)
    
    @staticmethod
    def readDouble(data: bytes) -> int:
        Binary.checkLength(data, 8)
        return unpack('>d', data)[0]

    @staticmethod
    def writeDouble(value: int) -> bytes:
        return pack('>d', value)

    @staticmethod
    def readLDouble(data: bytes) -> int:
        Binary.checkLength(data, 8)
        return unpack('<d', data)[0]

    @staticmethod
    def writeLDouble(value: int) -> bytes:
        return pack('<d', value)
    
    @staticmethod
    def readLong(data: bytes) -> int:
        Binary.checkLength(data, 8)
        return unpack('>Q', data)[0]
    
    @staticmethod
    def writeLong(value: int) -> bytes:
        return pack('>Q', value)

    @staticmethod
    def readLLong(data: bytes) -> int:
        Binary.checkLength(data, 8)
        return unpack('<Q', data)[0]

    @staticmethod
    def writeLLong(value: int) -> bytes:
        return pack('<Q', value)
    
    @staticmethod
    def readUnsignedVarInt(buffer: bytes, offset: int) -> int:
        if isinstance(buffer, bytes):
            buffer = buffer.decode()
        value = 0
        i = 0
        while i <= 28:
            try:
                buffer[offset]
            except:
                raise Exception('No bytes left in buffer')
            b = ord(buffer[offset])
            offset += 1
            value |= ((b & 0x7f) << i)
            i += 7
            if (b & 0x80) == 0:
                return value
        raise Exception('VarInt did not terminate after 5 bytes!')
        
    @staticmethod
    def readVarInt(buffer: bytes, offset: int) -> int:
        raw = Binary.readUnsignedVarInt(buffer, offset)
        temp = int(raw / 2)
        if raw % 2 == 1:
            temp = temp * -1 - 1
        return temp
    
    @staticmethod
    def writeUnsignedVarInt(value: int) -> bytes:
        buf = ""
        value = value & 0xffffffff
        i = 0
        while i < 5:
            i = i + 1
            if (value >> 7) != 0:
                buf += chr(value | 0x80)
            else:
                buf += chr(value & 0x7f)
                return buf.encode()
            value = ((value >> 7) & (sys.maxsize >> 6))
        raise Exception('Value too large to be encoded as a VarInt')
        
    @staticmethod
    def writeVarInt(value: int) -> bytes:
        value = Binary.signInt(value)
        return Binary.writeUnsignedVarInt((value << 1) ^ (value >> 31))
        
    @staticmethod
    def readUnsignedVarLong(buffer: bytes, offset: int) -> int:
        if isinstance(buffer, bytes):
            buffer = buffer.decode()
        value = 0
        i = 0
        while i <= 63:
            try:
                buffer[offset]
            except:
                raise Exception('No bytes left in buffer')
            b = ord(buffer[offset])
            offset += 1
            value |= ((b & 0x7f) << i)
            i += 7
            if (b & 0x80) == 0:
                return value
        raise Exception('VarInt did not terminate after 10 bytes!')
        
    @staticmethod
    def readVarLong(buffer: bytes, offset: int) -> int:
        raw = Binary.readUnsignedVarLong(buffer, offset)
        temp = int(raw / 2)
        if raw % 2 == 1:
            temp = temp * -1 - 1
        return temp
    
    @staticmethod
    def writeUnsignedVarLong(value: int) -> bytes:
        buf = ""
        i = 0
        while i < 10:
            i = i + 1
            if (value >> 7) != 0:
                buf += chr(value | 0x80)
            else:
                buf += chr(value & 0x7f)
                return buf.encode()
            value = ((value >> 7) & (sys.maxsize >> 6))
        raise Exception('Value too large to be encoded as a VarLong')
        
    @staticmethod
    def writeVarLong(value: int) -> bytes:
        return Binary.writeUnsignedVarLong((value << 1) ^ (value >> 63))
    
    @staticmethod
    def flipShortEndianness(value: int) -> int:
        return Binary.readLShort(Binary.writeShort(value))

    @staticmethod
    def flipIntEndianness(value: int) -> int:
        return Binary.readLInt(Binary.writeInt(value))

    @staticmethod
    def flipLongEndianness(value: int) -> int:
        return Binary.readLLong(Binary.writeLong(value))
