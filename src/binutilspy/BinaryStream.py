"""
*
*  __  __ _____ ____   ____                 _             
* |  \/  |  ___|  _ \ / ___| __ _ _ __ ___ (_)_ __   __ _ 
* | |\/| | |_  | | | | |  _ / _` | '_ ` _ \| | '_ \ / _` |
* | |  | |  _| | |_| | |_| | (_| | | | | | | | | | | (_| |
* |_|  |_|_|   |____/ \____|\__,_|_| |_| |_|_|_| |_|\__, |
*                                                    |___/ 
*
* Licensed under the Apache License, Version 2.0 (the "License")
* you may not use this file except in compliance with the License.
* You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
"""

from binutilspy.Binary import Binary

class BinaryStream:
    offset = 0
    buffer = b""
    
    def __init__(self, buffer: bytes = b"", offset: int = 0):
        self.offset = offset
        self.buffer = buffer
       
    def reset(self):
        self.buffer = b""
        self.offset = 0
       
    def rewind(self):
        self.offset = 0
       
    def setOffset(self, offset: int):
        self.offset = offset
      
    def setBuffer(self, buffer: bytes = b"", offset: int = 0):
        self.buffer = buffer
        self.offset = offset
        
    def getOffset(self) -> int:
        return self.offset
      
    def getBuffer(self) -> bytes:
        return self.buffer
       
    def get(self, length) -> bytes:
        buffer = self.getBuffer()[self.offset:self.offset + length]
        self.offset += length
        return buffer
       
    def getRemaining(self) -> str:
        s = self.buffer[self.offset:]
        if s == False:
            raise Exception("No bytes left to read")
        self.offset = len(self.buffer)
        return s
    
    def put(self, data: bytes):
        self.buffer += data
      
    def getBool(self):
        return Binary.readBool(self.get(1))
     
    def putBool(self, value):
        self.put(Binary.writeBool(value))
      
    def getByte(self):
        return Binary.readByte(self.get(1))
    
    def getSignedByte(self):
        return Binary.readSignedByte(self.get(1))
    
    def putByte(self, value):
        self.put(Binary.writeByte(value))
      
    def getTriad(self):
        return Binary.readTriad(self.get(3))
    
    def putTriad(self, value):
        self.put(Binary.writeTriad(value))
    
    def getLTriad(self):
        return Binary.readLTriad(self.get(3))
    
    def putLTriad(self, value):
        self.put(Binary.writeLTriad(value))
    
    def getShort(self):
        return Binary.readShort(self.get(2))
    
    def putShort(self, value):
        self.put(Binary.writeShort(value))
       
    def getSignedShort(self):
        return Binary.readSignedShort(self.get(2))
     
    def getLShort(self):
        return Binary.readLShort(self.get(2))
    
    def getSignedLShort(self):
        return Binary.readSignedLShort(self.get(4))
    
    def putLShort(self, value):
        self.put(Binary.writeLShort(value))
      
    def getInt(self):
        return Binary.readInt(self.get(4))
    
    def putInt(self, value):
        self.put(Binary.writeInt(value))
       
    def getLInt(self):
        return Binary.readLInt(self.get(4))
    
    def putLInt(self, value):
        self.put(Binary.writeLInt(value))
       
    def getFloat(self):
        return Binary.readFloat(self.get(4))
    
    def getRoundedFloat(self, accuracy):
        return Binary.readRoundedFloat(self.get(4), accuracy)
    
    def putFloat(self, value):
        self.put(Binary.writeFloat(value))
       
    def getLFloat(self):
        return Binary.readLFloat(self.get(4))
    
    def getRoundedLFloat(self, accuracy):
        return Binary.readRoundedLFloat(self.get(4), accuracy)
    
    def putLFloat(self, value):
        self.put(Binary.writeLFloat(value))
    
    def getDouble(self):
        return Binary.readDouble(self.get(8))
    
    def putDouble(self, value):
        self.put(Binary.writeDouble(value))
       
    def getLDouble(self):
        return Binary.readLDouble(self.get(8))
    
    def putLDouble(self, value):
        self.put(Binary.writeLDouble(value))
     
    def getLong(self):
        return Binary.readLong(self.get(8))
    
    def putLong(self, value):
        self.put(Binary.writeLong(value))
     
    def getLLong(self):
        return Binary.readLLong(self.get(8))
    
    def putLLong(self, value):
        self.put(Binary.writeLLong(value))
     
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
        self.offset < 0 or self.offset >= len(self.buffer)
        
