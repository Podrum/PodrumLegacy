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

from podrum.utils.BinaryStream import BinaryStream
from podrum.utils.UUID import UUID

class NetworkStream(BinaryStream):
    def getString(self):
        return self.get(self.getUnsignedVarInt()).decode()
        
    def putString(self, value):
        self.putUnsignedVarInt(len(value))
        self.buffer += value.encode()

    def getBytesString(self):
        return self.get(self.getUnsignedVarInt())
        
    def putBytesString(self, value):
        self.putUnsignedVarInt(len(value))
        self.buffer += value
        
    def getUUID(self):
        part1 = self.getLInt()
        part0 = self.getLInt()
        part3 = self.getLInt()
        part2 = self.getLInt()
        return UUID(part0, part1, part2, part3)
    
    def putUUID(self, uuid):
        self.putLInt(uuid.getPart(1))
        self.putLInt(uuid.getPart(0))
        self.putLInt(uuid.getPart(3))
        self.putLInt(uuid.getPart(2))

    def getBlockCoordinates(self):
        pass # just one sec
    
    def putBlockCoordinates(self, vector3):
        pass # just one sec
