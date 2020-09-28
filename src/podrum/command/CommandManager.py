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

from copy import deepcopy
from podrum.command.vanilla.PluginsCommand import PluginsCommand
from podrum.command.vanilla.ReloadCommand import ReloadCommand
from podrum.command.vanilla.SayCommand import SayCommand
from podrum.command.vanilla.StopCommand import StopCommand
from podrum.utils.Logger import Logger

class CommandManager:
    commands = {}

    def __init__(self):
        self.registerVanillaCommands()

    def isCommand(self, command):
        try:
            self.commands[command]
            return True
        except:
            Logger.log("error", "Invalid Command")
            return False

    def registerVanillaCommands(self):
        self.registerCommand("plugins", PluginsCommand("plugins"))
        self.registerCommand("reload", ReloadCommand("reload"))
        self.registerCommand("say", SayCommand("say"))
        self.registerCommand("stop", StopCommand("stop"))

    def registerCommand(self, name, command):
        self.commands.update({name: deepcopy(command)})