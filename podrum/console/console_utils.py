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
import platform
import sys

if platform.system() == "Windows":
    import msvcrt
else:
    import fcntl

class console_utils:
    @staticmethod
    async def ainput() -> object:
        if platform.system() != "Windows":
            fcntl.fcntl(sys.stdin, fcntl.F_SETFL, fcntl.fcntl(sys.stdin, fcntl.F_GETFL) | os.O_NONBLOCK)
        out: object = asyncio.Future()
        result: str = ""
        while True:
            if platform.system() == "Windows":
                if msvcrt.kbhit():
                    user_input: str = msvcrt.getch().decode()
                    if user_input == "\b":
                        result = result[0:-1]
                    else:
                        result += user_input
                    if user_input == "\r":
                        print("")
                    else:
                        print("\r\x1b[K" + result, end = "")
                    if result.endswith("\r"):
                        command: str = result[:-1]
                        break
                else:
                    await asyncio.sleep(0.0001)
            else:
                user_input: str = sys.stdin.read(1)
                if len(user_input) > 0:
                    result += user_input
                    if result.endswith("\n"):
                        command: str = result[:-1]
                        break
                else:
                    await asyncio.sleep(0.0001)
        out.set_result(result)
        return out
