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

import asyncio
import fcntl
import os
import sys

class async_tasks:
    def __init__(self, server: object) -> None:
        self.server: object = server
          
    async def input_task(self) -> None:
        orig_fl = fcntl.fcntl(sys.stdin, fcntl.F_GETFL)
        fcntl.fcntl(sys.stdin, fcntl.F_SETFL, orig_fl | os.O_NONBLOCK)
        result: str = ""
        while True:
            result += sys.stdin.read(1)
            if result.endswith("\n"):
                command: str = result[:-1]
                self.server.managers.event_manager.call_event("execute_command", command, self.server, self.server.managers.command_manager)
                result: str = ""
            await asyncio.sleep(0.0001)
