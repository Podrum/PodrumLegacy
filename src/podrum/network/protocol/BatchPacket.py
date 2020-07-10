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

import zlib

from podrum.network.PacketPool import PacketPool
from podrum.network.protocol.DataPacket import DataPacket
from podrum.network.protocol.ProtocolInfo import ProtocolInfo

class BatchPacket(DataPacket):
    NID = ProtocolInfo.BATCH_PACKET
    
    payload = ""
    compressionLevel = 7
    
    def canBeBatched():
        return False
    
    def canBeSentBeforeLogin():
        return True
    
    def decodeHeader(self):
        pid = self.getByte()
        assert pid == self.NID
        
    def decodePayload(self):
        data = self.getRemaining()
        try:
            self.payload = zlib.decompress(data, 1024 * 1024 * 2)
        except:
            self.payload = ""
            
    def encodeHeader(self):
        self.putByte(self.NID)
    
    def encodePayload(self):
        compress = zlib.compressobj(self.compressionLevel, zlib.DEFLATED, -zlib.MAX_WBITS)
        compressedData = compress.compress(self.payload)
        compressedData += compress.flush()
        self.put(compressedData)
        
    def addPacket(packet: DataPacket):
        if not packet.canBeBatched():
            raise Exception(str(type(packet).__name__) + " cannot be put inside a BatchPacket")
        if not packet.isEncoded:
            packet.encode()
        self.payload += Binary.writeUnsignedVarInt(len(packet.buffer)) + packet.buffer
        
    def getPackets(self):
        stream = DataPacket.BinaryStream(self.payload)
        count = 0
        while not stream.feof():
            count += 1
            if count >= 500:
                raise Exception("Too many packets in a single batch")
            yield stream.getString()
            
    def getCompressionLevel(self):
        return self.compressionLevel
    
    def setCompressionLevel(self, level: int):
        self.compressionLevel = level
