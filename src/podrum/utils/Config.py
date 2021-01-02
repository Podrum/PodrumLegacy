"""
*  ____           _
* |  _ \ ___   __| |_ __ _   _ _ __ ___
* | |_) / _ \ / _` | '__| | | | '_ ` _ \
* |  __/ (_) | (_| | |  | |_| | | | | | |
* |_|   \___/ \__,_|_|   \__,_|_| |_| |_|
*
* Licensed under the Mozilla Public License, Version 2.
* Permissions of this weak copyleft license are conditioned on making
* available source code of licensed files and modifications of those files 
* under the same license (or in certain cases, one of the GNU licenses).
* Copyright and license notices must be preserved. Contributors
* provide an express grant of patent rights. However, a larger work
* using the licensed work may be distributed under different terms and without 
* source code for files added in the larger work.
"""

import json
import os
from podrum.utils.Properties import Properties
from podrum.utils.Logger import Logger
import re
import toml
import yaml


class Config:
    formats = {
        "detect": -1,
        "json": 0,
        "yml": 1,
        "properties": 2,
        "toml": 3,
        "ini": 4
    }
    
    server = None
    config = None
    format = None
    file = None
        
    def fixYamlIndexes(self, data):
        return re.sub(r"#^( *)(y|Y|yes|Yes|YES|n|N|no|No|NO|true|True|TRUE|false|False|FALSE|on|On|ON|off|Off|OFF)( *)\:#m", "\1\"\2\"\3:", data)
        
    def load(self, file, configFormat = formats["detect"]):
        self.config = {}
        self.format = configFormat
        self.file = file
        content = file.read()
        if self.format == self.formats["detect"]:
            baseName = os.path.basename(self.file.name)
            extension = baseName.rsplit(".", 1)[1]
            if extension in self.formats:
                self.format = self.formats[extension]
        if self.format == self.formats["json"]:
            self.config = json.loads(content)
        elif self.format == self.formats["yaml"]:
            self.fixYamlIndexes(content)
            self.config = yaml.loads(content)
        elif self.format == self.formats["properties"]:
            self.config = Properties.loads(content)
        elif self.format == self.formats["toml"]:
            self.config = toml.loads(content)
        elif self.format == self.formats["ini"]:
            self.config = toml.loads(content)

    def close(self):
        self.file.close()
                
    def save(self):
        try:
            if self.format == self.formats["json"]:
                self.file = open(self.file.name , "+w")
                json.dump(self.config, self.file, indent = 4)
            elif self.format == self.formats["yaml"]:
                self.file = open(self.file.name , "+w")
                yaml.dump(self.config, self.file)
            elif self.format == self.formats["properties"]:
                self.file = open(self.file.name , "+w")
                Properties.dump(self.config, self.file)
            elif self.format == self.formats["toml"]:
                self.file = open(self.file.name , "+w")
                toml.dump(self.config, self.file)
            elif self.format == self.formats["ini"]:
                self.file = open(self.file.name , "+w")
                toml.dump(self.config, self.file)
        except Exception as e:
            Logger.error(f"Could not save the config: {self.file.name}")
            Logger.error(e)
                
