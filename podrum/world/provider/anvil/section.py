r"""
  ____           _
 |  _ \ ___   __| |_ __ _   _ _ __ ___
 | |_) / _ \ / _` | '__| | | | '_ ` _ \
 |  __/ (_) | (_| | |  | |_| | | | | | |
 |_|   \___/ \__,_|_|   \__,_|_| |_| |_|

 Copyright 2021 Podrum Team.

 This file is licensed under the GPL v2.0 license.
 The license file is located in the root directory
 of the source code. If not you may not use this file.
"""

from podrum.world.chunk_utils import chunk_utils

class section:
    def __init__(self, block_ids: list = [], data_entries: list = [], block_light_entries: list = [], sky_light_entries: list = []) -> None:
        if len(block_ids) == 4096:
            self.block_ids: list = block_ids
        else:
            self.block_ids: list = [0] * 4096
        if len(data_entries) == 2048:
            self.data_entries: list = data_entries
        else:
            self.data_entries: list = [0] * 2048
        if len(block_light_entries) == 2048:
            self.block_light_entries: list = block_light_entries
        else:
            self.block_light_entries: list = [0] * 2048
        if len(sky_light_entries) == 2048:
            self.sky_light_entries: list = sky_light_entries
        else:
            self.sky_light_entries: list = [-1] * 2048
            
    @staticmethod
    def get_index(x: int, y: int, z: int) -> int:
        return (y << 8) + (z << 4) + x
      
    @staticmethod
    def check_bounds(x: int, y: int, z: int) -> None:
        assert x >= 0 and x < 16, f"x ({x}) is not between 0 and 15"
        assert y >= 0 and y < 16, f"y ({y}) is not between 0 and 15"
        assert z >= 0 and z < 16, f"z ({z}) is not between 0 and 15"
              
    def get_block_id(self, x: int, y: int, z: int) -> int:
        return self.block_ids[section.get_index(x, y, z)]
        
    def set_block_id(self, x: int, y: int, z: int, block_id: int) -> None:
        self.block_ids[section.get_index(x, y, z)] = block_id
        
    def get_data(self, x: int, y: int, z: int) -> int:
        return chunk_utils.get_nibble_4(self.data_entries, section.get_index(x, y, z))
        
    def set_data(self, x: int, y: int, z: int, data: int) -> None:
        chunk_utils.set_nibble_4(self.data_entries, section.get_index(x, y, z), data)
        
    def get_block_light(self, x: int, y: int, z: int) -> int:
        return chunk_utils.get_nibble_4(self.block_light_entries, section.get_index(x, y, z))
        
    def set_block_light(self, x: int, y: int, z: int, light_level: int) -> None:
        chunk_utils.set_nibble_4(self.block_light_entries, section.get_index(x, y, z), light_level)
        
    def get_sky_light(self, x: int, y: int, z: int) -> int:
        return chunk_utils.get_nibble_4(self.sky_light_entries, section.get_index(x, y, z))
        
    def set_sky_light(self, x: int, y: int, z: int, light_level: int) -> None:
        chunk_utils.set_nibble_4(self.sky_light_entries, section.get_index(x, y, z), light_level)
        
    def get_highest_block_at(self, x: int, z: int) -> int:
        section.check_bounds(x, 15, z)
        for y in range(15, -1, -1):
            if self.get_block_id(x, y, z) != 0:
                return y
        return -1
