
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
from nbt_utils.tag_ids import tag_ids
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
from world.chunk.chunk import chunk as server_chunk
from world.chunk.sub_chunk import sub_chunk
from world.chunk_utils import chunk_utils
from world.provider.pm_anvil.chunk import chunk
from world.provider.anvil.region import region

class pm_anvil:
    provider_name: str = "pmanvil"
    region_file_extension: str = "mcapm"
    
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
    def cr_index(x: int, z: int) -> tuple:
        return x >> 5, z >> 5
    
    @staticmethod
    def rc_index(x: int, z: int) -> tuple:
        return x - ((x >> 5) << 5), z - ((z >> 5) << 5)
    
    @staticmethod
    def to_server_chunk(chunk_in: object) -> object:
        cnv_chunk: object = server_chunk(chunk_in.x, chunk_in.z)
        for x in range(0, 16):
            for z in range(0, 16):
                for y in range(0, chunk_in.get_highest_block_at(x, z) + 1):
                    block: int = chunk_in.get_block_id(x, y, z) & 0xff
                    meta: int = chunk_in.get_data(x, y, z) & 0xff
                    try:
                        runtime_id: int = block_map.get_runtime_id(block, meta)
                    except KeyError:
                        runtime_id: int = block_map.get_runtime_id(block, 0)
                    cnv_chunk.set_block_runtime_id(x, y, z, runtime_id)
        return cnv_chunk
    
    @staticmethod
    def to_anvil_chunk(chunk_in: object) -> object:
        cnv_chunk: object = chunk(chunk_in.x, chunk_in.z)
        for x in range(0, 16):
            for z in range(0, 16):
                for y in range(0, chunk_in.get_highest_block_at(x, z) + 1):
                    legacy_id: tuple = block_map.get_legacy_id(chunk_in.get_block_runtime_id(x, y, z))
                    block: int = (((legacy_id[0] >> 7) * 128) ^ legacy_id[0]) - ((legacy_id[0] >> 7) * 128)
                    meta: int = (((legacy_id[1] >> 7) * 128) ^ legacy_id[1]) - ((legacy_id[1] >> 7) * 128)
                    cnv_chunk.set_block_id(x, y, z, block)
                    cnv_chunk.set_data(x, y, z, meta)
        return cnv_chunk
    
    def get_chunk(self, x: int, z: int) -> object:
        region_index: tuple = anvil.cr_index(x, z)
        chunk_index: tuple = anvil.rc_index(x, z)
        region_path: str = os.path.join(os.path.join(self.world_dir, "region"), f"r.{region_index[0]}.{region_index[1]}.{self.region_file_extension}")
        reg: object = region(region_path)
        chunk_data: bytes = reg.get_chunk_data(chunk_index[0], chunk_index[1])
        result: object = chunk(x, z)
        if len(chunk_data) > 0:
            result.nbt_deserialize(chunk_data)
        return anvil.to_server_chunk(result)
                                        
    def set_chunk(self, x: int, z: int, chunk_in: object) -> None:
        region_index: tuple = anvil.cr_index(x, z)
        chunk_index: tuple = anvil.rc_index(x, z)
        region_path: str = os.path.join(os.path.join(self.world_dir, "region"), f"r.{region_index[0]}.{region_index[1]}.{self.region_file_extension}")
        reg: object = region(region_path)
        reg.put_chunk_data(chunk_index[0], chunk_index[1], anvil.to_anvil_chunk(chunk_in).serialize())
                                        
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
