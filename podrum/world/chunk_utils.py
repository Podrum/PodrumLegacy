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

class chunk_utils:
    @staticmethod
    def reorder_byte_array(array: list) -> list:
        result: list = [0] * 4096
        if array != result:
            i: int = 0
            for x in range(0, 16):
                z_m: int = x + 256
                for z in range(x, z_m, 16):
                    y_m: int = z + 4096
                    for y in range(z, y_m, 256):
                        result[i]: int = array[y]
                        i += 1
            return result
        
    @staticmethod
    def reorder_nibble_array(array: list, common_value: int = 0) -> list:
        result: list = [common_value] * 2048
        if array != result:
            i: int = 0
            for x in range(0, 8):
                for z in range(0, 16):
                    zx: int = ((z << 3) | x)
                    for y in range(0, 8):
                        j: int = ((y << 8) | zx)
                        j80: int = (j | 0x80)
                        if array[j] != common_value and array[j80] != common_value:
                            i1: int = array[j]
                            i2: int = array[j80]
                            result[i]: int = (i2 << 4) | (i1 & 0x0f)
                            result[i | 0x80]: int = (i1 >> 4) | (i2 & 0xf0)
                        i += 1
                i += 128
            return result

    @staticmethod
    def convert_biome_colors(array: list) -> list:
        result: list = [0] * 256
        for color in array:
            result.append((color >> 24) & 0xff)
        return result
