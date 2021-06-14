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

from binary_utils.binary_stream import binary_stream
from world.chunk.sub_chunk import sub_chunk

class chunk:
    def __init__(self, x: int, z: int, sub_chunks: dict = {}, biomes: list = []) -> None:
        self.x: int = x
        self.z: int = z
        self.has_changed: bool = False
        self.sub_chunks: dict = {}
        for y in range(0, 16):
            if y in self.sub_chunks:
                self.sub_chunks[y]: object = sub_chunks[y]
            else:
                self.sub_chunks[y]: object = sub_chunk()
        if len(biomes) == 256:
            self.biomes: list = biomes
        else:
            self.biomes: list = [0] * 256
    
    def get_sub_chunk_send_count(self) -> int:
        top_empty: int = 16
        for i in range(0, 16 + 1):
            if self.sub_chunks[i].is_empty():
                top_empty: int = i
            else:
                break
        return top_empty
        
    def get_block_runtime_id(self, x: int, y: int, z: int, layer: int = 0) -> int:
        return self.sub_chunks[y >> 4].get_block_runtime_id(x & 0x0f, y & 0x0f, z & 0x0f, layer)
    
    def set_block_runtime_id(self, x: int, y: int, z: int, runtime_id: int, layer: int = 0) -> None:
        self.sub_chunks[y >> 4].set_block_runtime_id(x & 0x0f, y & 0x0f, z & 0x0f, runtime_id, layer)
        self.has_changed: bool = True
            
    def get_highest_block_at(self, x: int, z: int, layer: int = 0) -> int:
        for i in range(15, -1, -1):
            index: int = self.sub_chunks[i].get_highest_block_at(x & 0x0f, z & 0x0f, layer)
            if index != -1:
                return index + (i << 4)
        return -1

    def network_serialize(self) -> object:
        stream: object = binary_stream()
        for y in range(0, self.get_sub_chunk_send_count()):
            self.sub_chunks[y].network_serialize(stream)
        stream.write_var_int(len(self.biomes))
        for biome in self.biomes:
            stream.write_unsigned_byte(biome)
        stream.write_unsigned_byte(0)
        return stream.data
