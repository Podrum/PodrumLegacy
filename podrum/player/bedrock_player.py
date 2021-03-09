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

from packet.raknet.game_packet import game_packet
from packet.raknet.frame import frame
from utils.protocol_buffer import protocol_buffer
import zlib

class bedrock_player:
    def __init__(self, address, server):
        self.address = address
        self.server = server
        
    def handle_packet(self, data):
        pass
    
    def send_packet(self, data):
        buffer: object = protocol_buffer()
        buffer.write_mcbe_byte_array(data)
        new_packet = game_packet()
        compress = zlib.compressobj(self.compressionLevel, zlib.DEFLATED, -zlib.MAX_WBITS)
        compressed_data = compress.compress(buffer.data)
        compressed_data += compress.flush()
        new_packet.body = compressed_data
        new_packet.write_data()
        send_packet = frame()
        send_packet.reliability = 0
        send_packet.body = new_packet.buffer
        self.server.raknet_handler.add_to_queue(send_packet, self.address)
