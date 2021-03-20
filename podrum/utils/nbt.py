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
from nbt_tag.byte_array_tag import byte_array_tag
from nbt_tag.byte_tag import byte_tag
from nbt_tag.double_tag import double_tag
from nbt_tag.float_tag import float_tag
from nbt_tag.int_array_tag import int_array_tag
from nbt_tag.int_tag import int_tag
from nbt_tag.long_array_tag import long_array_tag
from nbt_tag.long_tag import long_tag
from nbt_tag.short_tag import short_tag
from nbt_tag.string_tag import string_tag

class nbt:
    @staticmethod
    def new_tag(tag_id: int) -> object:
        if tag_id == nbt_tag_ids.byte_tag:
            return byte_tag()
        if tag_id == nbt_tag_ids.short_tag:
            return short_tag()
        if tag_id == nbt_tag_ids.int_tag:
            return int_tag()
        if tag_id == nbt_tag_ids.long_tag:
            return long_tag()
        if tag_id == nbt_tag_ids.float_tag:
            return float_tag()
        if tag_id == nbt_tag_ids.double_tag:
            return double_tag()
        if tag_id == nbt_tag_ids.byte_array_tag:
            return byte_array_tag()
        if tag_id == nbt_tag_ids.string_tag:
            return string_tag()
        if tag_id == nbt_tag_ids.list_tag:
            return
        if tag_id == nbt_tag_ids.compound_tag:
            return
        if tag_id == nbt_tag_ids.int_array_tag:
            return int_array_tag()
        if tag_id == nbt_tag_ids.long_array_tag:
            return long_array_tag()
