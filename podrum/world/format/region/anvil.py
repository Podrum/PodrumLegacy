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

import math
from nbt_utils.tag.byte_tag import byte_tag
from nbt_utils.tag.compound_tag import compound_tag
from nbt_utils.tag.int_tag import int_tag
from nbt_utils.tag.long_tag import long_tag
from nbt_utils.tag.string_tag import string_tag
from nbt_utils.utils.nbt_be_binary_stream import nbt_be_binary_stream
import os
from podrum.world.chunk.chunk import chunk
from podrum.world.chunk.empty_sub_chunk import empty_sub_chunk
from podrum.world.chunk.sub_chunk import sub_chunk
from podrum.world.format.region.region import region
import random
import sys
import time

class anvil:
    def __init__(self, world_dir: str) -> None:
        self.world_dir: str = os.path.abspath(world_dir)
        if not os.path.isdir(self.world_dir):
            os.mkdir(self.world_dir)
        if not isfile(os.path.join(self.world_dir, "level.dat")):
            self.create_options_file()
        region_dir: str = os.path.join(self.world_dir, "region")
        if not os.path.isdir(region_dir):
            os.mkdir(region_dir)
        
    @staticmethod
    def cr_index(x: int, z: int) -> tuple:
        return math.ceil(x / 32), math.ceil(z / 32)
    
    @staticmethod
    def rc_index(x: int, z: int) -> tuple:
        return abs(abs(self.x << 5) - abs(x)), abs(abs(self.z << 5) - abs(y))
    
    def get_chunk(self, x: int, z: int) -> object:
        region_index: tuple = anvil.cr_index(x, z)
        chunk_index: tuple = anvil.rc_index(x, z)
        region_path: str = os.path.join(os.path.join(self.world_dir, "region"), f"r.{region_index[0]}.{region_index[1]}.mca"
        reg: object = region(region_path)
        chunk_data: bytes = reg.get_chunk_data(chunk_index[0], chunk_index[1])
        stream: object = nbt_be_binary_stream(chunk_data)
        tag: object = compound_tag()
        tag.read(stream)
        comment = """root_tag: object = root_tag.get_tag("")
        level_tag: object = root_tag.get_tag("Level")
        self.x: int = level_tag.get_tag("xPos").value
        self.z: int = level_tag.get_tag("zPos").value
        self.biomes: list = level_tag.get_tag("Biomes").value
        self.height_map: list = level_tag.get_tag("HeightMap").value
        self.terrain_populated: bool = level_tag.get_tag("TerrainPopulated").value > 0
        self.light_populated: bool = level_tag.get_tag("LightPopulated").value > 0
        self.last_update: int = level_tag.get_tag("LastUpdate").value
        self.inhabited_time: int = level_tag.get_tag("InhabitedTime").value
        self.tile_entities: list = level_tag.get_tag("TileEntities").value
        self.entities: list = level_tag.get_tag("Entities").value"""
    
    def create_options_file(self) -> None:
        stream: object = nbt_be_binary_stream(chunk)
        tag: object = compound_tag("", [
            compound_tag("Data", [
                byte_tag("hardcore", 0),
                byte_tag("MapFeatures", 0),
                byte_tag("raining", 0),
                byte_tag("thundering", 0),
                int_tag("GameType", 0),
                int_tag("generatorVersion", 0),
                int_tag("rainTime", 0),
                int_tag("SpawnX", 0),
                int_tag("SpawnY", 0),
                int_tag("SpawnZ", 0),
                int_tag("thunderTime", 0),
                int_tag("version", 19133),
                long_tag("LastPlayed", int(time.time())),
                long_tag("RandomSeed", random.randint(0, sys.maxsize)),
                long_tag("SizeOnDisk", 0),
                long_tag("Time", 0),
                string_tag("generatorName", "flat"),
                string_tag("LevelName", "world")
            ])
        ])
        tag.write(stream)
        file: object = open(os.path.join(self.world_dir, "level.dat"), "wb")
        file.write(stream.data)
