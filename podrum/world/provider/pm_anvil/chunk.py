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

from world.provider.anvil.chunk import chunk
from world.provider.pm_anvil.section import section

class chunk(chunk):
    def __init__(self, x: int, z: int, sections: dict = {}, height_map: list = [], biomes: list = [], entities: list = [], tile_entities: list = []) -> None:
        self.x: int = x
        self.z: int = z
        self.sections: dict = {}
        for i in range(0, 16):
            if i in sections:
                self.sections[i]: object = sections[i]
            else:
                self.sections[i]: object = section()
        if len(height_map) == 256:
            self.height_map: list = height_map
        else:
            self.height_map: list = [0] * 256      
        if len(biomes) == 256:
            self.biomes: list = biomes
        else:
            self.biomes: list = [0] * 256
        self.entities: list = entities
        self.tile_entities: list = tile_entities
        self.light_populated: bool = False
        self.terrain_populated: bool = False
