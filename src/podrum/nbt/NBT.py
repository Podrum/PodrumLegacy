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

from abc import ABCMeta, abstractmethod

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
    __metaclass__ = ABCMeta
    
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
    TAG_COMPOUND = 10
    TAG_IntArray = 11
    TAG_LongArray = 12
    
    @staticmethod
    def createTag(type: int) -> NamedTag:
        if type == NBT.TAG_Byte:
            return ByteTag()
        elif type == NBT.TAG_Short:
            return ShortTag()
        elif type == NBT.TAG_Int:
            return IntTag()
        elif type == NBT.TAG_Long:
            return LongTag()
        elif type == NBT.TAG_Float:
            return FloatTag()
        elif type == NBT.TAG_Double:
            return DoubleTag()
        elif type == NBT.TAG_ByteArray:
            return ByteArrayTag()
        elif type == NBT.TAG_String:
            return StringTag()
        elif type == NBT.TAG_List:
            return ListTag()
        elif type == NBT.TAG_Compound:
            return CompoundTag()
        elif type == NBT.TAG_IntArray:
            return IntArrayTag()
        elif type == NBT.TAG_LongArray:
            return LongArrayTag()
        else:
            raise ValueError("Unknown NBT tag type " + str(type))
    
    
    
