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
    config = {}
    
    def __init__(self):
        self.server = Server.Server()
        
    def load(self, path, format = DETECT):
        if os.path.isfile(path):
            file = open(path)
            if format == self.DETECT:
                bname = os.path.basename(self.file)
                extension = os.path.splitext(bname)[0]
                try:
                    self.formats[extension]
                except:
                    return
            elif format == self.JSON:
                pass
                
                
