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

from nbt_utils.tag.byte_array_tag import byte_array_tag
from world.format.anvil.anvil import anvil

class pm_anvil(anvil):
    region_file_extension: str = "mcapm"
    format_name: str = "pmanvil"
    
    @staticmethod
    def section_to_sub_chunk(section_tag: object) -> object:
        return sub_chunk(
            section_tag.get_tag("Blocks").value,
            section_tag.get_tag("Data").value,
            section_tag.get_tag("SkyLight").value,
            section_tag.get_tag("BlockLight").value
        )
    
    @staticmethod
    def sub_chunk_to_section(sub_chunk: object) -> object:
        return compound_tag("", [
                byte_array_tag("Blocks", sub_chunk.ids),
                byte_array_tag("Data", sub_chunk.data),
                byte_array_tag("SkyLight", sub_chunk.sky_light),
                byte_array_tag("BlockLight", sub_chunk.block_light)
        ])
