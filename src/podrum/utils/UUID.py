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

from podrum.utils.Binary import Binary
from podrum.utils.Utils import Utils

class UUID:
    parts = [0, 0, 0, 0]
    version = None
    
    def __init__(self, part1 = 0, part2 = 0, part3 = 0, part4 = 0, version = None):
        self.parts[0] = int(part1)
        self.parts[1] = int(part2)
        self.parts[2] = int(part3)
        self.parts[3] = int(part4)
        self.version = (self.parts[1] & 0xf000) >> 12 if version == None else int(version)
        
    def getVersion(self):
        return self.version
    
    def equals(self, uuid: UUID):
        return uuid.parts[0] == self.parts[0] and uuid.parts[1] == self.parts[1] and uuid.parts[2] == self.parts[2] and uuid.parts[3] == self.parts[3]
    
    def fromBinary(self, uuid, version = None):
        if len(uuid) != 16:
            raise Exeption("Must have exactly 16 bytes")
        return UUID(Binary.readInt(Utils.substr(uuid, 0, 4)), Binary.readInt(Utils.substr(uuid, 4, 4)), Binary.readInt(Utils.substr(uuid, 8, 4)), Binary.readInt(Utils.substr(uuid, 12, 4)), version)

    def fromString(self, uuid, version = None):
        return self.fromBinary(Utils.hex2bin(uuid.strip().replace("-", "")), version)
