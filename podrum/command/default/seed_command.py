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


class seed_command(Command):

    def __init__(self, server) -> None:
        self.server = server
        self.name: str = "seed"
        self.description: str = "Displays the world seed."

    def execute(self, args: list, sender) -> None:
        sender.send_message(f"Seed: {self.server.config.data['seed']}")
