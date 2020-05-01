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

from ..wizard import wizard

def read():
    pass


def write():
    pass


# Name include extension
def createFiles(path, name):
    open(f'{path}/{name}', 'w+')


def createDir(path, name):
    os.mkdir(f'{path}/{name}')


def checkForFile(type_, path: str, name: str):
    if type_.lower() == 'file' or 'f': return os.path.isfile(f'{path}/{name}')
    elif type_.lower() == 'directory' or 'dir': return os.path.isdir(f'{path}/{name}')


def checkAllFiles(path):
    firstLaunch = False
    if not checkForFile('f', path, 'server.json'):
        createFiles(path, 'server.json')
        firstLaunch = True
    elif not checkForFile('dir', path, 'plugins'): createDir(path, 'plugins')
    elif not checkForFile('dir', path, 'worlds'): createDir(path, 'worlds')
    if firstLaunch: wizard()
