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

import hashlib
import os
import random
import time

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
    
    def equals(self, uuid):
        return uuid.parts[0] == self.parts[0] and uuid.parts[1] == self.parts[1] and uuid.parts[2] == self.parts[2] and uuid.parts[3] == self.parts[3]
    
    def fromBinary(self, uuid, version = None):
        if len(uuid) != 16:
            raise Exception("Must have exactly 16 bytes")
        return UUID(Binary.readInt(Utils.substr(uuid, 0, 4)), Binary.readInt(Utils.substr(uuid, 4, 4)), Binary.readInt(Utils.substr(uuid, 8, 4)), Binary.readInt(Utils.substr(uuid, 12, 4)), version)

    def fromString(self, uuid, version = None):
        return self.fromBinary(Utils.hex2bin(uuid.strip().replace("-", "")), version)
    
    def fromData(self, data):
        hash = hashlib.new("md5").update("".join(data))
        return self.fromBinary(hash, 3)

    def fromRandom(self):
        return self.fromData(Binary.writeInt(int(time.time())), Binary.writeShort(os.getpid()), Binary.writeShort(os.geteuid()), Binary.writeInt(random.randint(-0x7fffffff, 0x7fffffff)), Binary.writeInt(random.randint(-0x7fffffff, 0x7fffffff)))
    
    def toBinary(self):
        return Binary.writeInt(self.parts[0]) + Binary.writeInt(self.parts[1]) + Binary.writeInt(self.parts[2]) + Binary.writeInt(self.parts[3])
    
    def toString(self):
        hex = Utils.bin2hex(self.toBinary())
        if self.version != None:
            return Utils.substr(hex, 0, 8) + "-" + Utils.substr(hex, 8, 4) + "-" + int(self.version, 16) + Utils.substr(hex, 13, 3) + "-8" + Utils.substr(hex, 17, 3) + "-" + Utils.substr(hex, 20, 12)
        return Utils.substr(hex, 0, 8) + "-" + Utils.substr(hex, 8, 4) + "-" + Utils.substr(hex, 12, 4) + "-" + Utils.substr(hex, 16, 4) + "-" + Utils.substr(hex, 20, 12)
    
    def getPart(self, partNumber: int):
        if partNumber < 0 or partNumber > 3:
            raise Exception("Invalid UUID part index" + str(partNumber))
        return self.parts[partNumber]
