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

from game_data.mcbe.block_states import block_states

class block_map:
    def __init__(self) -> None:
        self.states: dict = {}
        for runtime_id, state in enumerate(block_states):
            block_name: str = self.states[state["block"]["name"]]
            if block_name not in self.states:
                self.states[block_name]: dict = {}
            if "LegacyStates" in state:
                for legacy_state in state["LegacyStates"]:
                    
                    self.register_block(legacy_state["id"], legacy_state["val"], runtime_id)
                      
    @staticmethod
    def hash_legacy_id(block_id: int, meta: int) -> int:
        return 
                
    def register_block(self, block_id: int, meta: int, runtime_id: int) -> None:
        self.legacy_to_runtime_ids[(block_id << 4) | meta]: int = runtime_id
    
    def legacy_to_runtime_id(self, block_id: int, meta: int) -> int:
        return self.legacy_to_runtime_ids[block_map.hash_legacy_id(block_id, meta)]
