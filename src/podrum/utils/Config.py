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
import pickle
from podrum.utils import Logger

from podrum.ServerFS.ServerFS import read
from podrum.Server import Server

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
    is_array = lambda var: isinstance(var, (list, tuple))

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

    def __init__(self, file, type = DETECT, default = [], correct=None):
        self.load(file, type, default)
        correct = correct

    @staticmethod
    def isset(self, variable):
        return variable in locals() or variable in globals()
    
    def reload(self):
        self.config = []
        self.nestedCache = []
        self.correct = False
        self.load(self.file, self.type)
        
    @staticmethod
    def fixYAMLIndexes(str):
        return re.sub(r"#^([ ]*)([a-zA-Z_]{1}[ ]*)\\:$#m", r"$1\"$2\":", str)
    
    def load(self, file, type=DETECT, default = []):
        self.correct = True
        self.type = type
        self.file = file
        if not self.is_array(default):
            default = []
        if not os.path.exists(file):
            self.config = default
            self.save()
        else:
            if self.type == self.DETECT:
                bname = os.path.basename(self.file)
                extension = bname.split(".")
                arrlist = extension.pop()
                extension = arrlist.strip().lower()
                if self.isset(self.formats[extension]):
                    self.type = self.formats[extension]
                else:
                    self.correct = False
            if self.correct:
                content = open(self.file).read()
            if (self.type == self.PROPERTIES) and (self.type == self.CNF):
                self.parseProperties(content)
            elif self.type == self.JSON:
                self.config = json.loads(content)
            elif self.type == self.YAML:
                content = self.fixYAMLIndexes(content)
                self.config = yaml.load(content)
            elif self.type == self.SERIALIZED:
                self.config = pickle.loads(content)
            elif self.type == self.ENUM:
                self.parseList(content)
            else:
                self.correct = False
                return False
            if not self.is_array(self.config): # Is array doesn't exist
                self.config = default
            if self.fillDefaults(default, self.config) > 0:
                self.save()
        else:
            return False

        return True

    def check():
        return correct = True
    
    def save():
        if self.correct == True:
            try:
                content = None
                if (type == PROPERTIES) and (type == CNF):
                    content = writeProperties()
                elif type == JSON:
                    content = json.dumps(config)
                elif type == YAML:
                    content = yaml.emit(config)
                elif type == SERIALIZED:
                    content = pickle.dumps(self.config)
                elif type == ENUM:
                    "\r\n".join(config.keys())
                else:
                    correct = False
                    return False
            except ValueError:
                logger.log('error', f'Could not save Config {self.file}')
            return True
        else:
            return false
