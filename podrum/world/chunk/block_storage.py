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

from block.block_map import block_map
import math

class block_storage:
    block_map: object = block_map()
  
    def __init__(self, blocks: list = [], palette: list = []) -> None:
        if len(palette) > 0:
            self.palette: list = palette
        else:
            self.palette: list = [block_storage.block_map.legacy_to_runtime_id(0, 0)]
        if len(blocks) == 4096:
            self.blocks: list = blocks
        else:
            self.blocks: list = [0] * 4096
           
    @staticmethod
    def get_index(x: int, y: int, z: int) -> int:
        return (((x & 0x0f) << 8) + ((z & 0x0f) << 4)) | (y & 0x0f)
    
    def get_block(self, x, y, z) -> tuple:
        palette_index: int = self.blocks[block_storage.get_index(x, y, z)]
        runtime_id: int = self.palette[palette_index]
        return block_storage.block_map.runtime_to_legacy_id(runtime_id)
    
    def set_block(self, x, y, z, block: int, meta: int) -> None:
        runtime_id: int = block_storage.block_map.legacy_to_runtime_id(block, meta)
        if runtime_id not in self.palette:
            self.palette.append(runtime_id)
        self.blocks[block_storage.get_index(x, y, z)]: int = self.palette.index(runtime_id)

    def network_serialize(self, stream: object, force: bool = False):
        bits_per_block: int = math.ceil(math.log2(len(self.palette)))
        if bits_per_block == 0:
            if not force:
                return
            bits_per_block: int = 1
        elif bits_per_block == 7:
            bits_per_block: int = 8
        elif bits_per_block > 8:
            bits_per_block: int = 16
        stream.write_unsigned_byte((bits_per_block << 1) | 1)
        blocks_per_word: int = math.floor(32 / bits_per_block)
        words_per_chunk: int = math.ceil(4096 / blocks_per_word)
        pos: int = 0
        for chunk in range(0, words_per_chunk):
            word: int = 0
            for block in range(0, blocks_per_word):
                state: int = self.blocks[pos]
                word |= state << (bits_per_block * block)
                pos += 1
            stream.write_int_le(word)
        stream.write_signed_var_int(len(self.palette))
        for runtime_id in self.palette:
            stream.write_signed_var_int(runtime_id)
