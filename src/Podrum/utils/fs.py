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


def read(file):
    with open(file) as f:
        return f.read()
        f.close()


def write(file, content):
    with open(file) as f:
        f.write(content)


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
    if not checkForFile('f', path, 'server.json'):
        createFile(path, 'server.json')
        firstLaunch = True
    elif not checkForFile('dir', path, 'plugins'):
        createDir(path, 'plugins')
    elif not checkForFile('dir', path, 'worlds'):
        createDir(path, 'worlds')
    # if firstLaunch: wizard() TODO: Implement wizard
