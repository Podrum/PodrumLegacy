"""
*  ____           _
* |  _ \ ___   __| |_ __ _   _ _ __ ___
* | |_) / _ \ / _` | '__| | | | '_ ` _ \
* |  __/ (_) | (_| | |  | |_| | | | | | |
* |_|   \___/ \__,_|_|   \__,_|_| |_| |_|
*
* Licensed under the Apache License, Version 2.0 (the "License")
* you may not use this file except in compliance with the License.
* You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
"""

from podrum.plugin.PluginLoader import PluginLoader

class PluginBase:
    name = ""
    description = ""
    author = ""
    version = ""
    apiVersion = ""
    
    def __init__(self):
        self.name = PluginLoader.name
        self.description = PluginLoader.description
        self.author = PluginLoader.author
        self.version = PluginLoader.version
        self.apiVersion = PluginLoader.apiVersion
    
    def onStart(self): pass

    def onStarted(self): pass

    def onStop(self): pass

    def onStopped(self): pass
    
    def getName(self):
        return self.name

    def getDescription(self):
        return self.description

    def getAuthor(self):
        return self.author

    def getVersion(self):
        return self.version

    def getApiVersion(self):
        return self.apiVersion
