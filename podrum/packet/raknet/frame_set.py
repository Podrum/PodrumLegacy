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

from packet.raknet.frame import frame
from utils.protocol_buffer import protocol_buffer

class frame_set(protocol_buffer):
    def __init__(self, data = b"", pos = 0):
        super().__init__(data, pos)
        self.frames: list = []
    
    def read_data(self) -> None:
        self.packet_id: int = self.read_uchar()
        self.sequence_number: int = self.read_utriad("little")
        while not self.pos_exceeded():
            frame_to_append: object = frame(self.data[self.pos:])
            frame_to_append.read_data()
            self.frames.append(frame_to_append)
            self.pos += frame_to_append.get_size()
        
    def write_data(self) -> None:
        self.write_uchar(self.packet_id)
        self.write_utriad(self.sequence_number, "little")
        for frame_to_write in self.frames:
            frame_to_write.write_data()
            self.write(frame_to_write.data)
            
    def get_size(self) -> int:
        length: int = 4
        for frame_in_list in self.frames:
            length += frame_in_list.get_size()
        return length
