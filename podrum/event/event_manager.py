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
    events: dict = {}
  
    @staticmethod
    def register_listener(event: object, listener: Callable) -> None:
        event_manager.events[event.__name__].append(listener)
        
    @staticmethod
    def remove_listener(event: object, listener: Callable) -> None:
        event_manager.events[event.__name__].remove(listener)
        
    @staticmethod
    def get_listeners(event: object) -> list:
        return event_manager.events[event.__name__]
    
    @staticmethod
    def register_event(event: object) -> None:
        event_manager.events[event.__name__] = []
        
    @staticmethod
    def remove_event(event: object) -> None:
        del event_manager.events[event.__name__]
