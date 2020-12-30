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

class CommandManager:
    commands = {}

    @staticmethod
    def isCommand(command):
        if command in CommandManager.commands:
            return True
        return False
    
    @staticmethod
    def registerVanillaCommands():
        CommandManager.registerCommand(DifficultyCommand())
        CommandManager.registerCommand(HelpCommand())
        CommandManager.registerCommand(PluginsCommand())
        CommandMamager.registerCommand(ReloadCommand())
        CommandManager.registerCommand(SayCommand())
        CommandManager.registerCommand(StopCommand())

    @staticmethod
    def registerCommand(command):
        CommandManager.commands[command.name] = command
