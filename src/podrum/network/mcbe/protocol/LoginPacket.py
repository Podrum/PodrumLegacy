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

import base64
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
    deviceId = None
    deviceOS = None
    deviceModel = None
    clientRandomId = None
    serverAddress = None
    languageCode = None
    skin = None

    def skinFromDecodedJwt(self, decodedJwt):
        return {
            "SkinId": decodedJwt["SkinId"],
            "SkinResourcePatch": decodedJwt["SkinResourcePatch"],
            "SkinImageWidth": decodedJwt["SkinImageWidth"],
            "SkinImageHeight": decodedJwt["SkinImageHeight"],
            "SkinData": base64.b64decode(decodedJwt["SkinData"]),
            "AnimatedImageData": decodedJwt["AnimatedImageData"],
            "CapeImageWidth": decodedJwt["CapeImageWidth"],
            "CapeImageHeight": decodedJwt["CapeImageHeight"],
            "CapeData": base64.b64decode(decodedJwt["CapeData"]),
            "SkinGeometryData": base64.b64decode(decodedJwt["SkinGeometryData"]),
            "SkinAnimationData": base64.b64decode(decodedJwt["SkinAnimationData"]),
            "PremiumSkin": decodedJwt["PremiumSkin"],
            "PersonaSkin": decodedJwt["PersonaSkin"],
            "CapeOnClassicSkin": decodedJwt["CapeOnClassicSkin"],
            "CapeId": decodedJwt["CapeId"],
            "SkinColor": decodedJwt["SkinColor"],
            "ArmSize": decodedJwt["ArmSize"],
            "PersonaPieces": decodedJwt["PersonaPieces"],
            "PieceTintColors": decodedJwt["PieceTintColors"]
        }

    def decodePayload(self):
        self.protocol = self.getInt()
        stream = NetworkStream(self.getBytesString())
        chainData = json.loads(stream.get(stream.getLInt()).decode())
        for chain in chainData["chain"]:
            decodedChain = Utils.decodeJwt(chain)
            if "extraData" in decodedChain:
                extraData = decodedChain["extraData"]
                self.xuid = extraData["XUID"]
                self.identity = extraData["identity"]
                self.displayName = extraData["displayName"]
            self.identityPublicKey = decodedChain["identityPublicKey"]
        decodedJwt = Utils.decodeJwt(stream.get(stream.getLInt()).decode())
        self.deviceId = decodedJwt["DeviceId"]
        self.deviceOs = decodedJwt["DeviceOS"]
        self.deviceModel = decodedJwt["DeviceModel"]
        self.clientRandomId = decodedJwt["ClientRandomId"]
        self.serverAddress = decodedJwt["ServerAddress"]
        self.languageCode = decodedJwt["LanguageCode"]
        self.skin = self.skinFromDecodedJwt(decodedJwt)
