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

import re
import os
import json
import yaml
import pickle

from podrum import Server
from podrum.utils.Properties import Properties

class Config:
    DETECT = -1
    JSON = 0
    YAML = 1
    PROPERTIES = 2
    
    formats = {
        "json": JSON,
        "yml": YAML,
        "properties", PROPERTIES
    }
    
    server = None
    config = None
    formatType = None
    
    def __init__(self):
        self.server = Server.Server()
        
    def fixYamlIndexes(self, data):
        return re.sub(r"#^( *)(y|Y|yes|Yes|YES|n|N|no|No|NO|true|True|TRUE|false|False|FALSE|on|On|ON|off|Off|OFF)( *)\:#m", "\1\"\2\"\3:", data)
        
    def load(self, path, formatType = DETECT):
        self.config = {}
        self.formatType = formatType
        if os.path.isfile(path):
            file = open(path).read()
            if self.formatType == self.DETECT:
                bname = os.path.basename(self.file)
                extension = os.path.splitext(bname)[0]
                try:
                    self.formatType = self.formats[extension]
                except:
                    return
            if self.formatType == self.JSON:
                self.config = json.loads(content)
            elif self.formatType == self.YAML:
                self.fixYamlIndexes(content)
                self.config = yaml.loads(content)
            elif self.formatType == self.PROPERTIES:
                self.config = Properties.loads(content)
                
