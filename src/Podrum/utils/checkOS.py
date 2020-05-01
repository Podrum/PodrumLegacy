from sys import platform

def getOS():
    if platform == 'linux' or platform == 'linux2':
        return 'linux'
    elif platform == 'darwin':
        return 'osx'
    elif platform == 'win32' or platform == 'win64':
        return 'windows'