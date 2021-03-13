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

from constant.misc import misc
from constant.raknet_packet_ids import raknet_packet_ids
from constant.version import version
from packet.raknet.acknowledgement import acknowledgement
from packet.raknet.connection_request import connection_request
from packet.raknet.connection_request_accepted import connection_request_accepted
from packet.raknet.frame import frame
from packet.raknet.frame_set import frame_set
from packet.raknet.game_packet import game_packet
from packet.raknet.incompatible_protocol_version import incompatible_protocol_version
from packet.raknet.new_incoming_connection import new_incoming_connection
from packet.raknet.offline_ping import offline_ping
from packet.raknet.offline_pong import offline_pong
from packet.raknet.online_ping import online_ping
from packet.raknet.online_pong import online_pong
from packet.raknet.open_connection_reply_1 import open_connection_reply_1
from packet.raknet.open_connection_reply_2 import open_connection_reply_2
from packet.raknet.open_connection_request_1 import open_connection_request_1
from packet.raknet.open_connection_request_2 import open_connection_request_2
import random
import sys
from threading import Thread
import time
from utils.context import context
from utils.raknet_address import raknet_address
from utils.raknet_reliability import raknet_reliability
from utils.udp_server_socket import udp_server_socket

class raknet_handler(Thread):
    def __init__(self, server: object, host: str, port: int, name: str) -> None:
        super().__init__()
        self.server: object = server
        self.host: str = host
        self.port: int = port
        self.socket: object = udp_server_socket(host, port)
        self.guid: int = random.randint(0, sys.maxsize)
        self.name: str = "MCPE;Dedicated Server;390;1.14.60;0;10;13253860892328930865;Bedrock level;Survival;1;19132;19133;" # name
        self.connections: dict = {}

    def create_connection(self, address, mtu_size) -> None:
        self.connections[address.token]: object = context()
        self.connections[address.token].address: object = address
        self.connections[address.token].mtu_size: int = mtu_size
        self.connections[address.token].connected: bool = False
        self.connections[address.token].recovery_queue: dict = {}
        self.connections[address.token].ack_queue: list = []
        self.connections[address.token].nack_queue: list = []
        self.connections[address.token].fragmented_packets: dict = {}
        self.connections[address.token].compound_id: int = 0
        self.connections[address.token].client_sequence_numbers: list = []
        self.connections[address.token].server_sequence_number: int = 0
        self.connections[address.token].client_sequence_number: int = 0
        self.connections[address.token].server_reliable_frame_index: int = 0
        self.connections[address.token].client_reliable_frame_index: int = 0
        self.connections[address.token].queue: object = frame_set()
        self.connections[address.token].queue.packet_id: int = raknet_packet_ids.frame_set_0
        self.connections[address.token].channel_index: list = [0] * 32

    def handle_offline_ping(self, data: bytes, address: object) -> None:
        packet: object = offline_ping(data)
        packet.read_data()
        if packet.magic == misc.raknet_magic:
            new_packet: object = offline_pong()
            new_packet.packet_id: int = raknet_packet_ids.offline_pong
            new_packet.client_timestamp: int = packet.client_timestamp
            new_packet.server_guid: int = self.guid
            new_packet.magic: bytes = misc.raknet_magic
            new_packet.server_name: str = self.name
            new_packet.write_data()
            self.socket.send(new_packet.data, address.host, address.port)

    def handle_offline_ping(self, data: bytes, address: object) -> None:
        packet: object = offline_ping(data)
        packet.read_data()
        if packet.magic == misc.raknet_magic:
            new_packet: object = offline_pong()
            new_packet.packet_id: int = raknet_packet_ids.offline_pong
            new_packet.client_timestamp: int = packet.client_timestamp
            new_packet.server_guid: int = self.guid
            new_packet.magic: bytes = misc.raknet_magic
            new_packet.server_name: str = self.name
            new_packet.write_data()
            self.socket.send(new_packet.data, address.host, address.port)

    def handle_open_connection_request_1(self, data: bytes, address: object) -> None:
        packet: object = open_connection_request_1(data)
        packet.read_data()
        if packet.magic == misc.raknet_magic:
            if packet.protocol_version in version.raknet_protocol_versions:
                new_packet: object = open_connection_reply_1()
                new_packet.packet_id: int = raknet_packet_ids.open_connection_reply_1
                new_packet.magic: bytes = misc.raknet_magic
                new_packet.server_guid: int = self.guid
                new_packet.use_security: bool = False
                new_packet.mtu_size: int = packet.mtu_size
            else:
                new_packet: object = incompatible_protocol_version()
                new_packet.packet_id: int = raknet_packet_ids.incompatible_protocol_version
                new_packet.protocol_version: int = packet.protocol_version
                new_packet.magic: bytes = misc.raknet_magic
                new_packet.server_guid: int = self.guid
            new_packet.write_data()
            self.socket.send(new_packet.data, address.host, address.port)

    def handle_open_connection_request_2(self, data: bytes, address: object) -> None:
        packet: object = open_connection_request_2(data)
        packet.read_data()
        if packet.magic == misc.raknet_magic:
            new_packet: object = open_connection_reply_2()
            new_packet.packet_id: int = raknet_packet_ids.open_connection_reply_2
            new_packet.magic: bytes = misc.raknet_magic
            new_packet.server_guid: int = self.guid
            new_packet.client_address: object = address
            new_packet.mtu_size: int = packet.mtu_size
            new_packet.use_encryption: bool = False
            new_packet.write_data()
            self.socket.send(new_packet.data, address.host, address.port)
            self.create_connection(address, packet.mtu_size)
            
    def handle_frame_set(self, data: bytes, address: object) -> None:
        connection: object = self.connections[address.token]
        packet: object = frame_set(data)
        packet.read_data()
        if packet.sequence_number not in connection.client_sequence_numbers:
            if packet.sequence_number in connection.nack_queue:
                connection.nack_queue.remove(packet.sequence_number)
            connection.client_sequence_numbers.append(packet.sequence_number)
            connection.ack_queue.append(packet.sequence_number)
            hole_size: int = packet.sequence_number - connection.client_sequence_number
            if hole_size > 0:
                for sequence_number in range(connection.client_sequence_number + 1, hole_size):
                    if sequence_number not in connection.client_sequence_numbers:
                        connection.nack_queue.append(sequence_number)
            connection.client_sequence_number: int = packet.sequence_number
            for frame_from_set in packet.frames:
                if not raknet_reliability.reliable(frame_from_set.reliability):
                    self.handle_frame(frame_from_set, address)
                else:
                    hole_size: int = frame_from_set.reliable_frame_index - connection.client_reliable_frame_index
                    if hole_size == 0:
                        self.handle_frame(frame_from_set, address)
                        connection.client_reliable_frame_index += 1
    
    def handle_ack(self, data: bytes, address: object) -> None:
        connection: object = self.connections[address.token]
        packet: object = acknowledgement(data)
        packet.read_data()
        for sequence_number in packet.sequence_numbers:
            if sequence_number in connection.recovery_queue:
                del connection.recovery_queue[sequence_number]
    
    def handle_nack(self, data: bytes, address: object) -> None:
        connection: object = self.connections[address.token]
        packet: object = acknowledgement(data)
        packet.read_data()
        for sequence_number in packet.sequence_numbers:
            if sequence_number in connection.recovery_queue:
                lost_packet: object = connection.recovery_queue[sequence_number]
                lost_packet.sequence_number: int = connection.server_sequence_number
                connection.server_sequence_number += 1
                lost_packet.write_data()
                self.socket.send(lost_packet.data, address.host, address.port)
                del connection.recovery_queue[sequence_number]

    def handle_connection_request(self, data, address):
        packet: object = connection_request(data)
        packet.read_data()
        new_packet: object = connection_request_accepted()
        new_packet.packet_id: int = raknet_packet_ids.connection_request_accepted
        new_packet.client_address: object = address
        new_packet.system_index: int = 0
        new_packet.system_addresses: list = [raknet_address("255.255.255.255", 19132)] * 20
        new_packet.request_timestamp: int = packet.request_timestamp
        new_packet.accepted_timestamp: int = int(time.time())
        new_packet.write_data()
        frame_to_send: object = frame()
        frame_to_send.reliability: int = 0
        frame_to_send.body: bytes = new_packet.data
        self.add_to_queue(frame_to_send, address)

    def handle_new_incoming_connection(self, data, address):
        connection: object = self.connections[address.token]
        packet: object = new_incoming_connection(data)
        packet.read_data()
        if packet.server_address.port == self.port:
            connection.connected: bool = True
            self.server.event_manager.dispatch("new_incoming_connection", address)

    def handle_online_ping(self, data, address):
        packet: object = online_ping(data)
        packet.read_data()
        new_packet: object = online_pong()
        new_packet.packet_id: int = raknet_packet_ids.online_pong
        new_packet.client_timestamp: int = packet.client_timestamp
        new_packet.server_timestamp: int = int(time.time())
        new_packet.write_data()
        frame_to_send: object = frame()
        frame_to_send.reliability: int = 0
        frame_to_send.body: bytes = new_packet.data
        self.add_to_queue(frame_to_send, address, False)

    def handle_fragmented_frame(self, packet: object, address: object) -> None:
        connection: object = self.connections[address.token]
        if packet.compound_id not in connection.fragmented_packets:
            connection.fragmented_packets[packet.compound_id]: dict = {packet.index: packet}
        else:
            connection.fragmented_packets[packet.compound_id][packet.index]: int = packet
        if len(connection.fragmented_packets[packet.compound_id]) == packet.compound_size:
            new_frame: object = frame()
            new_frame.body: bytes = b""
            for i in range(0, packet.compound_size):
                new_frame.body += connection.fragmented_packets[packet.compound_id][i].body
            del connection.fragmented_packets[packet.compound_id]
            self.handle_frame(new_frame, address)
        
    def handle_frame(self, packet: object, address: object) -> None:
        connection: object = self.connections[address.token]
        if packet.fragmented:
            self.handle_fragmented_frame(packet, address)
        else:
            if not connection.connected:
                if packet.body[0] == raknet_packet_ids.connection_request:
                    self.handle_connection_request(packet.body, address)
                elif packet.body[0] == raknet_packet_ids.new_incoming_connection:
                    self.handle_new_incoming_connection(packet.body, address)
            elif packet.body[0] == raknet_packet_ids.online_ping:
                self.handle_online_ping(packet.body, address)
            elif packet.body[0] == raknet_packet_ids.disconnect:
                self.disconnect(address)
            else:
                self.server.event_manager.dispatch("packet_data", packet.body, address)

    def send_queue(self, address: object) -> None:
        connection: object = self.connections[address.token]
        if len(connection.queue.frames) > 0:
            connection.queue.sequence_number: int = connection.server_sequence_number
            connection.server_sequence_number += 1
            connection.recovery_queue[connection.queue.sequence_number]: object = connection.queue
            connection.queue.write_data()
            self.socket.send(connection.queue.data, address.host, address.port)
            connection.queue.frames: list = []
                
    def add_to_queue(self, packet: object, address: object, is_imediate: bool = True) -> None:
        connection: object = self.connections[address.token]
        if raknet_reliability.reliable(packet.reliability):
            packet.reliable_frame_index: int = connection.server_reliable_frame_index
            connection.server_reliable_frame_index += 1
            if packet.reliability == 3:
                packet.ordered_frame_index: int = connection.channel_index[packet.order_channel]
                connection.channel_index[packet.order_channel] += 1
        max_data_size = connection.mtu_size - 28
        if packet.get_size() > max_data_size:
            fragmented_body = []
            for i in range(0, len(packet.body), max_data_size):
                fragmented_body.append(packet.body[i:i + max_data_size])
            for index, body in enumerate(fragmented_body):
                new_packet: object = frame()
                new_packet.reliability: int = packet.reliability
                new_packet.compound_id: int = connection.compound_id
                new_packet.compound_size: int = len(fragmented_data)
                new_packet.index: int = index
                new_packet.body: bytes = body
                if index != 0:
                    new_packet.reliable_frame_index: int = connection.server_reliable_frame_index
                    connection.server_reliable_frame_index += 1
                if new_packet.reliability == 3:
                    new_packet.ordered_frame_index: int = packet.ordered_frame_index
                    new_packet.order_channel: int = packet.order_channel
                if is_imediate:
                    connection.queue.frames.append(packet)
                    self.send_queue(address)
                else:
                    frame_size: int = new_packet.get_size()
                    queue_size: int = connection.queue.get_size()
                    if frame_size + queue_size >= max_data_size:
                        self.send_queue(address)
                    connection.queue.frames.append(new_packet)
        else:
            if is_imediate:
                connection.queue.frames.append(packet)
                self.send_queue(address)
            else:
                frame_size: int = packet.get_size()
                queue_size: int = connection.queue.get_size()
                if frame_size + queue_size >= max_data_size:
                    self.send_queue(address)
                connection.queue.frames.append(packet)
            
    def send_ack_queue(self, address: object) -> None:
        connection: object = self.connections[address.token]
        if len(connection.ack_queue) > 0:
            packet: object = acknowledgement()
            packet.packet_id: int = raknet_packet_ids.ack
            packet.sequence_numbers: list = connection.ack_queue
            packet.write_data()
            self.socket.send(packet.data, address.host, address.port)
            connection.ack_queue: list = []
    
    def send_nack_queue(self, address: object) -> None:
        connection: object = self.connections[address.token]
        if len(connection.ack_queue) > 0:
            packet: object = acknowledgement()
            packet.packet_id: int = raknet_packet_ids.nack
            packet.sequence_numbers: list = connection.nack_queue
            packet.write_data()
            self.socket.send(packet.data, address)
            connection.nack_queue: list = []

    def handle_packet(self, data: bytes, address: object) -> None:
        if address.token in self.connections:
            if raknet_packet_ids.frame_set_0 <= data[0] <= raknet_packet_ids.frame_set_f:
                self.handle_frame_set(data, address)
            elif data[0] == raknet_packet_ids.ack:
                self.handle_ack(data, address)
            elif data[0] == raknet_packet_ids.nack:
                self.handle_nack(data, address)
        elif data[0] == raknet_packet_ids.offline_ping or data[0] == raknet_packet_ids.offline_ping_open_connections:
            self.handle_offline_ping(data, address)
        elif data[0] == raknet_packet_ids.open_connection_request_1:
            self.handle_open_connection_request_1(data, address)
        elif data[0] == raknet_packet_ids.open_connection_request_2:
            self.handle_open_connection_request_2(data, address)
            
    def disconnect(self, address):
        packet = frame()
        packet.reliability = 0
        packet.body = b"\x13"
        self.add_to_queue(packet, address)
        del self.connections[address.token]
        self.server.event_manager.dispatch("raknet_disconnect", address)

    def start_handler(self) -> None:
        self.stopped: bool = False
        self.start()

    def stop_handler(self) -> None:
        self.stopped: bool = True

    def run(self) -> None:
        while not self.stopped:
            recv = self.socket.receive()
            self.handle_packet(recv[0], raknet_address(recv[1][0], recv[1][1]))
            for connection in dict(self.connections).values():
                self.send_ack_queue(connection.address)
                self.send_nack_queue(connection.address)
                self.send_queue(connection.address)
