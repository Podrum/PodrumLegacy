import importlib
import json
import os
import sys
from zipfile import ZipFile

class Plugin:
    server = None
    pluginsDir = ""
    plugins = {}
    pluginsCount = 0

    @staticmethod
    def load(pluginDir):
        plugin = ZipFile(pluginDir, "r")
        pluginInfo = json.loads(plugin.read("plugin.json"))
        if pluginInfo["name"] in Plugin.plugins:
            print("Cannot load duplicate plugin " + pluginInfo["name"])
            return
        sys.path.append(pluginDir)
        module_str, obj_str = pluginInfo["main"].rsplit(".", 1)
        module = importlib.import_module(module_str)
        obj = getattr(module, obj_str)
        obj().onLoad()
        Plugin.plugins[pluginInfo["name"]] = {
            "description": pluginInfo["description"] if "description" in pluginInfo else "",
            "author": pluginInfo["author"] if "author" in pluginInfo else "",
            "version": pluginInfo["version"] if "version" in pluginInfo else "",
            "api-version": pluginInfo["api-version"],
            "main": obj()
        }
        obj.name = pluginInfo["name"]
        obj.description = pluginInfo["description"]
        obj.author = pluginInfo["author"]
        obj.version = pluginInfo["version"]
        obj.server = Plugin.server
        obj().onEnable()
        Plugin.pluginsCount += 1

    @staticmethod
    def loadAll():
        for fileName in os.listdir(Plugin.pluginsDir):
            path = Plugin.pluginsDir
            if not Plugin.pluginsDir.endswith("/") or not Plugin.pluginsDir.endswith("\\"):
                path += "/"
            path += fileName
            if os.path.isfile(path):
                if path.endswith(".pyz"):
                    Plugin.load(path)

    @staticmethod
    def unload(name):
        if name in Plugin.plugins:
            Plugin.plugins[name]["main"].onDisable()
            del Plugin.plugins[name]
            Plugin.pluginsCount -= 1

    @staticmethod
    def unloadAll():
        for name in dict(Plugin.plugins):
            Plugin.unload(name)
