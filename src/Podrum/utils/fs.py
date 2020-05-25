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
import json
from ..wizard import wizard


def read(file):
    with open(file) as f:
        return f.read()
        f.close()


def write(file, content):
    with open(file) as f:
        f.write(content)
        f.close()


# Name include extension
def createFile(path, name):
    f = open(f'{path}/{name}', 'w+')
    f.close()


def createDir(path, name):
    try:
        os.mkdir(f'{path}/{name}')
    except:
        pass


def checkForFile(path, name):
    return os.path.isfile(f'{path}/{name}')


def checkForDir(path):
    return os.path.isdir(f'{path}')


def checkAllFiles(path):
    firstLaunch = False
    if not checkForFile(path, 'server.json') or (os.path.getsize(f'{path}/server.json') == 0):
        createFile(path, 'server.json')
        firstLaunch = True
    elif not checkForFile(path, 'plugins'):
        createDir(path, 'plugins')
    elif not checkForFile(path, 'worlds'):
        createDir(path, 'worlds')
    if firstLaunch:
        wizard.wizard(path)

def createServerConfigFromWizard(path, isWizardSkipped, options):
    if(isWizardSkipped == False):
        with open(f'{path}/server.json', 'w', encoding="utf8") as file:
            content = {
            "MOTD": options[1],
            "Language": options[0],
            "MaxPlayers": options[2],
            "Gamemode": options[3]

            }
            json.dump(content, file, indent=4, skipkeys=True, ensure_ascii=False)
    else:
        content = {
            "MOTD": "Podrum powered server.",
            "Language": "eng",
            "MaxPlayers": "20",
            "Gamemode": "0"

        }
        with open(f'{path}/server.json', 'w', encoding="utf8") as fl:
            json.dump(content, fl, indent=4, skipkeys=True)
