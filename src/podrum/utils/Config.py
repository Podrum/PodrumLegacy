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
    
    config = {}
    nestedCache = []
    file = None
    correct = False
    _type = DETECT

    formats = {
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
    }

    def __init__(self, file: str, _type = DETECT: int, default = [], correct = None):
        self.load(file, _type, default)
        correct = self.correct
    
    def reload(self):
        self.config = {}
        self.nestedCache = []
        self.correct = False
        self.load(self.file, self._type)
        
    @staticmethod
    def fixYAMLIndexes(_str: str) -> str:
        return re.sub(r"#^( *)(y|Y|yes|Yes|YES|n|N|no|No|NO|true|True|TRUE|false|False|FALSE|on|On|ON|off|Off|OFF)( *)\:#m", "\1\"\2\"\3:", _str)
    
    def load(self, file, _type = DETECT, default = []):
        self.correct = True
        self._type = int(_type)
        self.file = file
        if not isinstance(default, dict):
            default = {}
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
            if (self._type == self.PROPERTIES) and (self._type == self.CNF):
                self.parseProperties(content)
            elif self._type == self.JSON:
                self.config = json.loads(content)
            elif self._type == self.YAML:
                content = self.fixYAMLIndexes(content)
                self.config = yaml.load(content)
            elif self._type == self.SERIALIZED:
                self.config = pickle.loads(content)
            elif self._type == self.ENUM:
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
        return correct == True
    
    def save(self) -> None:
        if self.correct == True:
            try:
                content = None
                if (self._type == self.PROPERTIES) or (self._type == self.CNF):
                    content = writeProperties()
                elif self._type == self.JSON:
                    content = json.dumps(config)
                elif self._type == self.YAML:
                    content = yaml.emit(config)
                elif self._type == self.SERIALIZED:
                    content = pickle.dumps(self.config)
                elif self._type == self.ENUM:
                    "\r\n".join(config.keys())
                else:
                    correct = False
                    return False
            except ValueError:
                logger.log('error', f'Could not save Config {self.file}')
            return True
        else:
            return false
        
    def setJsonOption(self, options: int):
        if self.__type is not self.JSON:
            raise RuntimeError("Attempt to set JSON options for non-JSON config")
        self.json_options = options
        self.changed = True

        return self

    def enableJsonOption(self, options: int):
        if self.__type is not self.JSON:
            raise RuntimeError("Attempt to enable  JSON options for non-JSON config")
        self.json_options |= options
        self.changed = True

        return self

    def disableJsonOption(self, options: int):
        if self.__type is not self.JSON:
            raise RuntimeError("Attempt to disable JSON options for non-JSON config")
        self.json_options &= ~options
        self.changed = True

        return self

    def getJsonOption(self) -> int:
        if self.__type is not self.JSON:
            raise RuntimeError("Attempt to get JSON options for non-JSON config")
        return self.json_options

    def get(self, k, default = False):
        return self.config[k] if self.config[k] else default

    def set(self, k, v = True):
        self.config[k] = v
        self.changed = True
        for nkey, nvalue in self.nested_cache:
            if nkey[0:len(k) + 1] is k + ".":
                del self.nested_cache[nkey]
                
    def getAll(self, keys = False):
        return self.config.keys() if keys == True else self.config   

    def setAll(self, v):
        self.config = v

    def writeProperties(self) -> str:
        content = "#Properties Config file\r\n#" + time.strftime("%c") + "\r\n"
        for k, v in self.config.items():
            if isinstance(v, bool):
                v = "on" if v else "off"
            elif isinstance(v, list):
                v = ';'.join(v)
            content += str(k) + "=" + str(v) + "\r"
        return content

    def parseProperties(self, content: str):
        matches = re.findall(r'/([a-zA-Z0-9\-_\.]+)[ \t]*=([^\r\n]*)/u', content)
        if len(matches) > 0:
            for i, k in enumerate(matches[1]):
                v = str(matches[2][i]).strip()
                if v.lower() == "on" or v.lower() == "true" or v.lower() == "yes":
                    v = True
                    break
                if v.lower() == "off" or v.lower() == "false" or v.lower() == "no":
                    v = False
                    break
                if self.config[k]:
                    Logger.log('debug', "[Config] Repeated property {} on file {}".format(k, self.file))
                self.config[k] = v
