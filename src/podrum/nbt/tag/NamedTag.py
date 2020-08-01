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

import copy

from podrum.nbt.NBTStream import NBTStream
from podrum.nbt.ReaderTracker import ReaderTracker

class NamedTag:
    name = none
    cloning = False
    
    def __init__(self, name = ""):
        if len(name) > 32767:
            raise Exception("Tag name cannot be more than 32767 bytes, got length " + len(name))
        self.name = name

    def getName(self) -> str:
        return self.name

    def setName(self, name: str):
        self.name = name

    def getValue(self): pass

    def getType(self) -> int: pass

    def write(self, nbt: NBTStream): pass

    def read(self, nbt: NBTStream, tracker: ReaderTracker): pass

    def toString(self, indentation: int = 0) -> str:
        return ("  " * indentation) + type(object) + ": " + (("name='NamedTag.name', ") if (self.name != "") else "") + "value='" + str(self.getValue()) + "'"

    def safeClone(self):
        if NamedTag.cloning:
            raise ValueError("Recursive NBT tag dependency detected")
        self.cloning = True
        retval = copy.deepcopy(self)
        self.cloning = False
        retval.cloning = False
        return retval

    def equals(self, that):
        return self.name == that.name and self.equalsValue(that)

    def equalsValue(self, that):
        return isinstance(that, self) and self.getValue() == that.getValue()