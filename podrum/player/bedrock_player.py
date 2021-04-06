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
from constant.version import version
from packet.mcbe.game_packet import game_packet
from packet.mcbe.login_packet import login_packet
from packet.mcbe.play_status_packet import play_status_packet
from packet.mcbe.resource_pack_client_response_packet import resource_pack_client_response_packet
from packet.mcbe.resource_pack_stack_packet import resource_pack_stack_packet
from packet.mcbe.resource_packs_info_packet import resource_packs_info_packet
from rak_net.protocol.frame import frame
import zlib

class bedrock_player:
    def __init__(self, connection, server):
        self.connection = connection
        self.server = server

    def handle_login_packet(self, data: bytes):
        packet: object = login_packet(data)
        packet.decode()
        for chain in packet.chain_data:
            if "identityPublicKey" in chain:
                self.identity_public_key: str = chain["identityPublicKey"]
            if "extraData" in chain:
                self.xuid: str = chain["extraData"]["XUID"]
                self.username: str = chain["extraData"]["displayName"]
                self.identity: str = chain["extraData"]["identity"]
        self.send_play_status(0)
        packet: object = resource_packs_info_packet()
        packet.forced_to_accept: bool = False
        packet.scripting_enabled: bool = False
        packet.encode()
        self.send_packet(packet.data)
        self.server.logger.info(f"{self.username} logged in with uuid {self.identity}.")

    def handle_resource_pack_client_response_packet(self, data):
        packet: object = resource_pack_client_response_packet(data)
        packet.decode()
        if packet.status == 0:
            packet: object = resource_pack_stack_packet()
            packet.forced_to_accept: bool = False
            packet.experimental: bool = False
            packet.game_version: str = version.mcbe_version
            packet.encode()
            self.send_packet(packet.data)
        elif packet.status == 3:
            pass # Start Game
        
    def handle_packet(self, data):
        if data[0] == mcbe_packet_ids.login_packet:
            self.handle_login_packet(data)
        elif data[0] == mcbe_packet_ids.resource_pack_client_response_packet:
            self.handle_resource_pack_client_response_packet(data)
    
    def send_play_status(self, status):
        packet: object = play_status_packet()
        packet.status: int = status
        packet.encode()
        self.send_packet(packet.data)
    
    def send_packet(self, data):
        new_packet: object = game_packet()
        new_packet.write_packet_data(data)
        new_packet.encode()
        send_packet: object = frame()
        send_packet.reliability: int = 0
        send_packet.body: bytes = new_packet.data
        self.connection.add_to_queue(send_packet, False)
