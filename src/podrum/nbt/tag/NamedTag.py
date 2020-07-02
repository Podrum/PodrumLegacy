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

from podrum.nbt.NBTStream import NBTStream
from podrum.nbt.ReaderTracker import ReaderTracker

class NamedTag():
    __metaclass__ = ABCMeta
    
    name = None
    cloning = False
    
    def __init__(self, name = ''):
        if len(name > 32767):
            raise ValueError("Tag name cannot be more than 32767 bytes, got length " + str(len(name)))
        self.name = name
        
    def getName(self):
        return self.name
    
    def setName(self, name):
        self.name = name
