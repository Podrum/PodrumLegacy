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
