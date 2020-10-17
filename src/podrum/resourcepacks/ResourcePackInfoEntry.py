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
