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


class list_command(Command):

    def __init__(self, server) -> None:
        self.server = server
        self.name: str = "list"
        self.description: str = "Lists players on the server."

    def execute(self, args: list, sender) -> None:
        online_players = len(self.server.players.values())
        max_players = self.server.config.data['max_players']

        sender.send_message(
            f"There are {online_players}/{max_players} players online: "
            f"\n{', '.join(p.username for p in self.server.players.values())}"
        )
