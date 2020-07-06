"""
*  ____           _
* |  _ \ ___   __| |_ __ _   _ _ __ ___
* | |_) / _ \ / _` | '__| | | | '_ ` _ \
* |  __/ (_) | (_| | |  | |_| | | | | | |
* |_|   \___/ \__,_|_|   \__,_|_| |_| |_|
*
* This program is free software: you can redistribute it and/or modify
* it under the terms of the GNU Lesser General Public License as published by
* the Free Software Foundation, either version 3 of the License, or
* (at your option) any later version.
"""

import json

from podrum.network.protocol.DataPacket import DataPacket
from podrum.network.protocol.ProtocolInfo import ProtocolInfo
from podrum.utils.BinaryStream import BinaryStream
from podrum.utils.Utils import Utils

class DataPacket(DataPacket):
    NID = ProtocolInfo.LOGIN_PACKET
    
    username = None
    protocol = None
    clientUUID = None
    clientId = None
    xuid = None
    identityPublicKey = None
    serverAddress = None
    locale = None
    chainData = {}
    clientDataJwt = None
    clientData = {}
    skipVerification = False
    
    def canBeSentBeforeLogin():
        return True
        
    def mayHaveUnreadBytes(self):
        return self.protocol != None and self.protocol != ProtocolInfo.MCBE_PROTOCOL_VERSION
        
    def decodePayload(self):
        self.protocol = self.getInt()
        try:
            buffer = BinaryStream(self.getString())
            self.chainData = json.loads(buffer.get(buffer.getLInt())
            hasExtraData = False
            for chain in self.chainData["chain"]:
                webtoken = Utils.decodeJWT(chain)
        
    
    def encodePayload(): pass
    
