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

from nbt_utils.tag.compound_tag import compound_tag

class chunk:
    def __init__(self, x: int, z: int, sections: dict = {}, height_map: list = [], biomes: list = [], entities: object = compound_tag("Entities"), tile_entities: object = compound_tag("TileEntities")) -> None:
        self.x: int = x
        self.z: int = z
        self.sections: dict = {}
        for i in range(0, 16):
            if i in sections:
                self.sections[i]: object = sections[i]
            else:
                self.sections[i]: object = None
        if len(height_map) == 256;
            self.height_map: list = height_map
        else:
            self.height_map: list = [0] * 256      
        if len(biomes) == 256;
            self.biomes: list = biomes
        else:
            self.biomes: list = [0] * 256
        self.light_populated: bool = False
        self.terrain_populated: bool = False
        
    def get_block_id(self, x: int, y: int, z: int) -> int:
        return self.sections[y >> 4].get_block_id(x & 0x0f, y & 0x0f, z & 0x0f)
        
    def set_block_id(self, x: int, y: int, z: int, block_id: int) -> None:
        self.sections[y >> 4].set_block_id(x & 0x0f, y & 0x0f, z & 0x0f, block_id)
        
    def get_data(self, x: int, y: int, z: int) -> int:
        return self.sections[y >> 4].get_data(x & 0x0f, y & 0x0f, z & 0x0f)
        
    def set_data(self, x: int, y: int, z: int, data: int) -> None:
        self.sections[y >> 4].set_data(x & 0x0f, y & 0x0f, z & 0x0f, data)
        
    def get_block_light(self, x: int, y: int, z: int) -> int:
        return self.sections[y >> 4].get_block_light(x & 0x0f, y & 0x0f, z & 0x0f)
        
    def set_block_light(self, x: int, y: int, z: int, light_level: int) -> None:
        self.sections[y >> 4].set_block_light(x & 0x0f, y & 0x0f, z & 0x0f, light_level)
        
    def get_sky_light(self, x: int, y: int, z: int) -> int:
        return self.sections[y >> 4].get_sky_light(x & 0x0f, y & 0x0f, z & 0x0f)
        
    def set_sky_light(self, x: int, y: int, z: int, light_level: int) -> None:
        self.sections[y >> 4].set_sky_light(x & 0x0f, y & 0x0f, z & 0x0f, light_level)
        
    def get_highest_block_at(self, x: int, z: int) -> int:
        for i in range(len(self.sections) - 1, -1, -1):
            section_to_check: object = self.sections[i]
            if section_to_check is not None:
                index: int = section_to_check.get_highest_block_at(x & 0x0f, z & 0x0f)
                if index != -1:
                    return index + (i << 4)
        return -1
    
    def recalculate_height_map(self) -> None:
        for x in range(0, 16):
            for z in range(0, 16):
                self.height_map[(x << 4) + z]: int = get_highest_block_at(x, z) + 1
