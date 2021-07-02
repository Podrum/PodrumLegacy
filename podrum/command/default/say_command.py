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

class say_command:
    def __init__(self, server: object) -> None:
        self.server: object = server
        self.name: str = "say"
        self.description: str = "say command"
    
    def execute(self, args: list, sender: object) -> None:
        if len(args) > 0:
            sender.send_chat_message(" ".join(args))
        else:
            sender.send_message("say <message>")
