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

import os

from podrum.lang import Base

class Parser:

    def checkYesNo(str):
        str = str.lower()
        if str == 'y' or str == 'yes':
            return True
        elif str == 'n' or str == 'no':
            return False
        else:
            return

    def checkIfLangExists(str):
        path = os.getcwd() + '/src/podrum/lang/'
        allLangs = Base.Base.getLangNames(path)
        if(str in allLangs):
            return True
        else:
            return False
