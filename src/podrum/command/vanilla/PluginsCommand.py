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
from podrum.GeneralVariables import GeneralVariables

class PluginsCommand(Command):
    def __init__(self, name = "", description = ""):
        super().__init__("plugins", "Plugins Command")

    def execute(self, sender, args):
        plugin = GeneralVariables.plugin
        pluginsString = ""
        for count, pluginName in enumerate(plugin.plugins):
            pluginsString += pluginName
            if count >= plugin.pluginsCount:
                pluginsString += ", "
        sender.sendMessage(f"Plugins({plugin.pluginsCount}): {pluginsString}")
