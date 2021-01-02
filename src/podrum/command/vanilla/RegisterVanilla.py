"""
*  ____           _
* |  _ \ ___   __| |_ __ _   _ _ __ ___
* | |_) / _ \ / _` | '__| | | | '_ ` _ \
* |  __/ (_) | (_| | |  | |_| | | | | | |
* |_|   \___/ \__,_|_|   \__,_|_| |_| |_|
*
* Licensed under the Mozilla Public License, Version 2.
* Permissions of this weak copyleft license are conditioned on making
* available source code of licensed files and modifications of those files 
* under the same license (or in certain cases, one of the GNU licenses).
* Copyright and license notices must be preserved. Contributors
* provide an express grant of patent rights. However, a larger work
* using the licensed work may be distributed under different terms and without 
* source code for files added in the larger work.
"""

from podrum.command.CommandManager import CommandManager
from podrum.command.vanilla.DifficultyCommand import DifficultyCommand
from podrum.command.vanilla.HelpCommand import HelpCommand
from podrum.command.vanilla.PluginsCommand import PluginsCommand
from podrum.command.vanilla.ReloadCommand import ReloadCommand
from podrum.command.vanilla.SayCommand import SayCommand
from podrum.command.vanilla.StopCommand import StopCommand

class RegisterVanilla:
    def __init__(self):
        CommandManager.registerCommand(DifficultyCommand())
        CommandManager.registerCommand(HelpCommand())
        CommandManager.registerCommand(PluginsCommand())
        CommandManager.registerCommand(ReloadCommand())
        CommandManager.registerCommand(SayCommand())
        CommandManager.registerCommand(StopCommand())
