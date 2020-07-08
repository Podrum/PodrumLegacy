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

class ResourcePackInfoEntry:
    packId = None # UUID
    version = None
    packSize = None

    def __init__(self, packId, version, packSize = 0):
        self.packId = packId
        self.version = version
        self.packSize = packSize

    def getPackId(self):
        return self.packId

    def getVersion(self):
        return self.version

    def getPackSize(self):
        return self.packSize
