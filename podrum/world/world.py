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

class world:
    def __init__(self, provider: object, server: object):
        self.provider: object = provider
        self.server: object = server
        self.chunks: dict = {}
            
    def load_chunk(self, x: int, z: int) -> None:
        self.chunks[f"{x} {z}"]: object = self.provider.get_chunk(x, z)
            
    def unload_chunk(self, x: int, z: int) -> None:
        self.provider.save_chunk(x, z)
        del self.chunks[f"{x} {z}"]
            
    def get_chunk(self, x: int, z: int) -> object:
        return self.chunks[f"{x} {z}"]
        
    def save_chunk(self, x: int, z: int) -> None:
        self.provider.set_chunk(self.get_chunk(x, z))
        
    def get_block(self, x: int, y: int, z: int, block: object) -> None:
        return self.chunks[f"{x >> 4} {z >> 4}"].get_block_runtime_id(x & 0x0f, y & 0x0f, z & 0x0f)
        
    def set_block(self, x: int, y: int, z: int, block: object) -> None:
        self.chunks[f"{x >> 4} {z >> 4}"].set_block_runtime_id(x & 0x0f, y & 0x0f, z & 0x0f, block.runtime_id)
        
    def get_highest_block_at(self, x: int, z: int) -> int:
        return self.chunks[f"{x >> 4} {z >> 4}"].get_highest_block_at(x & 0x0f, z & 0x0f)
        
    def save(self) -> None:
        for chunk in self.chunks.values():
            self.save_chunk(chunk)
            
    def get_world_name(self) -> str:
        return self.provider.get_world_name()
        
    def set_world_name(self, world_name: str) -> None:
        self.provider.set_world_name(world_name)
        
    def get_spawn_position(self) -> object:
        return self.provider.get_spawn_position()
        
    def set_spawn_position(self, world_name: object) -> None:
        self.provider.set_spawn_position(world_name)
        
    def get_world_gamemode(self) -> str:
        return self.provider.get_world_gamemode()
        
    def set_world_gamemode(self, world_name: str) -> None:
        self.provider.set_world_gamemode(world_name)
        
    def get_player_position(self, uuid: str) -> object:
        return self.provider.get_player_position(uuid)
        
    def set_player_position(self, uuid: str, position: object) -> None:
        self.provider.set_player_position(uuid, position)

    def get_player_gamemode(self, uuid: str) -> int:
        return self.provider.get_player_gamemode(uuid)
        
    def set_player_gamemode(self, uuid: str, gamemode: int) -> None:
        self.provider.set_player_gamemode(uuid, gamemode)
        
    def create_player(self, uuid: str) -> None:
        self.provider.create_player_file(uuid)
        
    def has_player(self, uuid: str) -> bool:
        self.provider.has_player_file(uuid)
