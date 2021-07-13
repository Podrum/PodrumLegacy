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

from podrum.game_data.mcbe.item_states import item_states

class item_map:
    @staticmethod
    def load_map() -> None:
        item_map.states_1: dict = {}
        item_map.states_2: dict = {}
        for state in item_states:
            item_map.states_1[state["name"]] = state["runtime_id"]
            item_map.states_2[state["runtime_id"]] = state["name"]
            
    @staticmethod
    def name_to_runtime_id(name: str) -> None:
        return item_map.states_1[name]
      
    @staticmethod
    def runtime_id_to_name(runtime_id: id) -> None:
        return item_map.states_2[runtime_id]
