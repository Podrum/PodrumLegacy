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

import gzip
from block.block_map import block_map
from nbt_utils.constant.tag_ids import tag_ids
from nbt_utils.tag.byte_tag import byte_tag
from nbt_utils.tag.byte_array_tag import byte_array_tag
from nbt_utils.tag.compound_tag import compound_tag
from nbt_utils.tag.int_tag import int_tag
from nbt_utils.tag.int_array_tag import int_array_tag
from nbt_utils.tag.list_tag import list_tag
from nbt_utils.tag.long_tag import long_tag
from nbt_utils.tag.string_tag import string_tag
from nbt_utils.utils.nbt_be_binary_stream import nbt_be_binary_stream
import os
import random
import sys
import time
from world.chunk.block_storage import block_storage
from world.chunk.chunk import chunk
from world.chunk.sub_chunk import sub_chunk
from world.chunk_utils import chunk_utils
from world.provider.anvil.region import region

class anvil:
    provider_name: str = "anvil"
    region_file_extension: str = "mca"
    
    def __init__(self, world_dir: str) -> None:
        self.world_dir: str = os.path.abspath(world_dir)
        if not os.path.isdir(self.world_dir):
            os.mkdir(self.world_dir)
        if not os.path.isfile(os.path.join(self.world_dir, "level.dat")):
            self.create_options_file()
        region_dir: str = os.path.join(self.world_dir, "region")
        if not os.path.isdir(region_dir):
            os.mkdir(region_dir)
            
    @staticmethod
    def get_index(x: int, y: int, z: int) -> int:
        return (x << 8) | (z << 4) | y
            
    @staticmethod
    def deserialize_sub_chunk(blocks: list, metas: list) -> object:
        blocks: list = chunk_utils.reorder_byte_array(blocks)
        metas: list = chunk_utils.reorder_nibble_array(metas)
        i_sub_chunk: object = sub_chunk()
        for x in range(0, 16):
            for z in range(0, 16):
                for y in range(0, 16):
                    index: int = anvil.get_index(x, y, z)
                    runtime_id: int = block_map.get_runtime_id(blocks[index], chunk_utils.get_nibble_4(metas, index))
                    i_sub_chunk.set_block_runtime_id(x, y, z, runtime_id, 0)
        return i_sub_chunk
            
    @staticmethod
    def deserialize_chunk(data: bytes) -> object:
        stream = nbt_be_binary_stream(data)
        root_tag: object = stream.read_root_tag()
        if not isinstance(root_tag, compound_tag):
            raise Exception("Invalid NBT data!")
        if not root_tag.has_tag("Level"):
            raise Exception("Level tag isnt present!")
        level_tag: object = root_tag.get_tag("Level")
        sub_chunks: dict = {}
        sections_tag: object = level_tag.get_tag("Sections")
        for section_tag in sections_tag.value:
            sub_chunks[section_tag.get_tag("Y").value]: object = anvil.deserialize_sub_chunk(
                section_tag.get_tag("Blocks").value,
                section_tag.get_tag("Data").value
            )
        if level_tag.has_tag("BiomeColors"):
            biomes: list = chunk_utils.convert_biome_colors(level_tag.get_tag("BiomeColors").value)
        else:
            biomes: list = level_tag.get_tag("Biomes").value
        i_chunk: object = chunk(
            level_tag.get_tag("xPos").value,
            level_tag.get_tag("zPos").value,
            sub_chunks,
            biomes
        )
        i_chunk.has_changed: bool = level_tag.get_tag("TerrainPopulated").value > 0
        
    @staticmethod
    def cr_index(x: int, z: int) -> tuple:
        return x >> 5, z >> 5
    
    @staticmethod
    def rc_index(x: int, z: int) -> tuple:
        return x - ((x >> 5) << 5), z - ((z >> 5) << 5)
    
    def get_chunk(self, x: int, z: int) -> object:
        region_index: tuple = anvil.cr_index(x, z)
        chunk_index: tuple = anvil.rc_index(x, z)
        region_path: str = os.path.join(os.path.join(self.world_dir, "region"), f"r.{region_index[0]}.{region_index[1]}.{self.region_file_extension}")
        reg: object = region(region_path)
        chunk_data: bytes = reg.get_chunk_data(chunk_index[0], chunk_index[1])
        return anvil.deserialize_chunk(chunk_data)
    
    @staticmethod
    def sub_chunk_to_section(sub_chunk: object) -> object:
        return compound_tag("", [
                byte_array_tag("Blocks", chunk_utils.reorder_byte_array(sub_chunk.ids)),
                byte_array_tag("Data", chunk_utils.reorder_byte_array(sub_chunk.data)),
                byte_array_tag("SkyLight", chunk_utils.reorder_byte_array(sub_chunk.sky_light)),
                byte_array_tag("BlockLight", chunk_utils.reorder_byte_array(sub_chunk.block_light))
        ])
                                        
    def set_chunk(self, x: int, z: int, chunk_in: object) -> None:
        region_index: tuple = anvil.cr_index(x, z)
        chunk_index: tuple = anvil.rc_index(x, z)
        region_path: str = os.path.join(os.path.join(self.world_dir, "region"), f"r.{region_index[0]}.{region_index[1]}.{self.region_file_extension}")
        reg: object = region(region_path)
        chunk_data: bytes = reg.get_chunk_data(chunk_index[0], chunk_index[1])
        stream: object = nbt_be_binary_stream(chunk_data)
        sections_tag = list_tag("Sections", [], tag_ids.compound_tag)
        for y, sub_chunk in chunk_in.sub_chunks.items():
            section_tag = anvil.sub_chunk_to_section(sub_chunk)
            section_tag.set_tag(byte_tag("Y", y))
            sections_tag.value.append(section_tag)
        tag: object = compound_tag("", [
            compound_tag("Level", [
                byte_array_tag("Biomes", chunk_in.biomes),
                list_tag("TileEntities", chunk_in.tiles, tag_ids.compound_tag),
                int_tag("xPos", chunk_in.x),
                int_tag("zPos", chunk_in.z),
                int_array_tag("HeightMap", chunk_in.height_map),
                byte_tag("V", 1),
                long_tag("LastUpdate", 0),
                long_tag("InhabitedTime", 0),
                byte_tag("LightPopulated", chunk_in.is_light_populated),
                byte_tag("TerrainPopulated", chunk_in.is_terrain_populated),
                list_tag("Entities", chunk_in.entities, tag_ids.compound_tag),
                sections_tag
            ]),
            int_tag("DataVersion", 1343)
        ])
        stream.write_root_tag(tag)
        reg.put_chunk_data(chunk_index[0], chunk_index[1], stream.data)
                                        
    def get_option(self, name: str) -> object:
        stream: object = nbt_be_binary_stream(gzip.decompress(open(os.path.join(self.world_dir, "level.dat"), "rb").read()))
        tag: object = stream.read_root_tag()
        return tag.get_tag("Data").get_tag(name).value
                                        
    def set_option(self, name: str, value: object) -> None:
        stream: object = nbt_be_binary_stream(gzip.decompress(open(os.path.join(self.world_dir, "level.dat"), "rb").read()))
        tag: object = stream.read_root_tag()
        data_tag: bytes = tag.get_tag("Data")
        if data_tag.has_tag(name):
            option_tag: object = data_tag.get_tag(name)
            option_tag.value = value
            data_tag.set_tag(option_tag)
            tag.set_tag(data_tag)
            stream.buffer: bytes = b""
            stream.pos: int = 0
            stream.write_root_tag(tag)
            file: object = open(os.path.join(self.world_dir, "level.dat"), "wb")
            file.write(gzip.compress(stream.data))
    
    def create_options_file(self) -> None:
        stream: object = nbt_be_binary_stream()
        tag: object = compound_tag("", [
            compound_tag("Data", [
                byte_tag("hardcore", 0),
                byte_tag("MapFeatures", 0),
                byte_tag("raining", 0),
                byte_tag("Difficulty", 0),
                byte_tag("initialized", 1),
                byte_tag("thundering", 0),
                int_tag("GameType", 0),
                int_tag("generatorVersion", 1),
                int_tag("rainTime", 0),
                int_tag("SpawnX", 256),
                int_tag("SpawnY", 70),
                int_tag("SpawnZ", 256),
                int_tag("thunderTime", 0),
                int_tag("version", 19133),
                long_tag("LastPlayed", int(time.time() * 1000)),
                long_tag("RandomSeed", random.randint(0, sys.maxsize)),
                long_tag("SizeOnDisk", 0),
                long_tag("Time", 0),
                compound_tag("GameRules", []),
                string_tag("generatorName", "flat"),
                string_tag("LevelName", "world")
            ])
        ])
        stream.write_root_tag(tag)
        file: object = open(os.path.join(self.world_dir, "level.dat"), "wb")
        file.write(gzip.compress(stream.data))
