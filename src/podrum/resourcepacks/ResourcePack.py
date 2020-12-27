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

class ResourcePack:
    def getPath(self):
        pass

    def getPackName(self):
        pass

    def getPackId(self):
        pass

    def getPackSize(self):
        pass

    def getPackVersion(self):
        pass

    def getSha256(self):
        pass

    def getPackChunk(self, start, length):
        pass
