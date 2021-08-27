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
from podrum.protocol.mcbe.type.time_type import time_type

class time_command:
    def __init__(self, server: object) -> None:
        self.server: object = server
        self.name: str = "time"
        self.description: str = "Changes or queries the world's game time."
    
    def execute(self, args: list, sender: object) -> None:
        if args:
            if len(args) > 1:
                try:
                    time = int(args[1])
                except ValueError:
                    time = int(getattr(time_type, args[1])) if hasattr(time_type, args[1]) else 0
                if args[0].lower() == "set":
                    sender.world.set_time(time)
                    sender.send_message(f"Set the time to {time}")
                    return
                elif args[0].lower() == "add":
                    sender.world.set_time(sender.world.time + time)
                    sender.send_message(f"Added {time} to the time")
                    return
            elif args[0].lower() == "query":
                sender.send_message(f"Time is {sender.world.time}")
                return
        sender.send_message("/time <add|query|set> <amount: int>")