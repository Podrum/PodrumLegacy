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

import asyncio
from podrum.block.default.stone import stone
from podrum.world.chunk.chunk import chunk

class void:
    generator_name: str = "void"
    
    @staticmethod
    async def generate(chunk_x: int, chunk_z: int, world: object) -> object:
        out: object = asyncio.Future()
        result: object = chunk(chunk_x, chunk_z)
        spawn_position: object = world.get_spawn_position()
        if chunk_x == spawn_position.x >> 4 and chunk_z == spawn_position.z:
            for x in range(0, 16):
                for z in range(0, 16):
                    result.set_block_runtime_id(x, 0, z, stone().runtime_id)
            spawn_position.y = 1
            world.set_spawn_position(spawn_position)
        out.set_result(result)
        return out
