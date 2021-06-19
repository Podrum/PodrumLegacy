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

from server import server

class default_events:
    @staticmethod
    def execute_command_event(user_input: str, sender: object, command_manager: object) -> None:
        if len(user_input) > 0:
            split_input: list = user_input.split()
            command_name: str = split_input[0]
            command_args: list = split_input[1:]
            if command_manager.has_command(command_name):
                command_manager.execute(command_name, command_args, sender)
            else:
                if isinstace(sender, server):
                    sender.logger.error("Invalid command!")
                else:
                    sender.send_message("Invalid command!")
