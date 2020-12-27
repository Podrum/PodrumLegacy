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

import json

from podrum.network.protocol.DataPacket import DataPacket
from podrum.network.protocol.ProtocolInfo import ProtocolInfo
from podrum.utils.Utils import Utils

class LoginPacket(DataPacket):
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
    
    def canBeSentBeforeLogin(self):
        return True
        
    def mayHaveUnreadBytes(self):
        return self.protocol is not None and self.protocol != ProtocolInfo.MCBE_PROTOCOL_VERSION
        
    def decodePayload(self):
        self.protocol = self.getInt()
        try:
            buffer = DataPacket.NetBinaryStream(self.getString())
            self.chainData = json.loads(buffer.get(buffer.getLInt()))
            hasExtraData = False
            for chain in self.chainData["chain"]:
                webtoken = Utils.decodeJWT(chain)
                if webtoken["extraData"] in locals() or webtoken["extraData"] in globals():
                    if hasExtraData:
                        raise Exception("Found 'extraData' multiple times in key chain")
                    hasExtraData = True
                    if webtoken["extraData"]["displayName"] in locals() or webtoken["extraData"]["displayName"] in globals():
                        self.username = webtoken["extraData"]["displayName"]
                    if webtoken["extraData"]["identity"] in locals() or webtoken["extraData"]["identity"] in globals():
                        self.clientUUID = webtoken["extraData"]["identity"]
                    if webtoken["extraData"]["XUID"] in locals() or webtoken["extraData"]["XUID"] in globals():
                        self.xuid = webtoken["extraData"]["XUID"]
                if webtoken["identityPublicKey"] in locals() or webtoken["identityPublicKey"] in globals():
                    self.identityPublicKey = webtoken["identityPublicKey"]
            self.clientDataJwt = buffer.get(buffer.getLInt())
            self.clientData = Utils.decodeJWT(self.clientDataJwt)
            self.clientId = self.clientData["ClientRandomId"] if self.clientData["ClientRandomId"] != None else None
            self.serverAddress = self.clientData["ServerAddress"] if self.clientData["ServerAddress"] != None else None
            self.locale = self.clientData["LanguageCode"] if self.clientData["LanguageCode"] != None else None
        except Exception as e:
            if self.protocol == ProtocolInfo.MCBE_PROTOCOL_VERSION:
                raise Exception(f"Error: {str(e)}")
                
    def encodePayload(self): 
        pass
    
