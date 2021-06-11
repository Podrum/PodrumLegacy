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

from world.provider.anvil.chunk import chunk
from world.provider.pm_anvil.section import section

class chunk(chunk):
    def __init__(self, x: int, z: int, sections: dict = {}, height_map: list = [], biomes: list = [], entities: list = [], tile_entities: list = []) -> None:
        self.x: int = x
        self.z: int = z
        self.sections: dict = {}
        for i in range(0, 16):
            if i in sections:
                self.sections[i]: object = sections[i]
            else:
                self.sections[i]: object = section()
        if len(height_map) == 256:
            self.height_map: list = height_map
        else:
            self.height_map: list = [0] * 256      
        if len(biomes) == 256:
            self.biomes: list = biomes
        else:
            self.biomes: list = [0] * 256
        self.entities: list = entities
        self.tile_entities: list = tile_entities
        self.light_populated: bool = False
        self.terrain_populated: bool = False
            
    def nbt_serialize(self) -> bytes:
        stream: object = nbt_be_binary_stream()
        self.recalculate_height_map()
        sections: list = list_tag("Sections", [], tag_ids.compound_tag)
        for i, sect in self.sections.items():
            sections.value.append(compound_tag("", [
                byte_array_tag("Blocks", sect.block_ids),
                byte_array_tag("Data", sect.data_entries),
                byte_array_tag("BlockLight", sect.block_light_entries),
                byte_array_tag("SkyLight", sect.sky_light_entries)
            ]))
        root_tag: object = compound("", [
            compound("Level", [
                int_tag("xPos", self.x),
                int_tag("zPos", self.z),
                long_tag("LastUpdate", 0),
                long_tag("InhabitedTime", 0),
                byte_tag("TerrainPopulated", 1 if self.terrain_populated else 0),
                byte_tag("LightPopulated", 1 if self.light_populated else 0),
                sections,
                byte_array_tag("Biomes", self.biomes),
                list_tag("Entities", self.entities, tag_ids.compound_tag),
                list_tag("TileEntities", self.tile_entities, tag_ids.compound_tag),
                int_array_tag("HeightMap", self.height_map)
            ]),
            int_tag("DataVersion", 1343)
        ])
        stream.write_root_tag(root_tag)
        return stream.data
    
    def nbt_deserialize(self, data: bytes) -> None:
        stream = nbt_be_binary_stream(data)
        root_tag: object = stream.read_root_tag()
        if not isinstance(root_tag, compound_tag):
            raise Exception("Invalid NBT data!")
        if not root_tag.has_tag("Level"):
            raise Exception("Level tag isnt present!")
        level_tag: object = root_tag.get_tag("Level")
        self.x: int = level_tag.get_tag("xPos").value
        self.z: int = level_tag.get_tag("zPos").value
        self.terrain_populated: bool = level_tag.get_tag("TerrainPopulated").value > 0
        if level_tag.has_tag("LightPopulated"):
            self.light_populated: bool = level_tag.get_tag("LightPopulated").value > 0
        else:
            self.light_populated: bool = False
        sections_tag: object = level_tag.get_tag("Sections")
        for section_tag in sections_tag.value:
            self.sections[section_tag.get_tag("Y").value]: object = section(
                section_tag.get_tag("Blocks").value,
                section_tag.get_tag("Data").value,
                section_tag.get_tag("BlockLight").value,
                section_tag.get_tag("SkyLight").value
            )
        if level_tag.has_tag("Biomes"):
            self.biomes: list = level_tag.get_tag("Biomes").value
        self.entities: list = level_tag.get_tag("Entities").value
        self.tile_entities: list = level_tag.get_tag("TileEntities").value
        self.height_map: list = level_tag.get_tag("HeightMap").value
