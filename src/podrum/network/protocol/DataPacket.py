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

from podrum.network.NetBinaryStream import NetBinaryStream

class DataPacket(NetBinaryStream):
    NID = 0
    PID_MASK = 0x3ff # 10 Bits
    
    SUBCLIENT_ID_MASK = 0x03 # 2 Bits
    SENDER_SUBCLIENT_ID_SHIFT = 10
    RECIPIENT_SUBCLIENT_ID_SHIFT = 12
    
    isEncoded = False
    _encapsulatedPacket = None
    
    senderSubId = 0
    recipientSubId = 0
    
    def pid(self):
        return self.NID
        
    def getName(self):
        return type(object).__name__
        
    def canBeBatched(self):
        return True
        
    def canBeSentBeforeLogin(self):
        return False
        
    def mayHaveUnreadBytes(self):
        return False
        
    def decodePayload(self): 
        pass
        
    def decode(self):
        self.offset = 0
        self.decodeHeader()
        self.decodePayload()
        
    def decodeHeader(self):
        header = self.getUnsignedVarInt()
        pid = header & self.PID_MASK
        if pid != self.NID:
            raise Exception(f"Expected {self.NID} for packet ID, got " + pid)
        self.senderSubId = (header >> self.SENDER_SUBCLIENT_ID_SHIFT) & self.SUBCLIENT_ID_MASK
        self.recipientSubId = (header >> self.RECIPIENT_SUBCLIENT_ID_SHIFT) & self.SUBCLIENT_ID_MASK;
    
    def encodePayload(self): pass
    
    def encode(self):
        self.reset()
        self.encodeHeader()
        self.encodePayload()
        self.isEncoded = True
        
    def encodeHeader(self):
        self.putUnsignedVarInt(
            self.NID |
            (self.senderSubId << self.SENDER_SUBCLIENT_ID_SHIFT) |
            (self.recipientSubId << self.RECIPIENT_SUBCLIENT_ID_SHIFT)
        )
        
    def writePayload(self): pass
    
    def clean(self):
        self.buffer = ""
        self.isEncoded = False
        self.offset = 0
        return self
