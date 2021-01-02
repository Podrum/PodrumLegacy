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

import json
from podrum.network.mcbe.NetworkStream import NetworkStream
from podrum.network.mcbe.protocol.DataPacket import DataPacket
from podrum.network.mcbe.protocol.Info import Info
from podrum.utils.Utils import Utils

class LoginPacket(DataPacket):
    networkId = Info.LOGIN_PACKET
    protocol = None
    xuid = None
    identity = None
    displayName = None
    identityPublicKey = None
    clientRandomId = None
    deviceOS = None
    deviceId = None
    deviceModel = None
    skin = None

    def decodePayload(self):
        self.protocol = self.getInt()
        stream = NetworkStream(self.getBytesString())
        chainData = json.loads(stream.get(stream.getLInt()).decode())
        for chain in chainData["chain"]:
            decodedChain = Utils.decodeJwt(chain)
            print(decodedChain)
            if "extraData" in decodedChain:
                extraData = decodedChain["extraData"]
                self.xuid = extraData["XUID"]
                self.identity = extraData["identity"]
                self.displayName = extraData["displayName"]
            self.identityPublicKey = decodedChain["identityPublicKey"]
        decodedJwt = Utils.decodeJwt(stream.get(stream.getLInt()).decode())
        print(decodedJwt)
