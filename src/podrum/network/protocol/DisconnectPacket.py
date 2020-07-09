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
