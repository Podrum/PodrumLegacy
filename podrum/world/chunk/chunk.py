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
                    
    def get_height(self) -> int:
        return len(self.sub_chunks)
    
    def get_highest_empty_sub_chunk_count(self) -> int:
        count: int = 0
        for i in range(15, -1, -1):
            if self.sub_chunks[i].is_empty():
                count += 1
        return count
    
    def get_sub_chunk(self, y: int) -> object:
        index: int = y >> 4
        if index not in self.sub_chunks:
            raise Exception("Invalid height")
        else:
            return self.sub_chunks[index]
        
    def get_block(self, x: int, y: int, z: int, layer: int = 0) -> tuple:
        return self.get_sub_chunk(y).get_block(x, y, z, layer)
    
    def set_block(self, x: int, y: int, z: int, block_id: int, meta: int, layer: int = 0) -> None:
        self.get_sub_chunk(y).set_block(x, y, z, block_id, meta, layer)

    def network_serialize(self) -> object:
        stream: object = binary_stream()
        sub_chunk_count: int = len(self.sub_chunks) - self.get_highest_empty_sub_chunk_count()
        for y in range(0, sub_chunk_count):
            self.sub_chunks[y].network_serialize(stream)
        stream.write_unsigned_byte(len(self.biomes))
        for biome in self.biomes:
            stream.write_unsigned_byte(biome)
        stream.write_unsigned_byte(0)
        return stream
