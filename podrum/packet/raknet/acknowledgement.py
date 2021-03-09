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

class acknowledgement(protocol_buffer):
    def read_data(self) -> None:
        self.packet_id: int = self.read_uchar()
        self.sequence_numbers: list = []
        count: int = self.read_ushort("big")
        for i in range(0, count):
            single: bool = self.read_bool()
            if not single:
                index = self.read_utriad("little")
                end_index = self.read_utriad("little")
                while index <= end_index:
                    self.sequence_numbers.append(index)
                    index += 1
            else:
                self.sequence_numbers.append(self.read_utriad("little"))
        
    def write_data(self) -> None:
        self.write_uchar(self.packet_id)
        self.sequence_numbers.sort()
        temp_buffer: object = protocol_buffer()
        count: int = 0
        if len(self.sequence_numbers) > 0:
            start_index = self.sequence_numbers[0]
            end_index = self.sequence_numbers[0]
            for pointer in range(1, len(self.sequence_numbers)):
                current_index = self.sequence_numbers[pointer]
                diff = current_index - end_index
                if diff == 1:
                    end_index = current_index
                elif diff > 1:
                    if start_index == end_index:
                        temp_buffer.write_bool(True)
                        temp_buffer.write_utriad(start_index, "little")
                        start_index = end_index = current_index
                    else:
                        temp_buffer.write_bool(False)
                        temp_buffer.write_utriad(start_index, "little")
                        temp_buffer.write_utriad(end_index, "little")
                        start_index = end_index = current_index
                    count += 1
            if start_index == end_index:
                temp_buffer.write_bool(True)
                temp_buffer.write_utriad(start_index, "little")
            else:
                temp_buffer.write_bool(False)
                temp_buffer.write_utriad(start_index, "little")
                temp_buffer.write_utriad(end_index, "little")
            count += 1
            self.write_ushort(count, "big")
            self.write(temp_buffer.data)
