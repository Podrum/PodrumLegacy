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
from podrum.protocol.mcbe.type.difficulty_type import difficulty_type


class difficulty_command(Command):

    def __init__(self, server) -> None:
        self.server = server
        self.name: str = "difficulty"
        self.description: str = (
            "Sets the difficulty level (peaceful, easy, etc.)."
        )

    def execute(self, args: list, sender) -> None:
        if not args:
            difficulty = (
                list(difficulty_type.__dict__.keys())
                [sender.world.difficulty + 2].capitalize()
            )

            sender.send_message(f"The difficulty is {difficulty}")
            return

        try:
            difficulty = int(args[0]) if int(args[0]) <= 2 else 4

        except ValueError:
            if hasattr(difficulty_type, args[0].lower()):
                difficulty = int(getattr(difficulty_type, args[0].lower()))

            else:
                difficulty = 0

        difficulty_name = (
            list(difficulty_type.__dict__.keys())[difficulty + 2].capitalize()
        )

        sender.world.set_difficulty(difficulty)
        sender.send_message(
            f"The difficulty has been set to {difficulty_name}"
        )
