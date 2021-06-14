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

from game_data.mcbe.block_states import block_states

class block_map:
    @staticmethod
    def load_map() -> None:
        block_map.states_1: dict = {}
        block_map.states_2: dict = {}
        meta: int = 0
        previous_state_name: str = ""
        for runtime_id, state in enumerate(block_states):
            if previous_state_name == state["name"]:
                meta += 1
            else:
                meta: int = 0
            previous_state_name: str = state["name"]
            block_map.states_2[runtime_id]: tuple = (state["name"], meta)
            block_map.states_1[f"""{state["name"]} {meta}"""]: int = runtime_id           
    
    @staticmethod
    def get_runtime_id(block_name: str, meta: int) -> int:
        return block_map.states_1[f"{block_name} {meta}"]
    
    @staticmethod
    def get_name_and_meta(runtime_id: int) -> tuple:
        return block_map.states_2[runtime_id]
