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

from threading import Thread

class command_interface(Thread):
    def __init__(self, server: object) -> None:
        super().__init__()
        self.server: object = server

    def dispatch(self, user_input: str) -> None:
        if len(user_input) > 0:
            raw_command: list = user_input.split()
            command_name: str = raw_command[0]
            command_args: list = raw_command[1:]
            commands: dict = self.server.command_manager.commands
            if self.server.command_manager.has_command(command_name):
                self.server.command_manager.execute(command_name, command_args, self.server)
            else:
                self.server.logger.error("Invalid command!")

    def start_interface(self) -> None:
        self.stopped: bool = False
        self.start()

    def stop_interface(self) -> None:
        self.stopped: bool = True

    def run(self) -> None:
        while not self.stopped:
            self.dispatch(input())
