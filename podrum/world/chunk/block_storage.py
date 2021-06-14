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

from block.default.air import air
import math

class block_storage:
    def __init__(self, blocks: list = [], palette: list = []) -> None:
        if len(palette) > 0:
            self.palette: list = palette
        else:
            self.palette: list = [air().runtime_id]
        if len(blocks) == 4096:
            self.blocks: list = blocks
        else:
            self.blocks: list = [0] * 4096
           
    @staticmethod
    def get_index(x: int, y: int, z: int) -> int:
        return (x << 8) + (z << 4) + y
    
    @staticmethod
    def check_bounds(x: int, y: int, z: int) -> None:
        assert x >= 0 and x < 16, f"x ({x}) is not between 0 and 15"
        assert y >= 0 and y < 16, f"y ({y}) is not between 0 and 15"
        assert z >= 0 and z < 16, f"z ({z}) is not between 0 and 15"
    
    def get_block_runtime_id(self, x, y, z) -> int:
        block_storage.check_bounds(x, y, z)
        palette_index: int = self.blocks[block_storage.get_index(x, y, z)]
        return self.palette[palette_index]
    
    def set_block_runtime_id(self, x, y, z, runtime_id: int) -> None:
        block_storage.check_bounds(x, y, z)
        if runtime_id not in self.palette:
            self.palette.append(runtime_id)
        self.blocks[block_storage.get_index(x, y, z)]: int = self.palette.index(runtime_id)
            
    def get_highest_block_at(self, x: int, z: int) -> int:
        block_storage.check_bounds(x, 15, z)
        for y in range(15, -1, -1):
            index: int = block_storage.get_index(x, y, z)
            palette_index: int = self.blocks[index]
            runtime_id: int = self.palette[palette_index]
            if runtime_id != air().runtime_id:
                return y
        return -1

    def network_serialize(self, stream: object):
        bits_per_block: int = math.ceil(math.log2(len(self.palette)))
        if bits_per_block == 0:
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
                if pos >= 4096:
                    break
                state: int = self.blocks[pos]
                word |= state << (bits_per_block * block)
                pos += 1
            stream.write_unsigned_int_le(word)
        stream.write_signed_var_int(len(self.palette))
        for runtime_id in self.palette:
            stream.write_signed_var_int(runtime_id)
