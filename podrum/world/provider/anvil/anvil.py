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

import gzip
import os
import random
import sys
import time

from nbt_utils.tag.byte_tag import byte_tag
from nbt_utils.tag.compound_tag import compound_tag
from nbt_utils.tag.double_tag import double_tag
from nbt_utils.tag.float_tag import float_tag
from nbt_utils.tag.int_tag import int_tag
from nbt_utils.tag.list_tag import list_tag
from nbt_utils.tag.long_tag import long_tag
from nbt_utils.tag.short_tag import short_tag
from nbt_utils.tag.string_tag import string_tag
from nbt_utils.tag_ids import tag_ids
from nbt_utils.utils.nbt_be_binary_stream import nbt_be_binary_stream

from podrum.block.block_map import block_map
from podrum.config import config
from podrum.game_data.mcbe.block_id_map import block_id_map
from podrum.geometry.vector_3 import vector_3
from podrum.world.chunk.chunk import chunk as server_chunk
from podrum.world.provider.anvil.chunk import chunk
from podrum.world.provider.anvil.region import region


class anvil:

    provider_name: str = "anvil"
    region_file_extension: str = "mca"
    
    def __init__(self, world_dir: str) -> None:
        self.world_dir: str = os.path.abspath(world_dir)
        self.config = config(os.path.join(os.getcwd(), "server.json"))
        if not os.path.isdir(self.world_dir):
            os.mkdir(self.world_dir)
        if not os.path.isfile(os.path.join(self.world_dir, "level.dat")):
            self.create_options_file()
        region_dir: str = os.path.join(self.world_dir, "region")
        if not os.path.isdir(region_dir):
            os.mkdir(region_dir)
        player_dir: str = os.path.join(self.world_dir, "players")
        if not os.path.isdir(player_dir):
            os.mkdir(player_dir)
        
    @staticmethod
    def cr_index(x: int, z: int) -> tuple:
        return x >> 5, z >> 5
    
    @staticmethod
    def rc_index(x: int, z: int) -> tuple:
        return x - ((x >> 5) << 5), z - ((z >> 5) << 5)
    
    @staticmethod
    def to_server_chunk(chunk_in) -> object:
        cnv_chunk = server_chunk(chunk_in.x, chunk_in.z)
        for x in range(16):
            for z in range(16):
                for y in range(chunk_in.get_highest_block_at(x, z) + 1):
                    block_id: int = chunk_in.get_block_id(x, y, z) & 0xff
                    meta: int = chunk_in.get_data(x, y, z) & 0xff
                    block_name: str = list(block_id_map.keys())[list(block_id_map.values()).index(block_id)]

                    try:
                        runtime_id: int = block_map.get_runtime_id(block_name, meta)
                    except KeyError:
                        runtime_id: int = block_map.get_runtime_id(block_name, 0)

                    cnv_chunk.set_block_runtime_id(x, y, z, runtime_id)
        return cnv_chunk
    
    @staticmethod
    def to_anvil_chunk(chunk_in) -> object:
        cnv_chunk = chunk(chunk_in.x, chunk_in.z)
        for x in range(16):
            for z in range(16):
                for y in range(chunk_in.get_highest_block_at(x, z) + 1):
                    legacy_id: tuple = block_map.get_name_and_meta(chunk_in.get_block_runtime_id(x, y, z))
                    block: int = (((block_id_map[legacy_id[0]] >> 7) * 128) ^ block_id_map[legacy_id[0]]) - ((block_id_map[legacy_id[0]] >> 7) * 128)
                    meta: int = (((legacy_id[1] >> 7) * 128) ^ legacy_id[1]) - ((legacy_id[1] >> 7) * 128)
                    cnv_chunk.set_block_id(x, y, z, block)
                    cnv_chunk.set_data(x, y, z, meta)
        return cnv_chunk
    
    def get_chunk(self, x: int, z: int) -> object:
        region_index: tuple = anvil.cr_index(x, z)
        chunk_index: tuple = anvil.rc_index(x, z)
        region_path: str = os.path.join(os.path.join(self.world_dir, "region"), f"r.{region_index[0]}.{region_index[1]}.{self.region_file_extension}")
        reg = region(region_path)
        chunk_data: bytes = reg.get_chunk_data(chunk_index[0], chunk_index[1])

        if len(chunk_data) > 0:
            result = chunk(x, z)
            result.nbt_deserialize(chunk_data)
            return anvil.to_server_chunk(result)
                                        
    def set_chunk(self, chunk_in) -> None:
        region_index: tuple = anvil.cr_index(chunk_in.x, chunk_in.z)
        chunk_index: tuple = anvil.rc_index(chunk_in.x, chunk_in.z)
        region_path: str = os.path.join(os.path.join(self.world_dir, "region"), f"r.{region_index[0]}.{region_index[1]}.{self.region_file_extension}")
        reg = region(region_path)
        reg.put_chunk_data(chunk_index[0], chunk_index[1], anvil.to_anvil_chunk(chunk_in).nbt_serialize())
                                        
    def get_option(self, name: str) -> object:
        with open(os.path.join(self.world_dir, "level.dat"), "rb") as file:
            stream = nbt_be_binary_stream(gzip.decompress(file.read()))
            file.close()
            tag = stream.read_root_tag()
            return tag.get_tag("Data").get_tag(name).value
                                        
    def set_option(self, name: str, value) -> None:
        with open(os.path.join(self.world_dir, "level.dat"), "rb") as file:
            stream = nbt_be_binary_stream(gzip.decompress(file.read()))
            file.close()
            tag = stream.read_root_tag()
            data_tag: bytes = tag.get_tag("Data")

            if data_tag.has_tag(name):
                option_tag = data_tag.get_tag(name)
                option_tag.value = value
                data_tag.set_tag(option_tag)
                tag.set_tag(data_tag)
                stream.buffer = b""
                stream.pos = 0
                stream.write_root_tag(tag)

                with open(os.path.join(self.world_dir, "level.dat"), "wb") as file:
                    file.write(gzip.compress(stream.data))
                    file.close()
            
    def get_player_option(self, uuid: str, name: str) -> object:
        with open(os.path.join(self.world_dir, f"players/{uuid}.dat"), "rb") as file:
            stream = nbt_be_binary_stream(gzip.decompress(file.read()))
            file.close()
            tag = stream.read_root_tag()

            return tag.get_tag(name).value
    
    def set_player_option(self, uuid: str, name: str, value) -> None:
        with open(os.path.join(self.world_dir, f"players/{uuid}.dat"), "rb") as file:
            stream = nbt_be_binary_stream(gzip.decompress(file.read()))
            file.close()
            tag = stream.read_root_tag()

            if tag.has_tag(name):
                option_tag = tag.get_tag(name)
                option_tag.value = value
                tag.set_tag(option_tag)
                stream.buffer = b""
                stream.pos = 0
                stream.write_root_tag(tag)

                with open(os.path.join(self.world_dir, f"players/{uuid}.dat"), "wb") as file:
                    file.write(gzip.compress(stream.data))
                    file.close()
            
    def get_spawn_position(self) -> object:
        return vector_3(
            self.get_option("SpawnX"),
            self.get_option("SpawnY"),
            self.get_option("SpawnZ")
        )
    
    def set_spawn_position(self, position) -> None:
        self.set_option("SpawnX", position.x)
        self.set_option("SpawnY", position.y)
        self.set_option("SpawnZ", position.z)
        
    def get_world_gamemode(self) -> int:
        return self.get_option("GameType")
    
    def set_world_gamemode(self, gamemode: int) -> None:
        self.set_option("GameType", gamemode)
        
    def get_world_name(self) -> str:
        return self.get_option("LevelName")
    
    def set_world_name(self, world_name: str) -> None:
        self.set_option("LevelName", world_name)
        
    def get_generator_name(self) -> str:
        return self.get_option("generatorName")
    
    def set_generator_name(self, generator_name: str) -> None:
        self.set_option("generatorName", generator_name)
        
    def get_time(self) -> int:
        return self.get_option("Time")
    
    def set_time(self, world_time: int) -> None:
        self.set_option("Time", world_time)
        
    def get_player_position(self, uuid: str) -> object:
        position_tag = self.get_player_option(uuid, "Pos")
        return vector_3(position_tag[0].value, position_tag[1].value, position_tag[2].value)
            
    def set_player_position(self, uuid: str, position) -> None:
        self.set_player_option(uuid, "Pos", [
            double_tag("", position.x),
            double_tag("", position.y),
            double_tag("", position.z)
        ])
        
    def get_player_gamemode(self, uuid: str) -> int:
        return self.get_player_option(uuid, "playerGameType")
            
    def set_player_gamemode(self, uuid: str, gamemode) -> None:
        self.set_player_option(uuid, "playerGameType", gamemode)
        
    def has_player_file(self, uuid: str) -> bool:
        return bool(
            os.path.isfile(os.path.join(self.world_dir, f"players/{uuid}.dat"))
        )
        
    def create_player_file(self, uuid: str) -> None:
        stream = nbt_be_binary_stream()
        tag = compound_tag("", [
            byte_tag("OnGround", 1),
            byte_tag("Sleeping", 0),
            short_tag("Air", 300),
            short_tag("AttackTime", 0),
            short_tag("DeathTime", 0),
            short_tag("Fire", 0),
            short_tag("Health", 20),
            short_tag("HurtTime", 0),
            short_tag("SleepTimer", 0),
            int_tag("Dimension", 0),
            int_tag("foodLevel", 0),
            int_tag("foodTickTimer", 0),
            int_tag("playerGameType", self.get_world_gamemode()),
            int_tag("XpLevel", 0),
            int_tag("XpTotal", 0),
            float_tag("FallDistance", 0),
            float_tag("foodExhastionLevel", 0),
            float_tag("foodSaturationLevel", 0),
            float_tag("XpP", 0),
            compound_tag("Inventory", []),
            list_tag("Motion", [
                double_tag("", 0),
                double_tag("", 0),
                double_tag("", 0)
            ], tag_ids.double_tag),
            list_tag("Pos", [
                double_tag("", self.get_spawn_position().x),
                double_tag("", self.get_spawn_position().y),
                double_tag("", self.get_spawn_position().z)
            ], tag_ids.double_tag),
            list_tag("Rotation", [
                float_tag("", 0),
                float_tag("", 0),
                float_tag("", 0)
            ], tag_ids.float_tag)
        ])
        stream.write_root_tag(tag)
        with open(os.path.join(self.world_dir, f"players/{uuid}.dat"), "wb") as file:
            file.write(gzip.compress(stream.data))
            file.close()
    
    def create_options_file(self) -> None:
        stream = nbt_be_binary_stream()
        tag = compound_tag("", [
            compound_tag("Data", [
                byte_tag("hardcore", 0),
                byte_tag("MapFeatures", 0),
                byte_tag("raining", 0),
                byte_tag("Difficulty", 0),
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
                string_tag("generatorName", self.config.data["world_type"]),
                string_tag("LevelName", "world"),
                compound_tag("GameRules", [])
            ])
        ])

        stream.write_root_tag(tag)
        with open(os.path.join(self.world_dir, "level.dat"), "wb") as file:
            file.write(gzip.compress(stream.data))
            file.close()
