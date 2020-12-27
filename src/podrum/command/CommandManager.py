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

from podrum.command.vanilla.DifficultyCommand import DifficultyCommand
from podrum.command.vanilla.HelpCommand import HelpCommand
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
        if command in self.commands:
            return self.commands[command]
        else:
            Logger.log("error", "Invalid Command")
            return False

    def registerVanillaCommands(self):
        self.registerCommand(DifficultyCommand())
        self.registerCommand(HelpCommand())
        self.registerCommand(PluginsCommand())
        self.registerCommand(ReloadCommand())
        self.registerCommand(SayCommand())
        self.registerCommand(StopCommand())

    def registerCommand(self, command):
        self.commands.update({command.getName(): command})
