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

import bin2ascii
from binutilspy.BinaryStream import BinaryStream
import os
from podrum.utils.Utils import Utils
import random
import time

class UUID:
    parts = [0, 0, 0, 0]
    version = None
    
    def __init__(self, part1 = 0, part2 = 0, part3 = 0, part4 = 0, version = None):
        self.parts = [part1, part2, part3, part4]
        self.version = version if version else ((self.parts[1] & 0xf000) >> 12)

    def fromBinary(self, uuid, version = None):
        if len(uuid) != 16:
            raise Exception("Must have exactly 16 bytes")
        stream = BinaryStream(uuid)
        return UUID(stream.getInt(), stream.getInt(), stream.getInt(), stream.getInt(), version)
    
    def toBinary(self):
        stream = BinaryStream()
        stream.putInt(self.parts[0])
        stream.putInt(self.parts[1])
        stream.putInt(self.parts[2])
        stream.putInt(self.parts[3])
        return stream.buffer

    def fromString(self, uuid, version = None):
        return self.fromBinary(bin2ascii.unhexlify(uuid.strip().replace("/-/g", "").encode()), version)

    def toString(self):
        stream = BinaryStream(bin2ascii.hexlify(self.toBinary()))
        return f"{stream.get(8).decode()}-{stream.get(4).decode()}-{stream.get(4).decode()}-{stream.get(4).decode()}-{stream.get(16).decode()}"
    
    def getPart(self, partNumber: int):
        if partNumber < 0 or partNumber > 3:
            raise Exception("Invalid UUID part index" + str(partNumber))
        return self.parts[partNumber]
