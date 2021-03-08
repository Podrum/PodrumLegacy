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

from utils.protocol_buffer import protocol_buffer
from utils.raknet_reliability import raknet_reliability

class frame(protocol_buffer):
    def __init__(self, data = b"", pos = 0):
        super().__init__(data, pos)
        self.fragmented: bool = False
    
    def read_data(self) -> None:
        flags: int = self.read_uchar()
        self.reliability: int = (flags & 0xf4) >> 5
        self.fragmented: bool = (flags & 0x10) > 0
        body_length: int = self.read_ushort("big") >> 3
        if raknet_reliability.reliable(self.reliability):
            self.reliable_frame_index: int = self.read_utriad("little")
        if raknet_reliability.sequenced(self.reliability):
            self.sequenced_frame_index: int = self.read_utriad("little")
        if raknet_reliability.ordered(self.reliability):
            self.ordered_frame_index: int = self.read_utriad("little")
            self.order_channel: int = self.read_uchar()
        if self.fragmented:
            self.compound_size: int = self.read_uint("big")
            self.compound_id: int = self.read_ushort("big")
            self.index: int = self.read_uint("big")
        self.body: bytes = self.read(body_length)
    
    def write_data(self) -> None:
        self.write_uchar(self.reliability | 0x10 if self.fragmented else self.reliability)
        self.write_ushort(len(self.body) << 3, "big")
        if raknet_reliability.reliable(self.reliability):
            self.write_utriad(self.reliable_frame_index, "little")
        if raknet_reliability.sequenced(self.reliability):
            self.write_utriad(self.sequenced_frame_index, "little")
        if raknet_reliability.ordered(self.reliability):
            self.write_utriad(self.ordered_frame_index, "little")
            self.write_uchar(self.order_channel)
        if self.fragmented:
            self.write_uint(self.compound_size, "big")
            self.write_ushort(self.compound_id, "big")
            self.write_uint(self.index, "big")
        self.write(self.body)
        
    def get_size(self) -> int:
        length: int = 3
        if raknet_reliability.reliable(self.reliability):
            length += 3
        if raknet_reliability.sequenced(self.reliability):
            length += 3
        if raknet_reliability.ordered(self.reliability):
            length += 4
        if self.fragmented:
            length += 10
        length += len(self.body)
        return length
