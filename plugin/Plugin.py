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

import array
import os
import json
import zipfile

class Plugin:
    @staticmethod
    def getPluginsDir():
        return os.getcwd() + "/plugins"

    @staticmethod
    def getPlugin(plugin):
        return zipfile.ZipFile(plugin)

    @staticmethod
    def getJsonManifest(plugin):
        data = Plugin.getPlugin(plugin).open("plugin.json").read()
        jsonData = json.loads(data)
        return jsonData
                
    @staticmethod
    def getName(plugin):
        return Plugin.getJsonManifest(plugin)["name"]

    @staticmethod
    def getDescription(plugin):
        return Plugin.getJsonManifest(plugin)["description"]

    @staticmethod
    def getAuthor(plugin):
        return Plugin.getJsonManifest(plugin)["author"]

    @staticmethod
    def getVersion(plugin):
        return Plugin.getJsonManifest(plugin)["version"]

    @staticmethod
    def getApiVersion(plugin):
        return Plugin.getJsonManifest(plugin)["api-version"]

    @staticmethod
    def getMain(plugin):
        return Plugin.getJsonManifest(plugin)["main"]