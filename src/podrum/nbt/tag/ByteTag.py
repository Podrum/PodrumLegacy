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

from podrum.nbt.NBT import NBT
from podrum.nbt.NBTStream import NBTStream
from podrum.nbt.ReaderTracker import ReaderTracker
from podrum.nbt.tag.NamedTag import NamedTag
from podrum.utils.Binary import Binary

class ByteTag(NamedTag):
    value = None

    def __init__(self, name: str = "", value: int = 0):
        super().__init__(name)
        if value < -128 or value > 127:
            raise Exception("Value " + value + " is too large!")
        self.value = value

    def getType(self) -> int:
        return NBT.TAG_Byte

    def read(self, nbt: NBTStream, tracker: ReaderTracker):
        self.value = nbt.getSignedByte()

    def write(self, nbt: NBTStream):
        nbt.buffer += chr(self.value)

    def getValue(self) -> int:
        return self.value