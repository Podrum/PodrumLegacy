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

class generator_manager:
    def __init__(self):
        self.generators: dict = {}
          
    def register_generator(self, generator: object) -> None:
        self.generators[generator.generator_name]: object = generator
          
    def get_generator(self, generator_name: str) -> object:
        if generator_name in self.generators:
            return self.generators[generator_name]
      
    def remove_generator(self, generator_name: str) -> None:
        if generator_name in self.generators:
            del self.generators[generator_name]
