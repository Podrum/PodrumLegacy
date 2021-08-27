r"""
  ____           _
 |  _ \ ___   __| |_ __ _   _ _ __ ___
 | |_) / _ \ / _` | '__| | | | '_ ` _ \
 |  __/ (_) | (_| | |  | |_| | | | | | |
 |_|   \___/ \__,_|_|   \__,_|_| |_| |_|

 Copyright 2021 Podrum Team.

 This file is licensed under the GPL v2.0 license.
 The license file is located in the root directory
 of the source code. If not you may not use this file.
"""
from podrum.command.command_abc import Command


class tell_command(Command):

    def __init__(self, server) -> None:
        self.server = server
        self.name: str = "tell"
        self.description: str = "Sends a private message to another player."
        self.aliases: list = ['msg', 'w']

    def execute(self, args: list, sender) -> None:
        if len(args) <= 1:
            sender.send_message("/tell <target: target> <message: message>")
            return

        if not self.server.find_player(args[0]):
            sender.send_message("This player is not online")
            return

        player = self.server.find_player(args[0])
        player_name = player.username

        if getattr(sender, 'username', None) == player_name:
            sender.send_message("You can not message yourself")
            return

        args.pop(0)

        name = (
            sender.username
            if sender in self.server.players.values() else "Server"
        )

        d_args = " ".join(args)

        sender.send_message(f"[{name} -> {player_name}] {d_args}")
        player.send_message(f"[{name} -> {player_name}] {d_args}")
