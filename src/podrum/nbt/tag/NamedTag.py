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

from abc import ABCMeta, abstractmethod

from podrum.nbt.NBTStream import NBTStream
from podrum.nbt.ReaderTracker import ReaderTracker

class NamedTag:
    __metaclass__ = ABCMeta
    
    name = None
    cloning = False
    
    def __init__(self, name = ''):
        if len(name > 32767):
            raise ValueError("Tag name cannot be more than 32767 bytes, got length " + str(len(name)))
        self.name = name
        
    def getName():
        return NamedTag.name
    
    def setName(name):
        NamedTag.name = name
        
    def getValue(): pass
    
    def getType(): pass
    
    def write(nbt: NBTStream): pass
    
    def read(nbt: NBTStream, tracker: ReaderTracker): pass
    
    def toString(indentation = 0):
        return ("  " * indentation) + type(object) + ": " + (("name='NamedTag.name', ") if (NamedTag.name != "") else "") + "value='" + str(NamedTag.getValue()) + "'"
    
    def safeClone() -> NamedTag:
        if NamedTag.cloning:
            raise ValueError("Recursive NBT tag dependency detected")
        NamedTag.cloning = True
        retval = NamedTag.copy()
        NamedTag.cloning = False
        retval.cloning = False
        return retval
    
    def equals(that: NamedTag):
        return NamedTag.name == that.name and NamedTag.equalsValue(that)
    
    def equalsValue(that: NamedTag):
        return isinstance(that, NamedTag()) and NamedTag.getValue() == that.getValue()
