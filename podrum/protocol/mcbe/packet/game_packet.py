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

from binary_utils.binary_stream import binary_stream
from protocol.mcbe.packet.mcbe_packet import mcbe_packet
import zlib

class game_packet(mcbe_packet):
    def __init__(self, data: bytes = b"", pos: int = 0) -> None:
        super().__init__(data, pos)
        self.packet_id: int = 0xfe

    def decode_payload(self):
        self.body: bytes = zlib.decompress(self.read_remaining(), -zlib.MAX_WBITS, 1024 * 1024 * 8)
        
    def encode_payload(self):
        compress: object = zlib.compressobj(1, zlib.DEFLATED, -zlib.MAX_WBITS)
        compressed_data: bytes = compress.compress(self.body)
        compressed_data += compress.flush()
        self.write(compressed_data)
  
    def write_packet_data(self, data):
        buffer: object = binary_stream()
        buffer.write_var_int(len(data))
        buffer.write(data)
        if hasattr(self, "body"):
            self.body += buffer.data
        else:
            self.body: bytes = buffer.data
            
    def read_packets_data(self):
        buffer: object = binary_stream(self.body)
        packets_data: list = []
        while not buffer.feos():
            packets_data.append(buffer.read(buffer.read_var_int()))
        return packets_data
