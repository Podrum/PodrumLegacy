class PluginBase:
    name = ""
    description = ""
    author = ""
    version = ""

    def getName(self):
        return self.name

    def getDescription(self):
        return self.description

    def getAuthor(self):
        return self.author

    def getVersion(self):
        return self.version

    def onEnable(self):
        pass

    def onDisable(self):
        pass
