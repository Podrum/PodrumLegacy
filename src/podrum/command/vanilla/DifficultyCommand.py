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

from podrum.command.Command import Command

class DifficultyCommand(Command):
    def __init__(self, name = "", description = ""):
        super().__init__("difficulty", "Difficulty Command")

    def execute(self, sender, args):
        if len(args) == 2:
            if args[1] == "0" or args[1].lower() == "peaceful":
                pass
            elif args[1] == "1" or args[1].lower() == "easy":
                pass
            elif args[1] == "2" or args[1].lower() == "normal":
               pass
            elif args[1] == "3" or args[1].lower() == "hard":
                pass
            else:
                sender.sendMessage(f"{args[1]} is not a valid parameter!")
        else:
            sender.sendMessage("difficulty <difficulty>")
