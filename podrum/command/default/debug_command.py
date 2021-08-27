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

import os
import threading

class debug_command:
    def __init__(self, server: object) -> None:
        self.server: object = server
        self.name: str = "debug"
        self.description: str = "Debug command."
    
    def execute(self, args: list, sender: object) -> None:
        thread_count: int = threading.active_count()
        sender.send_message(f"There are {thread_count} active threads.")
