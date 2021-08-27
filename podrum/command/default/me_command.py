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

class me_command:
    def __init__(self, server: object) -> None:
        self.server: object = server
        self.name: str = "me"
        self.description: str = "Displays a message about yourself."
    
    def execute(self, args: list, sender: object) -> None:
        if len(args) > 0:
            if getattr(sender, 'username', None) is None:
                sender.send_message("Cannot use this command as CONSOLE")
                return
            self.server.broadcast_message(f"* {sender.username} {' '.join(args)}")
        else:
            sender.send_message("/me <message: message>")
