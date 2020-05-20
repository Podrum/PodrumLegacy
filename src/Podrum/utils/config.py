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
import re
import os
import json
import yaml

from .fs import read
from ..Server import server

class Config:
    DETECT = -1
    PROPERTIES = 0
    CNF = self.PROPERTIES
    JSON = 1
    YAML = 2
    EXPORT = 3
    SERIALIZED = 4
    ENUM = 5
    ENUMERATION = self.ENUM
    
    config = []
    nestedCache = []
    file = ''
    correct = false
    type = self.DETECT

    formats = [{
        "properties" : self.PROPERTIES,
        "cnf" : self.CNF,
        "conf" : self.CNF,
        "config" : self.CNF,
        "json" : self.JSON,
        "js" : self.JSON,
        "yml" : self.YAML,
        "yaml" : self.YAML,
        "export" : self.EXPORT,
        "xport" : self.EXPORT,
        "sl" : self.SERIALIZED,
        "serialize" : self.SERIALIZED,
        "txt" : self.ENUM,
        "list" : self.ENUM,
        "enum" : self.ENUM,
    }]

    def __init__(file, type = self.DETECT, default = [], correct = null):
        self.load(file, type, default)
        correct = self.correct
        
    def reload():
        self.config = []
        self.nestedCache = []
        self.correct = false
        self.load(self.file, self.type)
        
    def fixYAMLIndexes(str):
        return re.sub(r"#^([ ]*)([a-zA-Z_]{1}[ ]*)\\:$#m", r"$1\"$2\":", str)
    
    def load(file, type = self.DETECT, default = []):
        self.correct = true
        self.type = type
        self.file = file
        if !in_array(default):
            default = []
        if !os.path.exists(file):
            self.config = default
            self.save()
        else:
            if self.type == self.DETECT:
                bname = os.path.basename(self.file)
                extension = bname.split(".")
                arrlist = extension.pop()
                extension = arrlist.strip().lower()
                if d
        
