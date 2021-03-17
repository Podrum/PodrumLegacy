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

from constant.nbt_tag_ids import nbt_tag_ids
from utils.nbt_be_binary_stream import nbt_be_binary_stream
from utils.nbt_le_binary_stream import nbt_le_binary_stream
from utils.nbt_net_le_binary_stream import nbt_net_le_binary_stream
from utils.context import context

class nbt:
    @staticmethod
    def read_type(stream: object, tag_id):
        if tag_id == nbt_tag_ids.byte_tag:
            return stream.read_byte_tag()
        elif tag_id == nbt_tag_ids.short_tag:
            return stream.read_short_tag()
        elif tag_id == nbt_tag_ids.int_tag:
            return stream.read_int_tag()
        elif tag_id == nbt_tag_ids.long_tag:
            return stream.read_long_tag()
        elif tag_id == nbt_tag_ids.float_tag:
            return stream.read_float_tag()
        elif tag_id == nbt_tag_ids.double_tag:
            return stream.read_double_tag()
        elif tag_id == nbt_tag_ids.byte_array_tag:
            return stream.read_byte_array_tag()
        elif tag_id == nbt_tag_ids.string_tag:
            return stream.read_string_tag()
        elif tag_id == nbt_tag_ids.list_tag:
            pass
        elif tag_id == nbt_tag_ids.compound_tag:
            pass
        elif tag_id == nbt_tag_ids.int_array_tag:
            return stream.read_int_array_tag()
