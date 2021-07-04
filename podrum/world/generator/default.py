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

from podrum.block.default.bedrock import bedrock
from podrum.block.default.stone import stone
from podrum.block.default.dirt import dirt
from podrum.block.default.grass import grass
from podrum.block.default.water import water
from podrum.block.default.sand import sand

from podrum.world.chunk.chunk import chunk
from podrum.world.generator.noise.perlin import Perlin
import random

class default:
    generator_name: str = "default"

    @staticmethod
    def generate(chunk_x: int, chunk_z: int, world: object) -> object:
        result: object = chunk(chunk_x, chunk_z)
        spawn_position: object = world.get_spawn_position()
        # Default: 62, Reduced to 20 for faster load time
        sea_level: int = 62
        seed: int = 578932354547655231

        # generates perlin noise
        perlin = Perlin(seed=seed)

        # chunk generation
        for x in range(0, 16):
            for z in range(0, 16):
                y = perlin((chunk_x << 4) + x, (chunk_z << 4) + z, scale=2, octaves=1, lacunarity=1, persistence=1)
                result.set_block_runtime_id(x, sea_level + y, z, grass().runtime_id)

                # fills in gaps underneath grass
                for i in range(sea_level + y + 1):
                    if (sea_level + (y - i)) == 0: 
                        result.set_block_runtime_id(x, (sea_level + (y - i)), z, bedrock().runtime_id)
                    elif (sea_level + (y - i)) <= 2: 
                        result.set_block_runtime_id(x, (sea_level + (y - i)), z, random.choice([bedrock().runtime_id, stone().runtime_id]))
                    elif (i <= 2): 
                        result.set_block_runtime_id(x, (sea_level + (y - i)) - 1, z, dirt().runtime_id)
                    else: 
                        result.set_block_runtime_id(x, (sea_level + (y - i)) - 1, z, stone().runtime_id)

                if sea_level + y < sea_level:
                    for i in range(sea_level - (sea_level + y)):
                        result.set_block_runtime_id(x, sea_level + y + i + 1, z, water().runtime_id)

        if chunk_x == spawn_position.x >> 4 and chunk_z == spawn_position.z:
            spawn_position.y = 256
            world.set_spawn_position(spawn_position)
        return result