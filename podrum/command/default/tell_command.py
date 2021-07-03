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

class tell_command:
    def __init__(self, server: object) -> None:
        self.server: object = server
        self.name: str = "tell"
        self.description: str = "tell command"
    
    def execute(self, args: list, sender: object) -> None:
        if len(args) > 1:
            if not self.server.find_player(args[0]):
                sender.send_message("This player is not online")
                return
            player = self.server.find_player(args[0])
            player_name = player.username
            args.remove(args[0])
            if sender in self.server.players.values():
                if sender.username == player_name:
                    sender.send_message("You can not message yourself")
                    return
                sender.send_message(f"[" + sender.username + " -> " + player_name + "] " + " ".join(args))
                player.send_message(f"[" + sender.username + " -> " + player_name + "] " + " ".join(args))
            else:
                sender.send_message(f"[Server -> " + player_name + "] " + " ".join(args))
                player.send_message(f"[Server -> " + player_name + "] " + " ".join(args))
        else:
            sender.send_message("tell <player> <message>")
