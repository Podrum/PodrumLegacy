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
from podrum.command import CommandManager

class HelpCommand(Command):
    commandManager = None

    def __init__(self, name = "", description = ""):
        super().__init__("difficulty", "Sets the difficulty level")
        self.commandManager = CommandManager.CommandManager

    def execute(self, sender, args):
        if args[1] == 0 or "peaceful".lower():
            mode = int(args[1] == 0)

        elif args[1] == 1 or "easy".lower():
            mode = int(args[1] == 1)


        elif args[1] == 2 or "medium".lower():
            mode = int(args[1] == 3)


        elif args[1] == 3 or "hard".lower():
            mode = int(args[1] == 4)

        else:
            sender.sendMessage(f"'{args[1]}' is not a valid parameter")
