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

import hashlib
import os

from podrum import Server
from podrum.utils.Binary import Binary
from podrum.utils.Utils import Utils

class QueryHandler:
    server = None
    lastToken = None
    token = None
    longData = None
    timeout = None
    
    HANDSHAKE = 9
    STATISTICS = 0
    
    def __init__(self):
        self.server = Server.Server()
        self.server.getLogger().log("info", "Starting GS4 status listener")
        addr = self.server.getAddress() if len(self.server.getAddress().spit(".")) == 4 else "0.0.0.0"
        port = self.server.getPort()
        self.server.getLogger().log("info", f"Setting query port to {port}")
        self.regenerateToken()
        self.lastToken = self.token
        self.server.getLogger().log("info", f"Query running on {addr}:{port}")
        
    def regenerateToken(self):
        self.lastToken = self.token
        self.token = os.urandom(16)
        
    def getTokenBytes(self, token: bytes, salt: bytes):
        hash = hashlib.new("sha512").update(salt + bytes(":", "utf-8") + token).digest()
        return Binary.readInt(hash[7:7 + 4])
    
    def handle(self, address: str, port: int, packet):
        offset = 2
        packetType = packet[offset]
        offset += 1
        sessionID = Binary.readInt(packet[offset:offset + 4])
        offset += 4
        payload = packet[offset:]
        if packetType == HANDSHAKE:
            reply = bytes(chr(self.HANDSHAKE), "utf-8")
            reply += Binary.writeInt(sessionID)
            reply += self.getTokenBytes(self.token, bytes(address, "utf-8")) + b"\x00"
            self.server.sendPacket(address, port, reply)
            
