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

from glob import glob
import importlib
import os
import sys

from podrum.utils.Logger import Logger
from podrum.plugin.Plugin import Plugin

class PluginLoader:
    pluginModule = None
    loadedPluginFiles = {}
    loadedPluginNames = {}
    loadedPluginsList = []
    loadedPluginsCount = 0
    name = None
    description = None
    author = None
    version = None
    apiVersion = None
    main = None
    pluginsDir = None

    def __init__(self):
        self.pluginsDir = Plugin().getPluginsDir()

    def setPluginValues(self, plugin):
        self.name = Plugin.getName(plugin)
        self.description = Plugin.getDescription(plugin)
        self.author = Plugin.getAuthor(plugin)
        self.version = Plugin.getVersion(plugin)
        self.apiVersion = Plugin.getApiVersion(plugin)
        self.main = Plugin.getMain(plugin)

    def load(self, plugin):
        if Plugin.getName(plugin) in self.loadedPluginNames:
            Logger.log('alert', f'Disabling duplicate plugin {Plugin.getName(plugin)}')
            return
        self.setPluginValues(plugin)
        sys.path.insert(0, plugin)
        self.pluginModule = importlib.import_module(self.main.rsplit('.', 1)[0])
        pluginClass = getattr(self.pluginModule, self.main.rsplit('.', 1)[1])
        Logger.log('info', f'Loading {self.name}...')
        pluginClass.onStart()
        Logger.log('success', f'Successfully loaded {self.name}!')
        pluginClass.onStarted()
        self.loadedPluginFiles.update({plugin: plugin})
        self.loadedPluginNames.update({self.name: PluginLoader.name})
        self.loadedPluginsList = list(self.loadedPluginNames.keys())
        self.loadedPluginsCount = len(self.loadedPluginNames)

    def unload(self, plugin):
        self.setPluginValues(plugin)
        if self.main.rsplit('.', 1)[0] in sys.modules:
            self.pluginModule = importlib.import_module(self.main.rsplit('.', 1)[0])
            pluginClass = getattr(self.pluginModule, self.main.rsplit('.', 1)[1])
            Logger.log('info', f'Unloading {self.name}...')
            pluginClass.onStop()
            Logger.log('success', f'Successfully unloaded {self.name}!')
            pluginClass.onStopped()
            del sys.modules[PluginLoader.main.rsplit('.', 1)[0]]
            del self.loadedPluginFiles[plugin]
            del self.loadedPluginNames[self.name]
            self.loadedPluginsList = list(self.loadedPluginNames.keys())
            self.loadedPluginsCount = len(self.loadedPluginNames)

    def reload(self, plugin):
        self.unload(plugin)
        self.load(plugin)

    def loadAll(self):
        pluginsDir = self.pluginsDir
        pluginsPaths = glob(pluginsDir + "/*.pyz")
        for pluginPath in pluginsPaths:
            if os.path.isfile(pluginPath):
                self.load(pluginPath)

    def unloadAll(self):
        pluginsDir = self.pluginsDir
        pluginsPaths = self.loadedPluginFiles
        for pluginPath in list(pluginsPaths):
            if os.path.isfile(pluginPath):
                self.unload(pluginPath)

    def reloadAll(self):
        pluginsDir = self.pluginsDir
        pluginsPaths = self.loadedPluginFiles
        for pluginPath in list(pluginsPaths):
            if os.path.isfile(pluginPath):
                self.reload(pluginPath)
