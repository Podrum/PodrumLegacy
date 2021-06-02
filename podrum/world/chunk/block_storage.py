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

from block.block_map import block_map

class block_storage:
    block_map: object = block_map()
  
    def __init__(self, blocks: list = [], palette: list = []) -> None:
        if len(palette) > 0:
            self.palette: list = palette
        else:
            self.palette: list = [block_storage.legacy_to_runtime_id(0, 0)]
        if len(blocks) == 4096:
            self.blocks: list = blocks
        else:
            self.blocks: list = [0] * 4096
           
    @staticmethod
    def get_index(x: int, y: int, z: int) -> int:
        return (((x & 0x0f) << 8) + ((z & 0x0f) << 4)) | (y & 0x0f)
    
    def get_block(self, x, y, z) -> tuple
        palette_index: int = self.blocks[block_storage.get_index(x, y, x)]
        runtime_id: int = self.pallete[palette_index]
        return block_storage.runtime_to_legacy_id(runtime_id)
    
    def set_block(self, x, y, z, block: int, meta: int) -> None:
        runtime_id: int = block_storage.legacy_to_runtime_id(block, meta)
        if runtime_id not in self.palette:
            self.palette.append(runtime_id)
        self.blocks[block_storage.get_index(x, y, x)]: int = self.pallete.index(runtime_id)
