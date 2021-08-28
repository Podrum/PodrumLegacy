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

import os

from podrum.block.block_map import block_map
from podrum.game_data.mcbe.block_id_map import block_id_map
from podrum.world.chunk.chunk import chunk as server_chunk
from podrum.world.provider.anvil.anvil import anvil
from podrum.world.provider.anvil.region import region
from podrum.world.provider.pm_anvil.chunk import chunk


class pm_anvil(anvil):

    provider_name: str = "pmanvil"
    region_file_extension: str = "mcapm"
    
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
            return pm_anvil.to_server_chunk(result)
                                        
    def set_chunk(self, chunk_in) -> None:
        region_index: tuple = anvil.cr_index(chunk_in.x, chunk_in.z)
        chunk_index: tuple = anvil.rc_index(chunk_in.x, chunk_in.z)
        region_path: str = os.path.join(os.path.join(self.world_dir, "region"), f"r.{region_index[0]}.{region_index[1]}.{self.region_file_extension}")
        reg = region(region_path)
        reg.put_chunk_data(chunk_index[0], chunk_index[1], anvil.to_anvil_chunk(chunk_in).nbt_serialize())
