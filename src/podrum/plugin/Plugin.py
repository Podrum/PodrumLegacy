import importlib
import json
import os
import sys
from zipfile import ZipFile

class Plugin:
    pluginsDir = ""
    plugins = {}
    pluginsCount = 0

    def __init__(self, pluginsDir):
        self.pluginsDir = pluginsDir

    def load(self, dir):
        plugin = ZipFile(dir, "r")
        pluginInfo = json.loads(plugin.read("plugin.json"))
        if pluginInfo["name"] in self.plugins:
            print("Cannot load duplicate plugin " + pluginInfo["name"])
            return
        sys.path.append(dir)
        module_str, obj_str = pluginInfo["main"].rsplit(".", 1)
        module = importlib.import_module(module_str)
        obj = getattr(module, obj_str)
        self.plugins[pluginInfo["name"]] = {
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
        obj().onEnable()
        self.pluginsCount += 1

    def loadAll(self):
        for path in os.listdir(self.pluginsDir):
            if os.path.isfile(path):
                if path.endswith(".pyz"):
                    self.load(path)

    def unload(self, name):
        if name in self.plugins:
            self.plugins[name]["main"].onDisable()
            del self.plugins[name]
            self.pluginsCount -= 1

    def unloadAll(self):
        for name in dict(self.plugins):
            self.unload(name)
