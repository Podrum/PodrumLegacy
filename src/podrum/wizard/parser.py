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
from ..lang import base
import os

def checkYesNo(string):
    string = string.lower()
    if string == 'y' or string == 'yes':
        return True
    elif string == 'n' or string == 'no':
        return False
    else:
        return

def checkIfLangExists(string):
    path = os.getcwd() + '/src/podrum/lang/'
    allLangs = base.getLangNames(path)
    if(string in allLangs):
        return True
    else:
        return False
