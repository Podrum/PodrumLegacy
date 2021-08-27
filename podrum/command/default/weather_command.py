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

import random
from podrum.command.command_abc import Command


class weather_command(Command):

    def __init__(self, server) -> None:
        self.server = server
        self.name: str = "weather"
        self.description: str = "Sets the weather."

    def execute(self, args: list, sender) -> None:
        if not args:
            sender.send_message("/weather <clear|rain|thunder> [duration: int]")
            return

        weather = args[0]
        try:
            dur = int(args[0])

        except ValueError:
            dur = random.randint(90000, 110000)

        if weather.lower() == "rain":
            sender.world.set_raining(True, dur)
            sender.send_message("Changing to rainy weather")

        elif weather.lower() == "thunder":
            sender.world.set_thundering(True, dur)
            sender.world.set_raining(True, dur)
            sender.send_message("Changing to rain and thunder")

        elif weather.lower() == "clear":
            sender.world.set_raining(False, dur)
            sender.world.set_thundering(False, dur)
            sender.send_message("Changing to clear weather")

        elif weather.lower() == "query":
            if sender.world.thundering:
                w_state = 'thunder'

            elif sender.world.raining:
                w_state = 'rain'

            else:
                w_state = 'clear'

            sender.send_message(
                f"Weather state is: "
                f"{w_state}"
            )

        else:
            sender.send_message("/weather <clear|rain|thunder> [duration: int]")
