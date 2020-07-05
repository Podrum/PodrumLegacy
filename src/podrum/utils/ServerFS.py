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
import zipfile
from podrum.wizard import Wizard

class ServerFS:
    def read(file):
        with open(file) as f:
            content = f.read()
            f.close()
            return content


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

    def getLangDir():
        if ServerFS.checkForDir(os.path.dirname(os.path.abspath(__file__)) + '/..'):
            langDir = os.path.dirname(os.path.abspath(__file__)) + '/../lang'
        else:
            pyzDir = zipfile.ZipFile(os.path.dirname(os.path.abspath(__file__)) + '/..')
            langDir = pyzFile.open('lang')
        return langDir


    def checkAllFiles(path):
        firstLaunch = False
        if not ServerFS.checkForFile(path, 'server.json') or (os.path.getsize(f'{path}/server.json') == 0):
            ServerFS.createFile(path, 'server.json')
            firstLaunch = True
        elif not ServerFS.checkForFile(path, 'plugins'):
            ServerFS.createDir(path, 'plugins')
        elif not ServerFS.checkForFile(path, 'worlds'):
            ServerFS.createDir(path, 'worlds')
        if firstLaunch:
            Wizard.Wizard.startWizard(path)

    def createServerConfigFromWizard(path, isWizardSkipped, options):
        if(isWizardSkipped == False):
            with open(f'{path}/server.json', 'w', encoding="utf8") as file:
                content = {
                "MOTD": options[2],
                "Language": options[0],
                "MaxPlayers": options[4],
                "Gamemode": options[3],
                "Server-Port": options[1]
                }
                json.dump(content, file, indent=4, skipkeys=True, ensure_ascii=False)
        else:
            content = {
                "MOTD": "Podrum powered server.",
                "Language": options[0],
                "MaxPlayers": "20",
                "Gamemode": "0",
                "Server-Port": "19132"
            }
            with open(f'{path}/server.json', 'w', encoding="utf8") as fl:
                json.dump(content, fl, indent=4, skipkeys=True)
