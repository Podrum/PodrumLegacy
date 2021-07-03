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

class provider_manager:
    def __init__(self):
        self.providers: dict = {}
    
    # [register_provider]
    # :return: = None
    # Registers a level provider
    def register_provider(self, provider: object) -> None:
        self.providers[provider.provider_name] = provider
    
    # [get_provider]
    # :return: = Provider
    # Gets a level provider
    def get_provider(self, provider_name: str) -> object:
        if provider_name in self.providers:
            return self.providers[provider_name]
    
    # [remove_provider]
    # :return: = None
    # Removes a level provider
    def remove_provider(self, provider_name: str) -> None:
        if provider_name in self.providers:
            del self.providers[provider_name]
