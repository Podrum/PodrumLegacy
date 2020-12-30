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
from podrum.command.CommandManager import CommandManager

class HelpCommand(Command):
    def __init__(self, name = "", description = ""):
        super().__init__("help", "Help Command")

    def execute(self, sender, args):
        sender.sendMessage("--- Showing help ---")
        for k, v in CommandManager.commands.items():
            if k != self.name:
                sender.sendMessage("/" + k + ": " + v.description)
