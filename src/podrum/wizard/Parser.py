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