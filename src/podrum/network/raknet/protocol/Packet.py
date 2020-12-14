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

class Packet:
    id = None
    sendTime = None
    
    def decodeHeader(self):
        self.getByte()
        
    def decodePayload(self):
        pass
        
    def decode(self):
        self.decodeHeader()
        self.decodePayload()
        
    def encodeHeader(self):
        self.putByte(self.id)
        
    def encodePayload(self):
        pass
        
    def encode(self):
        self.encodeHeader()
        self.encodePayload()
        
    def getString(self):
        return self.get(self.getShort()).decode()
        
    def putString(self, value):
        self.putShort(len(value))
        self.put(value.encode())
