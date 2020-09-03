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
        
    def getTokenString(self, token: bytes, salt: bytes):
        hash = hashlib.new("sha512").update(salt + bytes(":", "utf-8") + token).digest()
        return Binary.readInt(Utils.substr(hash, 7, 4))
