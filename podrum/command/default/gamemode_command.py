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
from podrum.protocol.mcbe.type.gamemode_type import gamemode_type

class gamemode_command:
    def __init__(self, server: object) -> None:
        self.server: object = server
        self.name: str = "gamemode"
        self.description: str = "Sets a player's game mode."
    
    def execute(self, args: list, sender: object) -> None:
        if len(args) >= 1:
            player = sender
            if len(args) > 1:
                player = self.server.find_player(args[1])
                if not player:
                    sender.send_message("This player is not online")
                    return
            try:
                gamemode = int(args[0]) if int(args[0]) <= 2 else 4
            except ValueError:
                if hasattr(gamemode_type, args[0]):
                    gamemode = int(getattr(gamemode_type, args[0]))
                else:
                    sender.send_message(f"'{args[0]}' is an invalid gamemode.")
                    return
            if getattr(player, "username", None) is None:
                sender.send_message("Cannot change CONSOLE game mode.")
                return
            gamemode_name = list(gamemode_type.__dict__.keys())[gamemode + 2].capitalize()
            player.set_gamemode(gamemode)
            player.send_message(f"Your game mode has been updated to {gamemode_name}")
            sender.send_message(f"Set {player.username if player != sender else 'own'} game mode to {gamemode_name}")
        else:
            sender.send_message("/gamemode <gameMode: int> [player: target]")