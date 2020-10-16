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

class DifficultyCommand(Command):
    def __init__(self, name = "", description = ""):
        super().__init__("difficulty", "Difficulty Command")

    def execute(self, sender, args):
        try:
            args[1]
        except:
            sender.sendMessage("difficulty <difficulty>")
        else:
            if args[1] == "0" or args[1].lower() == "peaceful":
                pass
            elif args[1] == "1" or args[1].lower() == "easy":
                pass
            elif args[1] == "2" or args[1].lower() == "normal":
               pass
            elif args[1] == "3" or args[1].lower() == "hard":
                pass
            else:
                sender.sendMessage("Invalid argument!")
