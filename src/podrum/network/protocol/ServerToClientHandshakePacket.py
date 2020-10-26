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

from podrum.network.protocol.DataPacket import DataPacket
from podrum.network.protocol.ProtocolInfo import ProtocolInfo

class ServerToClientHandshakePacket(DataPacket):
    NID = ProtocolInfo.SERVER_TO_CLIENT_HANDSHAKE_PACKET

    jwt = None

    def canBeSentBeforeLogin():
        return True

    def decodePayload(self):
        self.jwt = self.getString()

    def encodePayload(self):
        self.putString(self.jwt)
