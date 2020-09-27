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

from binutilspy.BinaryStream import BinaryStream
from podrum.utils.UUID import UUID

class NetBinaryStream(BinaryStream):
    def getString(self):
        self.get(self.getUnsignedVarInt())
        
    def putString(self, value):
        self.putUnsignedVarInt(len(value))
        self.buffer += value
        
    def getUUID(self):
        part1 = self.getLInt()
        part0 = self.getLInt()
        part3 = self.getLInt()
        part2 = self.getLInt()
        return UUID(part0, part1, part2, part3)
    
    def putUUID(self, uuid: UUID):
        self.putLInt(uuid.getPart(1))
        self.putLInt(uuid.getPart(0))
        self.putLInt(uuid.getPart(3))
        self.putLInt(uuid.getPart(2))
