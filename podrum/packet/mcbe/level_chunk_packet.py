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

from constant.mcbe_packet_ids import mcbe_packet_ids
from packet.mcbe.packet import packet

class level_chunk_packet(packet):
    def __init__(self, data: bytes = b"", pos: int = 0) -> None:
        super().__init__(data, pos)
        self.packet_id: int = mcbe_packet_ids.level_chunk_packet
 
    def decode_payload(self) -> None:
        self.chunk_x: int = self.read_signed_var_int()
        self.chunk_z: int = self.read_signed_var_int()
        self.sub_chunk_count: int = self.read_var_int()
        self.cache_enabled: bool = self.read_bool()
        self.chunk_data: bytes = self.read_remaining()
 
    def encode_payload(self) -> None:
        self.write_signed_var_int(self.chunk_x)
        self.write_signed_var_int(self.chunk_z)
        self.write_var_int(self.sub_chunk_count)
        self.write_bool(self.cache_enabled)
        self.write(self.chunk_data)
