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
import zlib

class game_packet(protocol_buffer):
    def read_data(self):
        self.packet_id: int = self.read_uchar()
        self.body: bytes = zlib.decompress(self.read_remaining(), -zlib.MAX_WBITS, 1024 * 1024 * 8)
        
    def write_data(self):
        self.write_uchar(self.packet_id)
        compress: object = zlib.compressobj(1, zlib.DEFLATED, -zlib.MAX_WBITS)
        compressed_data: bytes = compress.compress(self.body)
        compressed_data += compress.flush()
        self.write(compressed_data)
  
    def write_packet_data(self, data):
        buffer: object = protocol_buffer()
        buffer.write_mcbe_byte_array(data)
        if hasattr(self, "body"):
            self.body += buffer.data
        else:
            self.body: bytes = buffer.data
            
    def read_packets_data(self):
        buffer: object = protocol_buffer(self.body)
        packets_data: list = []
        while not buffer.pos_exceeded():
            packets_data.append(buffer.read_mcbe_byte_array())
        return packets_data
