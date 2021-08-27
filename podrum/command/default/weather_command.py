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
import random

class weather_command:
    def __init__(self, server: object) -> None:
        self.server: object = server
        self.name: str = "weather"
        self.description: str = "Sets the weather."
    
    def execute(self, args: list, sender: object) -> None:
        if args:
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
                sender.send_message(f"Weather state is: "
                                    f"{'clear' if not sender.world.raining and not sender.world.thundering else 'thunder' if sender.world.thundering else 'rain'}")
            else:
                sender.send_message("/weather <clear|rain|thunder> [duration: int]")
                return
        else:
            sender.send_message("/weather <clear|rain|thunder> [duration: int]")