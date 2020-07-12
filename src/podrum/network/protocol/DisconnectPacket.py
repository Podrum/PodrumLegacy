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

class DisconnectPacket(DataPacket):
    NID = ProtocolInfo.DISCONNECT_PACKET

    hideDisconnectionScreen = False
    message = ""

    def canBeSentBeforeLogin():
        return True

    def decodePayload(self):
        self.hideDisconnectionScreen = self.getBool()
        if not self.hideDisconnectionScreen:
            self.message = self.getString()

    def encodePayload(self):
        self.putBool(self.hideDisconnectionScreen)
        if not self.hideDisconnectionScreen:
            self.putString(self.message)
