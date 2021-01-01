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

class DataPacket(NetworkStream):
    pidMask = 0x3ff
    senderShift = 10
    receiverShift = 12
    subclientMask = 0x03

    networkId = None
    encoded = False
    senderSubId = 0
    receiverSubId = 0

    def decode(self):
        self.offset = 0
        self.decodeHeader()
        self.decodePayload()

    def decodeHeader(self):
        header = self.getUnsignedVarInt()
        pid = header & self.pidMask
        if pid != self.networkId:
            raise Exception("Packet ID must match network ID")
        self.senderSubId = (header >> self.senderShift) & self.subclientMask
        self.receiverSubId = (header >> self.receiverShift) & self.subclientMask

    def decodePayload(self):
        pass

    def encode(self):
        self.reset()
        self.encodeHeader()
        self.encodePayload()
        self.encoded = True

    def encodeHeader(self):
        self.putUnsignedVarInt(self.networkId | self.senderSubId << self.senderShift | self.receiverSubId << self.receiverShift)

    def encodePayload(self):
        pass