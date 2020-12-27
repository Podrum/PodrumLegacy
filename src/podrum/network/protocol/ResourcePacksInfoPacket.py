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

class ResourcePacksInfoPacket(DataPacket):
    NID = ProtocolInfo.RESOURCE_PACKS_INFO_PACKET

    mustAccept = False
    hasScripts = False
    behaviorPackEntries = []
    resourcePackEntries = []

    def decodePayload(self):
        self.mustAccept = self.getBool()
        self.hasScripts = self.getBool()
        behaviorPackCount = self.getLShort()
        while behaviorPackCount > 0:
            self.getString()
            self.getString()
            self.getLLong()
            self.getString()
            self.getString()
            self.getString()
            self.getBool()
            behaviorPackCount -= 1

        resourcePackCount = self.getLShort()
        while resourcePackCount > 0:
            self.getString()
            self.getString()
            self.getLLong()
            self.getString()
            self.getString()
            self.getString()
            self.getBool()
            resourcePackCount -= 1

    def encodePayload(self):
        self.putBool(self.mustAccept)
        self.putBool(self.hasScripts)
        self.putLShort(len(self.behaviorPackEntries))
        for entry in self.behaviorPackEntries:
            self.putString(entry.getPackId())
            self.putString(entry.getPackVersion())
            self.putLLong(entry.getPackSize())
            self.putString("")
            self.putString("")
            self.putString("")
            self.putBool(False)

        self.putLShort(len(self.resourcePackEntries))
        for entry in self.resourcePackEntries:
            self.putString(entry.getPackId())
            self.putString(entry.getPackVersion())
            self.putLLong(entry.getPackSize())
            self.putString("")
            self.putString("")
            self.putString("")
            self.putBool(False)
