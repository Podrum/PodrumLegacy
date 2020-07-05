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

class PlayStatusPacket(DataPacket):
    NID = ProtocolInfo.PLAY_STATUS_PACKET

    LOGIN_SUCCESS = 0
    LOGIN_FAILED_CLIENT = 1
    LOGIN_FAILED_SERVER = 2
    PLAYER_SPAWN = 3
    LOGIN_FAILED_INVALID_TENANT = 4
    LOGIN_FAILED_VANILLA_EDU = 5
    LOGIN_FAILED_EDU_VANILLA = 6
    LOGIN_FAILED_SERVER_FULL = 7

    status = None

    def decodePayload(self):
        self.status = self.getInt()

    def canBeSentBeforeLogin():
        return True

    def encodePayload(self):
        self.putInt(self.status)
