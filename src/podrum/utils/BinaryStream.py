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

from podrum.utils.Binary import Binary

class BinaryStream:
    offset = None
    buffer = None
    
    def __init__(self, buffer: str = "", offset: int = 0):
        self.offset = offset
        self.buffer = buffer
        
    def reset(self):
        self.buffer = ""
        self.offset = 0
        
    def rewind(self):
        self.offset = 0
        
    def setOffset(self, offset: int):
        self.offset = offset
        
    def setBuffer(self, buffer: str = "", offset: int = 0):
        self.buffer = buffer
        self.offset = offset
        
    def getOffset(self) -> int:
        return self.offset
        
    def getBuffer(self) -> str:
        return self.buffer
        
    def get(self, length) -> str:
        if length == 0:
            return ""
        buflength = len(self.buffer)
        if length == True:
            s = self.buffer[self.offset:]
            self.offset = buflength
            return s
        if length < 0:
            self.offset = buflength - 1
            return ""
        remaining = buflen - self.offset
        if remaining < length:
            raise Exception("Not enough bytes left in buffer: need " + str(length) + ", have " + str(remaining))
        if length == 1:
            b = self.buffer[self.offset]
            self.offset += 1
            return b
        else:
            start = self.offset - length
            self.offset += length
            if start < 0:
                 start = start + len(self.buffer)
            return self.buffer[start:start + length]
        
    def getRemaining(self) -> str:
        s = self.buffer[self.offset:]
        if s == False:
            raise Exception("No bytes left to read")
        self.offset = len(self.buffer)
        return s
    
    def put(self, s):
        self.buffer += s
        
    def getBool(self):
        return Binary.readBool(self.get(1))
        
    def putBool(self, value):
        self.buffer += Binary.writeBool(value)
        
    def getByte(self):
        return Binary.readByte(self.get(1))
    
    def putByte(self, value):
        self.buffer += Binary.writeByte(value)
        
    def getTriad(self):
        return Binary.readTriad(self.get(3))
    
    def putTriad(self, value):
        self.buffer += Binary.writeTriad(value)
        
    def getLTriad(self):
        return Binary.readLTriad(self.get(3))
    
    def putLTriad(self, value):
        self.buffer += Binary.writeLTriad(value)
        
    def getShort(self):
        return Binary.readShort(self.get(2))
    
    def putShort(self, value):
        self.buffer += Binary.writeShort(value)
        
    def getSignedShort(self):
        return Binary.readSignedShort(self.get(2))
        
    def getLShort(self):
        return Binary.readLShort(self.get(2))
    
    def getSignedLShort(self):
        return Binary.readSignedLShort(self.get(4))
    
    def putLShort(self, value):
        self.buffer += Binary.writeLShort(value)
        
    def getInt(self):
        return Binary.readInt(self.get(4))
    
    def putInt(self, value):
        self.buffer += Binary.writeInt(value)
        
    def getLInt(self):
        return Binary.readLInt(self.get(4))
    
    def putLInt(self, value):
        self.buffer += Binary.writeLInt(value)
        
    def getFloat(self):
        return Binary.readFloat(self.get(4))
    
    def getRoundedFloat(self, accuracy):
        return Binary.readRoundedFloat(self.get(4), accuracy)
    
    def putFloat(self, value):
        self.buffer += Binary.writeFloat(value)
        
    def getLFloat(self):
        return Binary.readLFloat(self.get(4))
    
    def getRoundedLFloat(self, accuracy):
        return Binary.readRoundedLFloat(self.get(4), accuracy)
    
    def putLFloat(self, value):
        self.buffer += Binary.writeLFloat(value)
        
    def getDouble(self):
        return Binary.readDouble(self.get(8))
    
    def putDouble(self, value):
        self.buffer += Binary.writeDouble(value)
        
    def getLDouble(self):
        return Binary.readLDouble(self.get(8))
    
    def putLDouble(self, value):
        self.buffer += Binary.writeLDouble(value)
        
    def getLong(self):
        return Binary.readLong(self.get(8))
    
    def putLong(self, value):
        self.buffer += Binary.writeLong(value)
        
    def getLLong(self):
        return Binary.readLLong(self.get(8))
    
    def putLLong(self, value):
        self.buffer += Binary.writeLLong(value)
        
    def getUnsignedVarInt(self):
        return Binary.readUnsignedVarInt(self.buffer, self.offset)
    
    def putUnsignedVarInt(self, value):
        self.put(Binary.writeUnsignedVarInt(value))
        
    def getVarInt(self):
        return Binary.readVarInt(self.buffer, self.offset)
    
    def putVarInt(self, value):
        self.put(Binary.writeVarInt(value))
        
    def getUnsignedVarLong(self):
        return Binary.readUnsignedVarLong(self.buffer, self.offset)
    
    def putUnsignedVarLong(self, value):
        self.put(Binary.writeUnsignedVarLong(value))
        
    def getVarLong(self):
        return Binary.readVarLong(self.buffer, self.offset)
    
    def putVarLong(self, value):
        self.put(Binary.writeVarLong(value))
        
    def feof(self):
        try:
            self.buffer[self.offset]
            return True
        except:
            return False
