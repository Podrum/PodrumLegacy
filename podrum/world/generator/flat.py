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

from podrum.block import blocks
from podrum.world.chunk.chunk import chunk


class flat:
    generator_name: str = "flat"
    
    @staticmethod
    def generate(chunk_x: int, chunk_z: int, world) -> object:
        result = chunk(chunk_x, chunk_z)
        spawn_position = world.get_spawn_position()

        for x in range(16):
            for z in range(16):
                result.set_block_runtime_id(x, 0, z, blocks.Bedrock().runtime_id)
                result.set_block_runtime_id(x, 1, z, blocks.Dirt().runtime_id)
                result.set_block_runtime_id(x, 2, z, blocks.Dirt().runtime_id)
                result.set_block_runtime_id(x, 3, z, blocks.Grass().runtime_id)

        if chunk_x == spawn_position.x >> 4 and chunk_z == spawn_position.z:
            spawn_position.y = 4
            world.set_spawn_position(spawn_position)

        return result
