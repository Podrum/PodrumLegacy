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

    def start_interface(self) -> None:
        self.stopped: bool = False
        self.start()

    def stop_interface(self) -> None:
        self.stopped: bool = True

    def run(self) -> None:
        while not self.stopped:
            self.server.managers.event_manager.call_event("execute_command", input(), self.server, self.server.managers.command_manager)
