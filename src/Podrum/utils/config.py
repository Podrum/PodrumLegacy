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

from .fs import *
from ..Server import Server

class Config:
    DETECT = -1
    PROPERTIES = 0
    CNF = PROPERTIES
    JSON = 1
    YAML = 2
    EXPORT = 3
    SERIALIZED = 4
    ENUM = 5
    ENUMERATION = ENUM
    
    config = []
    nestedCache = []
    file = ''
    correct = False
    type = DETECT

    formats = [{
        "properties" : PROPERTIES,
        "cnf" : CNF,
        "conf" : CNF,
        "config" : CNF,
        "json" : JSON,
        "js" : JSON,
        "yml" : YAML,
        "yaml" : YAML,
        "export" : EXPORT,
        "xport" : EXPORT,
        "sl" : SERIALIZED,
        "serialize" : SERIALIZED,
        "txt" : ENUM,
        "list" : ENUM,
        "enum" : ENUM,
    }]

    def __init__(,self, file, type_ = DETECT, default = [], correct = None):
        self.load(file, type_, default)
        correct = self.correct
        
    def reload(self):
        config = []
        nestedCache = []
        correct = False
        self.load(self.file, self.type_)
        
    def fixYAMLIndexes(self, string):
        return re.sub(r"#^([ ]*)([a-zA-Z_]{1}[ ]*)\\:$#m", r"$1\"$2\":", string)
    
    def load(self, file, type = DETECT, default = []):
        self.correct = True
        self.type = type
        self.file = file
        if not in_array(default):
            default = []
        if checkForFile(Server.path, file):
            self.config = default
            self.save()
        else:
            if self.type == self.DETECT:
                bname = os.path.basename(self.file)
                extension = bname.split(".")
                arrlist = extension.pop()
                extension = arrlist.strip().lower()
        
