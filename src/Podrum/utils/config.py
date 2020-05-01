from ..Server import *
import os

from ..wizard.wizard import wizard


class Config:
    def read(self):
        pass

    def write(self):
        pass

    def createFiles(self):
        pass

    def checkForFile(self, type_, path, name):
        if type_.lower() == 'file' or 'f':
            return os.path.isfile(f'{path}/{name}')
        elif type_.lower() == 'directory' or 'dir':
            return os.path.isdir(f'{path}/{name}')

    def checkAllFiles(self, path):
        if not self.createFiles('f', path, f'server.json'):
            open(f'{path}/server.json', 'w+')
        elif not self.createFiles('dir', path, f'plugins'):
            os.mkdir(f'{path}/plugins')
        elif not self.createFiles('dir', path, f'worlds'):
            os.mkdir(f'{path}/worlds')
