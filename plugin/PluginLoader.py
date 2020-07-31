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
    pluginsDir = Plugin.getPluginsDir()

    @staticmethod
    def setValues(plugin):
        PluginLoader.name = Plugin.getName(plugin)
        PluginLoader.description = Plugin.getDescription(plugin)
        PluginLoader.author = Plugin.getAuthor(plugin)
        PluginLoader.version = Plugin.getVersion(plugin)
        PluginLoader.apiVersion = Plugin.getApiVersion(plugin)
        PluginLoader.main = Plugin.getMain(plugin)

    @staticmethod
    def load(plugin):
        if Plugin.getName(plugin) in PluginLoader.loadedPluginNames:
            Logger.log('alert', f'Disabling duplicate plugin {Plugin.getName(plugin)}')
            return
        PluginLoader.setValues(plugin)
        sys.path.insert(0, plugin)
        PluginLoader.pluginModule = importlib.import_module(PluginLoader.main.rsplit('.', 1)[0])
        pluginClass = getattr(PluginLoader.pluginModule, PluginLoader.main.rsplit('.', 1)[1])
        Logger.log('info', f'Loading {PluginLoader.name}...')
        pluginClass.onStart()
        Logger.log('success', f'Successfully loaded {PluginLoader.name}!')
        pluginClass.onStarted()
        PluginLoader.loadedPluginFiles.update({plugin: plugin})
        PluginLoader.loadedPluginNames.update({PluginLoader.name: PluginLoader.name})
        PluginLoader.loadedPluginsList = list(PluginLoader.loadedPluginNames.keys())
        PluginLoader.loadedPluginsCount = len(PluginLoader.loadedPluginNames)

    @staticmethod
    def unload(plugin):
        PluginLoader.setValues(plugin)
        if PluginLoader.main.rsplit('.', 1)[0] in sys.modules:
            PluginLoader.pluginModule = importlib.import_module(PluginLoader.main.rsplit('.', 1)[0])
            pluginClass = getattr(PluginLoader.pluginModule, PluginLoader.main.rsplit('.', 1)[1])
            Logger.log('info', f'Unloading {PluginLoader.name}...')
            pluginClass.onStop()
            Logger.log('success', f'Successfully unloaded {PluginLoader.name}!')
            pluginClass.onStopped()
            del sys.modules[PluginLoader.main.rsplit('.', 1)[0]]
            del PluginLoader.loadedPluginFiles[plugin]
            del PluginLoader.loadedPluginNames[PluginLoader.name]
            PluginLoader.loadedPluginsList = list(PluginLoader.loadedPluginNames.keys())
            PluginLoader.loadedPluginsCount = len(PluginLoader.loadedPluginNames)

    @staticmethod
    def reload(plugin):
        PluginLoader.unload(plugin)
        PluginLoader.load(plugin)

    @staticmethod
    def loadAll():
        pluginsDir = PluginLoader.pluginsDir
        pluginsPaths = glob(pluginsDir + "/*.pyz")
        for pluginPath in pluginsPaths:
            if os.path.isfile(pluginPath):
                PluginLoader.load(pluginPath)

    @staticmethod
    def unloadAll():
        pluginsDir = PluginLoader.pluginsDir
        pluginsPaths = glob(pluginsDir + "/*.pyz")
        for pluginPath in pluginsPaths:
            if os.path.isfile(pluginPath):
                PluginLoader.unload(pluginPath)

    @staticmethod
    def reloadAll():
        pluginsDir = PluginLoader.pluginsDir
        pluginsPaths = glob(pluginsDir + "/*.pyz")
        for pluginPath in pluginsPaths:
            if os.path.isfile(pluginPath):
                PluginLoader.reload(pluginPath)


