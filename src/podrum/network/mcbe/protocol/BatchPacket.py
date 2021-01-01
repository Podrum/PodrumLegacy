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

from podrum.network.mcbe.NetworkStream import NetworkStream
from podrum.network.mcbe.protocol.DataPacket import DataPacket
from podrum.network.mcbe.protocol.Info import Info
import zlib

class BatchPacket(DataPacket):
    networkId = Info.BATCH_PACKET
    payload = b""
    compressionLevel = 7
    allowBatching = False
    allowBeforeLogin = True

    def decodeHeader(self):
        pid = self.getByte()
        if pid != self.networkId:
            raise Exception("Batch idi5 missmatched")

    def decodePayload(self):
        try:
            self.payload = zlib.decompress(self.getRemaining(), -zlib.MAX_WBITS, 1024 * 1024 * 8)
        except Exception as e:
            print(e)
            self.payload = b""

    def encodeHeader(self):
        self.putByte(self.networkId)

    def encodePayload(self):
        compress = zlib.compressobj(self.compressionLevel, zlib.DEFLATED, -zlib.MAX_WBITS)
        compressedData = compress.compress(self.payload)
        compressedData += compress.flush()
        self.put(compressedData)

    def addPacket(self, packet):
        if not packet.encoded:
            packet.encode()
        stream = NetworkStream()
        stream.putBytesString(packet.buffer)
        self.payload += stream.buffer

    def getPackets(self):
        stream = NetworkStream(self.payload)
        packets = []
        count = 0
        while not stream.feof():
            if count >= 500:
                raise Exception("Too many packets in a batch packet")
            count += 1
            packets.append(stream.getBytesString())
        return packets