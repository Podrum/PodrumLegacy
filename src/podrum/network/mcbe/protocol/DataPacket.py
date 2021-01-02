"""
*  ____           _
* |  _ \ ___   __| |_ __ _   _ _ __ ___
* | |_) / _ \ / _` | '__| | | | '_ ` _ \
* |  __/ (_) | (_| | |  | |_| | | | | | |
* |_|   \___/ \__,_|_|   \__,_|_| |_| |_|
*
* Licensed under the Mozilla Public License, Version 2.
* Permissions of this weak copyleft license are conditioned on making
* available source code of licensed files and modifications of those files 
* under the same license (or in certain cases, one of the GNU licenses).
* Copyright and license notices must be preserved. Contributors
* provide an express grant of patent rights. However, a larger work
* using the licensed work may be distributed under different terms and without 
* source code for files added in the larger work.
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