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


class say_command(Command):

    def __init__(self, server) -> None:
        self.server = server
        self.name: str = "say"
        self.description: str = "Sends a message in the chat."

    def execute(self, args: list, sender) -> None:
        if not args:
            sender.send_message("/say <message: message>")
            return

        if hasattr(sender, "username"):
            sender.server.broadcast_message(
                f"[{sender.username}] {' '.join(args)}"
            )

        else:
            sender.send_chat_message(' '.join(args))
