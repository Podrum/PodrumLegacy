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


class plugins_command(Command):

    def __init__(self, server) -> None:
        self.server = server
        self.name: str = "plugins"
        self.description: str = "Shows all server plugins."
        self.aliases: list = ["pl"]

    def execute(self, args: list, sender) -> None:
        n_plugins = len(self.server.managers.plugin_manager.plugins)

        sender.send_message(
            f"Plugins ({n_plugins}):"
            f" {', '.join(self.server.managers.plugin_manager.plugins)}"
        )
