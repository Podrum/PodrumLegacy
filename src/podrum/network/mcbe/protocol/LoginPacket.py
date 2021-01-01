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
from podrum.network.mcbe.protocol.DataPacket import DataPacket
from podrum.network.mcbe.protocol.Info import Info
from podrum.utils.Utils import Utils

class LoginPacket(DataPacket):
    networkId = Info.LOGIN_PACKET

    xuid = None
    identity = None
    displayName = None
    protocol = None
    identityPublicKey = None
    clientRandomId = None
    deviceOS = None
    deviceId = None
    deviceModel = None
    skin = None

    def decodePayload(self):
        self.protocol = self.getInt()
        print(self.protocol)
