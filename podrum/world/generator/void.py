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

from block.default.stone import stone
from world.chunk.chunk import chunk

class void:
    generator_name: str = "void"
    
    @staticmethod
    def generate(chunk_x: int, chunk_z: int, world: object) -> object:
        result: object = chunk(chunk_x, chunk_z)
        spawn_position: object = world.get_spawn_position()
        if chunk_x == spawn_position.x >> 4 and chunk_z == spawn_position.z:
            for x in range(0, 16):
                for z in range(0, 16):
                    result.set_block_runtime_id(x, 0, z, stone().runtime_id)
            spawn_position.y: int = result.get_highest_block_at(spawn_position.x, spawn_position.z)
            world.set_spawn_position(spawn_position)
        return result
