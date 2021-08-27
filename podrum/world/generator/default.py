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

from podrum.block import blocks

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
        chunk_type: str = "normal"

        # generates perlin noise
        perlin: object = Perlin(seed=world.server.config.data["seed"])

        # chunk generation
        for x in range(16):
            for z in range(16):
                y: int = perlin((chunk_x << 4) + x, (chunk_z << 4) + z)
                if sea_level + y <= sea_level and chunk_type != "water":
                    chunk_type: str = "water"

                # top layer, decides grass or sand if its a water chunk
                result.set_block_runtime_id(
                    x,
                    sea_level + y,
                    z,
                    blocks.grass().runtime_id
                    if chunk_type != "water"
                    else blocks.sand().runtime_id,
                )

                # decorate land
                if chunk_type != "water" and random.uniform(0, 1) > 0.85:
                    block_list = random.choices([blocks.yellow_flower().runtime_id, blocks.tallgrass().runtime_id, blocks.fern().runtime_id, blocks.poppy().runtime_id, None], weights=(1, 3, 1, 2, 3), k=10)
                    block = max(set(block_list), key=block_list.count)
                    if block is not None:
                        result.set_block_runtime_id(x, sea_level + y + 1, z, block)

                # fills in gaps underneath grass
                for i in range(sea_level + y + 1):
                    if (sea_level + (y - i)) == 0:
                        result.set_block_runtime_id(x, (sea_level + (y - i)), z, blocks.bedrock().runtime_id)
                    elif (sea_level + (y - i)) <= 2:
                        result.set_block_runtime_id(x, (sea_level + (y - i)), z, random.choice([blocks.bedrock().runtime_id, blocks.deepslate().runtime_id]))
                    elif (sea_level + (y - i)) <= 4:
                        result.set_block_runtime_id(x, (sea_level + (y - i)), z, blocks.deepslate().runtime_id)
                    elif (sea_level + (y - i)) <= 6:
                        result.set_block_runtime_id(x, (sea_level + (y - i)), z, random.choice([blocks.stone().runtime_id, blocks.deepslate().runtime_id]))
                    elif i <= 2:
                        result.set_block_runtime_id(
                            x,
                            (sea_level + (y - i)) - 1,
                            z,
                            blocks.dirt().runtime_id
                            if chunk_type != "water"
                            else blocks.sand().runtime_id,
                        )

                    else:
                        result.set_block_runtime_id(x, (sea_level + (y - i)) - 1, z, blocks.stone().runtime_id)

                # fills in water to sea level
                if sea_level + y <= sea_level:
                    for i in range(sea_level - (sea_level + y)):
                        result.set_block_runtime_id(x, sea_level + y + i + 1, z, blocks.still_water().runtime_id)

        if chunk_x == spawn_position.x >> 4 and chunk_z == spawn_position.z:
            spawn_position.y = 256
            world.set_spawn_position(spawn_position)

        return result
