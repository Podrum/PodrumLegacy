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

from podrum.nbt.tag import ByteArrayTag
from podrum.nbt.tag import ByteTag
from podrum.nbt.tag import CompoundTag
from podrum.nbt.tag import DoubleTag
from podrum.nbt.tag import FloatTag
from podrum.nbt.tag import IntArrayTag
from podrum.nbt.tag import IntTag
from podrum.nbt.tag import ListTag
from podrum.nbt.tag import LongArrayTag
from podrum.nbt.tag import LongTag
from podrum.nbt.tag import NamedTag
from podrum.nbt.tag import ShortTag
from podrum.nbt.tag import StringTag

class NBT:
    tagType = {
        "EndTag": 0,
        "ByteTag": 1,
        "ShortTag": 2,
        "IntTag": 3,
        "LongTag": 4,
        "FloatTag": 5,
        "DoubleTag": 6,
        "ByteArrayTag": 7,
        "StringTag": 8,
        "ListTag": 9,
        "CompoundTag": 10,
        "IntArrayTag": 11,
        "LongArrayTag": 12
    }

    def createTag(self, type: int) -> NamedTag:
        if type == self.tagType["ByteTag"]:
            return ByteTag.ByteTag()
        elif type == self.tagType["ShortTag"]:
            return ShortTag.ShortTag()
        elif type == self.tagType["IntTag"]:
            return IntTag.IntTag()
        elif type == self.tagType["LongTag"]:
            return LongTag.LongTag()
        elif type == self.tagType["FloatTag"]:
            return FloatTag.FloatTag()
        elif type == self.tagType["DoubleTag"]:
            return DoubleTag.DoubleTag()
        elif type == self.tagType["ByteArrayTag"]:
            return ByteArrayTag.ByteArrayTag()
        elif type == self.tagType["StringTag"]:
            return StringTag.StringTag()
        elif type == self.tagType["ListTag"]:
            return ListTag.ListTag()
        elif type == self.tagType["CompoundTag"]:
            return CompoundTag.CompoundTag()
        elif type == self.tagType["IntArrayTag"]:
            return IntArrayTag.IntArrayTag()
        elif type == self.tagType["LongArrayTag"]:
            return LongArrayTag.LongArrayTag()
        else:
            raise Exception(f"Unknown NBT tag type {str(type)}")