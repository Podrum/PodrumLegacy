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

from podrum.nbt.tag.ByteArrayTag import ByteArrayTag
from podrum.nbt.tag.ByteTag import ByteTag
from podrum.nbt.tag.CompoundTag import CompoundTag
from podrum.nbt.tag.DoubleTag import DoubleTag
from podrum.nbt.tag.FloatTag import FloatTag
from podrum.nbt.tag.IntArrayTag import IntArrayTag
from podrum.nbt.tag.IntTag import IntTag
from podrum.nbt.tag.ListTag import ListTag
from podrum.nbt.tag.LongArrayTag import LongArrayTag
from podrum.nbt.tag.LongTag import LongTag
from podrum.nbt.tag.NamedTag import NamedTag
from podrum.nbt.tag.ShortTag import ShortTag
from podrum.nbt.tag.StringTag import StringTag

class NBT:
    TAG_End = 0
    TAG_Byte = 1
    TAG_Short = 2
    TAG_Int = 3
    TAG_Long = 4
    TAG_Float = 5
    TAG_Double = 6
    TAG_ByteArray = 7
    TAG_String = 8
    TAG_List = 9
    TAG_Compound = 10
    TAG_IntArray = 11
    TAG_LongArray = 12

    def createTag(self, type: int) -> NamedTag:
        if type == self.TAG_Byte:
            return ByteTag()
        elif type == self.TAG_Short:
            return ShortTag()
        elif type == self.TAG_Int:
            return IntTag()
        elif type == self.TAG_Long:
            return LongTag()
        elif type == self.TAG_Float:
            return FloatTag()
        elif type == self.TAG_Double:
            return DoubleTag()
        elif type == self.TAG_ByteArray:
            return ByteArrayTag()
        elif type == self.TAG_String:
            return StringTag()
        elif type == self.TAG_List:
            return ListTag()
        elif type == self.TAG_Compound:
            return CompoundTag()
        elif type == self.TAG_IntArray:
            return IntArrayTag()
        elif type == self.TAG_LongArray:
            return LongArrayTag()
        else:
            raise ValueError("Unknown NBT tag type " + str(type))