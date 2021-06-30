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

from nbt_utils.tag.compound_tag import compound_tag

class item_extra:
    def __init__(self, nbt: object = compound_tag(), can_place_on: list = [], can_break: list = [], blocking_tick: int = None) -> None:
        self.nbt: object = nbt
        self.can_place_on: list = can_place_on
        self.can_break: list = can_break
        self.blocking_tick: int = blocking_tick
          
    def prepare_for_network(self) -> dict:
        result: dict = {}
        if self.nbt.name != "" and len(self.nbt.value) > 0:
            result["has_nbt"] = True
            result["version"] = 1
            result["nbt"] = self.nbt
        else:
            result["has_nbt"] = False
        result["can_place_on"] = self.can_place_on
        result["can_break"] = self.can_break
        if self.blocking_tick is not None:
            result["blocking_tick"] = self.blocking_tick
