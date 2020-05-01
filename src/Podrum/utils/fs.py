import os


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
    if not checkForFile('f', path, 'server.json'): createFiles(path, 'server.json')
    elif not checkForFile('dir', path, 'plugins'): createDir(path, 'plugins')
    elif not checkForFile('dir', path, 'worlds'): createDir(path, 'worlds')
