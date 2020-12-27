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
        # T O D O #
                
    def encodePayload(self): 
        pass
    
