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

import threading
import tracemalloc

class debug_command:
    def __init__(self, server: object) -> None:
        self.server: object = server
        self.name: str = "debug"
        self.description: str = "debug command"
    
    def execute(self, args: list, sender: object) -> None:
        thread_count: int = threading.active_count()
        if thread_count > 1:
            sender.send_message(f"Threre are {thread_count} active threads.")
        else:
            sender.send_message(f"Threre are {thread_count} active threads.")
        memory_usage: tuple = tracemalloc.get_traced_memory()
        sender.send_message(f"Threre are {'%.2f' % (memory_usage[0] / 10**6)}mb ram in use.")
