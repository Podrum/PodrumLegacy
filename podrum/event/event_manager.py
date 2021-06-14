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

class event_manager:
    def __init__(self, server: object) -> None:
        self.server: object = server
        self.events: dict = {}

    def register(self, event: str, function: object) -> None:
        if event in self.events:
            self.events[event].append(function)
        else:
            self.events[event]: list = [function]

    def dispatch(self, event: str, *args) -> None:
        if event in self.events:
            for function in self.events[event]:
                function(*args, self.server)
