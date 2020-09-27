"""
*
*  __  __ _____ ____   ____                 _             
* |  \/  |  ___|  _ \ / ___| __ _ _ __ ___ (_)_ __   __ _ 
* | |\/| | |_  | | | | |  _ / _` | '_ ` _ \| | '_ \ / _` |
* | |  | |  _| | |_| | |_| | (_| | | | | | | | | | | (_| |
* |_|  |_|_|   |____/ \____|\__,_|_| |_| |_|_|_| |_|\__, |
*                                                    |___/ 
*
* Licensed under the Apache License, Version 2.0 (the "License")
* you may not use this file except in compliance with the License.
* You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
"""

import warnings
from urllib import request
import json

version = "3.1"

def checkForLatestVersion():
    req = request.urlopen('https://pypi.python.org/pypi/BinUtilsPY/json')
    currentVersion = json.load(req)['info']['version']
    if currentVersion != version:
        warnings.warn("You are not using the latest version of BinUtilsPY: The latest version is: " + currentVersion + ", while you have: " + version)

checkForLatestVersion()

__all__ = ['Binary', 'BinaryStream']

from binutilspy.Binary import Binary
from binutilspy.BinaryStream import BinaryStream
