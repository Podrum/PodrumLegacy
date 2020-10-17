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
    def getPluginsDir(self):
        return os.getcwd() + "/plugins"

    def getPlugin(self, plugin):
        return zipfile.ZipFile(plugin)
    
    def getJsonManifest(self, plugin):
        data = self.getPlugin(plugin).open("plugin.json").read()
        jsonData = json.loads(data)
        return jsonData
                
    def getName(self, plugin):
        return self.getJsonManifest(plugin)["name"]

    def getDescription(self, plugin):
        return self.getJsonManifest(plugin)["description"]

    def getAuthor(self, plugin):
        return self.getJsonManifest(plugin)["author"]

    def getVersion(self, plugin):
        return self.getJsonManifest(plugin)["version"]

    def getApiVersion(self, plugin):
        return self.getJsonManifest(plugin)["api-version"]

    def getMain(self, plugin):
        return self.getJsonManifest(plugin)["main"]
