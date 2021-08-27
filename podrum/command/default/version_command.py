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
from podrum.version import version


class version_command(Command):
    def __init__(self, server) -> None:
        self.server = server
        self.name: str = "version"
        self.description: str = "Shows server version and software."
        self.aliases: list = ["ver", "about"]

    def execute(self, args: list, sender) -> None:
        sender.send_message(
            f"This server is running Podrum version {version.podrum_version} "
            f"{version.podrum_codename} on API {version.podrum_api_version}. "
            f"This version is licensed under the"
            f" {version.podrum_license} license."
        )
