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


class reload_command(Command):

    def __init__(self, server) -> None:
        self.server = server
        self.name: str = "reload"
        self.description: str = "Reloads all plugin."
    
    def execute(self, args: list, sender) -> None:
        sender.send_message("Reloading...")
        self.server.managers.plugin_manager.reload_all()
        sender.send_message("Successfully reloaded.")
