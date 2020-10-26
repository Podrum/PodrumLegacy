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

from podrum.command.Command import Command
from podrum.plugin.PluginLoader import PluginLoader

class PluginsCommand(Command):
    def __init__(self, name = "", description = ""):
        super().__init__("plugins", "Plugins Command")

    def execute(self, sender, args):
        pluginsString = ""
        for pluginName in PluginLoader.loadedPluginsList:
            pluginsString.join(pluginName)
            if pluginName != PluginLoader().loadedPluginsList[PluginLoader().loadedPluginsCount - 1]:
                pluginsString.join(", ")
        sender.sendMessage(f"Plugins({PluginLoader.loadedPluginsCount}): {pluginsString}")