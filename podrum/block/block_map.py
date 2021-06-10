################################################################################
#                                                                              #
#  ____           _                                                            #
# |  _ \ ___   __| |_ __ _   _ _ __ ___                                        #
# | |_) / _ \ / _` | '__| | | | '_ ` _ \                                       #
# |  __/ (_) | (_| | |  | |_| | | | | | |                                      #
# |_|   \___/ \__,_|_|   \__,_|_| |_| |_|                                      #
#                                                                              #
# Copyright 2021 Podrum Studios                                                #
#                                                                              #
# Permission is hereby granted, free of charge, to any person                  #
# obtaining a copy of this software and associated documentation               #
# files (the "Software"), to deal in the Software without restriction,         #
# including without limitation the rights to use, copy, modify, merge,         #
# publish, distribute, sublicense, and/or sell copies of the Software,         #
# and to permit persons to whom the Software is furnished to do so,            #
# subject to the following conditions:                                         #
#                                                                              #
# The above copyright notice and this permission notice shall be included      #
# in all copies or substantial portions of the Software.                       #
#                                                                              #
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR   #
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,     #
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE  #
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER       #
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING      #
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS #
# IN THE SOFTWARE.                                                             #
#                                                                              #
################################################################################

from game_data.mcbe.block_ids_map import block_ids_map
from game_data.mcbe.block_states import block_states

class block_map:
    @staticmethod
    def load_map() -> None:
        block_map.states_1: dict = {}
        block_map.states_2: dict = {}
        legacy_meta: int = 0
        previous_state_name: str = ""
        for runtime_id, state in enumerate(block_states):
            if previous_state_name == state["name"]:
                legacy_meta += 1
            else:
                legacy_meta: int = 0
            previous_state_name: str = state["name"]
            legacy_id: int = block_ids_map[state["name"]]
            block_map.states_2[runtime_id]: tuple = (legacy_id, legacy_meta)
            block_map.states_1[f"{legacy_id} {legacy_meta}"]: int = runtime_id           
    
    @staticmethod
    def get_runtime_id(block_id: int, meta: int) -> int:
        return block_map.states_1[f"{block_id} {meta}"]
    
    @staticmethod
    def get_legacy_id(runtime_id: int) -> tuple:
        return block_map.states_2[runtime_id]
