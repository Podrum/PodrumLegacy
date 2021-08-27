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

class kick_command:
    def __init__(self, server: object) -> None:
        self.server: object = server
        self.name: str = "kick"
        self.description: str = "Kicks a player off the server."
    
    def execute(self, args: list, sender: object) -> None:
        if args:
            player = self.server.find_player(args[0])
            if not self.server.find_player(args[0]):
                sender.send_message("This player is not online")
                return
            args.remove(args[0])
            if sender in self.server.players.values():
                player.disconnect(f"Kicked by {sender.username}{': ' if args else ''}{' '.join(args)}")
            else:
                player.disconnect(f"Kicked by Console{': ' if args else ''}{' '.join(args)}")
            sender.send_message(f"Kicked {player.username}.")
        else:
            sender.send_message("/kick <name: target> [reason: message]")