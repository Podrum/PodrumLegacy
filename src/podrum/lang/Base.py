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
import glob
import json

from podrum.utils.TextFormat import TextFormat
from podrum.wizard import Wizard

class Base:

    """
    getLangFiles and getLangNames are 
    for the wizard's use
    """

    langsList = [0]

    def getLangFiles(dir):
        path = dir + '/src/podrum/lang'
        allFiles = glob.glob(path + '/*.json')
        for file in allFiles:
            with open(f'{file}', 'r', encoding="utf8") as langFiles:
                data = json.load(langFiles)
                if "langName" in data:
                    name = data['langName']
                else:
                    name = 'Unknown name'
            langs = str(file.replace(path, '').replace("\\", "").replace('.json', ''))
            Base.langsList.append(langs)
            print(f'[{langs}] -> {name}')

    def getLangNames(dir):
        return Base.langsList

    """
    A translation from the selected 
    language is returned
    """
    def get(string):
        if Wizard.Wizard.isInWizard == True:
            path = os.getcwd() + "/src/podrum/lang/"
            with open(f'{path}/{Wizard.Wizard.options[0]}.json', 'r', encoding="utf8") as lF:
                data = json.load(lF)
                if string in data:
                    return data[string]
                else:
                    print(f"The value '{string}' does not exists in this language.")
        else:
            serverConfig = os.getcwd() + "/server.json"
            with open(f'{serverConfig}', 'r', encoding="utf8") as serverCfg:
                pref = json.load(serverCfg)
                if "Language" in pref:
                    lang = pref["Language"]
                else:
                    print(f"{TextFormat.RED}Language not found in server.json")
            path = os.getcwd() + "/src/podrum/lang/"
            with open(f'{path}{lang}.json', 'r', encoding="utf8") as lF:
                data = json.load(lF)
                if string in data:
                    return data[string]
                else:
                    print(f"{TextFormat.RED}The value '{string}' does not exists in this language")