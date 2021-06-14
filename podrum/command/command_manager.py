#########################################################                        
#  ____           _                                     #
# |  _ \ ___   __| |_ __ _   _ _ __ ___                 #
# | |_) / _ \ / _` | '__| | | | '_ ` _ \                #
# |  __/ (_) | (_| | |  | |_| | | | | | |               #
# |_|   \___/ \__,_|_|   \__,_|_| |_| |_|               #
#                                                       #
# Copyright 2021 Podrum Team.                           #
#                                                       #
# This file is licensed under the GPL v2.0 license.     #
# The license file is located in the root directory     #
# of the source code. If not you may not use this file. #
#                                                       #
#########################################################

class command_manager:
    def __init__(self) -> None:
        self.commands: list = []

    def register(self, command: object) -> None:
        self.commands.append(command)
        
    def has_command(self, name: str) -> bool:
        for command in self.commands:
            if command.name == name:
                return True
            if hasattr(command, "aliases"):
                for alias in command.aliases:
                    if alias == name:
                        return True
        return False

    def execute(self, name: str, args: list, sender: object) -> None:
        for command in self.commands:
            if command.name == name:
                command.execute(args, sender)
                break
            if hasattr(command, "aliases"):
                for alias in command.aliases:
                    if alias == name:
                        command.execute(args, sender)
                        break
