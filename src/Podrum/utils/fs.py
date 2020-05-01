import os





class fs:
    def read(self):
        pass

    def write(self):
        pass

    # Name include extension
    def createFiles(path, name):
        open(f'{path}/{name}', 'w+')

    def createDir(self, path, name):
        os.mkdir(f'{path}/{name}')

    def checkForFile(self, type_, path, name):
        if type_.lower() == 'file' or 'f':
            return os.path.isfile(f'{path}/{name}')
        elif type_.lower() == 'directory' or 'dir':
            return os.path.isdir(f'{path}/{name}')

    def checkAllFiles(self, path):
        if not self.checkForFile('f', path, 'server.json'):
            self.createFiles(path, 'server.json')
        elif not self.checkForFile('dir', path, 'plugins'):
            self.createDir(path, 'plugins')
        elif not self.checkForFile('dir', path, 'worlds'):
            self.createDir(path, 'worlds')
