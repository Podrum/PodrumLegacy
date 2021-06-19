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

from typing import Callable

class event_manager:
    def __init__(self) -> None:
        self.events: dict = {}

    def call_event(self, event_name: str, *args) -> None:
        if event_name in self.events:
            for event_entry in self.events[event_name]:
                event_entry(*args)

    def register_event(self, event_name: str, event_entry: Callable) -> None:
        if event_name in self.events:
            self.events[event_name].append(event_entry)
        else:
            self.events[event_name]: list = [event_entry]
                
    def remove_event(self, event_name: str) -> None:
        del self.events[event_name]
