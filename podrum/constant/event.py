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

from packet.mcbe.game_packet import game_packet
from player.bedrock_player import bedrock_player

class event:
    @staticmethod
    def on_packet_data(data, address, server) -> None:
        if address.token in server.players:
            if data[0] == 0xfe:
                packet = game_packet(data)
                packet.read_data()
                packets = packet.read_packets_data()
                for batch in packets:
                    print(hex(batch[0]))
                    server.players[address.token].handle_packet(batch)
            
    @staticmethod
    def on_new_incoming_connection(address, server):
        server.players[address.token] = bedrock_player(address, server)
        server.logger.info(f"{address.token} connected.")
                   
    @staticmethod
    def on_raknet_disconnect(address, server):
        del server.players[address.token]
        server.logger.info(f"{address.token} disconnected.")
