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

from binary_utils.binary_stream import binary_stream
from world.chunk.sub_chunk import sub_chunk
import xxhash

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
    
    def network_serialize_biomes(self) -> bytes:
        stream: object = binary_stream()
        for biome in self.biomes:
            stream.write_unsigned_byte(biome)
        return stream.data

    def network_serialize(self, cache_enabled: bool = False) -> bytes:
        stream: object = binary_stream()
        stream_2: object = binary_stream()
        stream.write_var_int(self.get_sub_chunk_send_count())
        stream.write_bool(cache_enabled)
        biomes_blob: bytes = self.network_serialize_biomes()
        if cache_enabled:
            stream.write_var_int(self.get_sub_chunk_send_count() + (1 if len(biomes_blob) > 0 else 0))
        for y in range(0, self.get_sub_chunk_send_count()):
            blob: bytes = self.sub_chunks[y].network_serialize()
            if cache_enabled:
                stream.write_unsigned_long_le(xxhash.xxh64(blob).intdigest())
            stream_2.write(blob)
        stream_2.write_var_int(len(self.biomes))
        if cache_enabled:
            if len(biomes_blob) > 0:
                stream.write_unsigned_long_le(xxhash.xxh64(biomes_blob).intdigest())
        stream_2.write(biomes_blob)
        stream_2.write_unsigned_byte(0)
        stream.write_var_int(len(stream_2.data))
        stream.write(stream_2.data)
        return stream.data
