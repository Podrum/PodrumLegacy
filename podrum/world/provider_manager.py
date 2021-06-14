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
        self._providers: dict = {}
          
    def register_provider(self, provider: object) -> None:
        self._providers[provider.provider_name]: object = provider
          
    def get_provider(self, provider_name: str) -> object:
        return self._providers[provider_name]
      
    def remove_provider(self, provider_name: str) -> None:
        del self._providers[provider_name]
