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
from packet.mcbe.game_packet import game_packet
from packet.mcbe.play_status_packet import play_status_packet
from packet.raknet.frame import frame
from utils.protocol_buffer import protocol_buffer
import zlib

class bedrock_player:
    def __init__(self, address, server):
        self.address = address
        self.server = server
        
    def handle_packet(self, data):
        if data[0] == mcbe_packet_ids.login_packet:
            self.send_play_status(7)
    
    def send_play_status(self, status):
        packet: object = play_status_packet()
        packet.packet_id: int = mcbe_packet_ids.play_status_packet
        packet.status: int = status
        packet.write_data()
        self.send_packet(packet.data)
    
    def send_packet(self, data):
        new_packet: object = game_packet()
        new_packet.packet_id: int = raknet_packet_ids.game_packet
        new_packet.write_packet_data(data)
        new_packet.write_data()
        send_packet: object = frame()
        send_packet.reliability: int = 0
        send_packet.body: bytes = new_packet.data
        self.server.raknet_handler.add_to_queue(send_packet, self.address, False)
