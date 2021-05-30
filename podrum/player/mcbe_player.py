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

from geometry.vector_2 import vector_2
from geometry.vector_3 import vector_3
from mcbe_data.get import get as get_mcbe_data
from protocol.mcbe.mcbe_protocol_info import mcbe_protocol_info
from protocol.mcbe.packet.available_entity_identifiers_packet import available_entity_identifiers_packet
from protocol.mcbe.packet.biome_definition_list_packet import biome_definition_list_packet
from protocol.mcbe.packet.chunk_radius_updated_packet import chunk_radius_updated_packet
from protocol.mcbe.packet.game_packet import game_packet
from protocol.mcbe.packet.creative_content_packet import creative_content_packet
from protocol.mcbe.packet.item_component_packet import item_component_packet
from protocol.mcbe.packet.level_chunk_packet import level_chunk_packet
from protocol.mcbe.packet.login_packet import login_packet
from protocol.mcbe.packet.play_status_packet import play_status_packet
from protocol.mcbe.packet.resource_pack_client_response_packet import resource_pack_client_response_packet
from protocol.mcbe.packet.resource_pack_stack_packet import resource_pack_stack_packet
from protocol.mcbe.packet.resource_packs_info_packet import resource_packs_info_packet
from protocol.mcbe.packet.request_chunk_radius_packet import request_chunk_radius_packet
from protocol.mcbe.packet.start_game_packet import start_game_packet
from protocol.mcbe.packet.packet_violation_warning_packet import packet_violation_warning_packet
from protocol.mcbe.type.login_status_type import login_status_type
from protocol.mcbe.type.resource_pack_client_response_type import resource_pack_client_response_type
from rak_net.protocol.frame import frame
from world.chunk.chunk import chunk
import zlib

class mcbe_player:
    def __init__(self, connection, server):
        self.connection = connection
        self.server = server
        
    def send_start_game(self) -> None:
        packet: object = start_game_packet()
        packet.entity_id: int = self.entity_id
        packet.entity_runtime_id: int = self.entity_id
        packet.player_gamemode: int = 1
        packet.spawn: object = vector_3(0, 4.0, 0)
        packet.rotation: object = vector_2(0, 0)
        packet.seed: int = 0
        packet.spawn_biome_type: int = 0
        packet.custom_biome_name: str = "plains"
        packet.dimension: int = 0
        packet.generator: int = 2
        packet.world_gamemode: int = 1
        packet.difficulty: int = 0
        packet.world_spawn: object = vector_3(0, 4.0, 0)
        packet.disable_achivements: bool = False
        packet.time: int = 0
        packet.edu_offer: int = 0
        packet.edu_features: bool = False
        packet.edu_product_id: str = ""
        packet.rain_level: float = 0
        packet.lightning_level: float = 0
        packet.confirmed_platform_locked: bool = False
        packet.multiplayer_game: bool = True
        packet.lan_broadcasting: bool = True
        packet.xbox_live_broadcast_mode: int = 4
        packet.platform_broadcast_mode: int = 4
        packet.enable_commands: bool = True
        packet.require_texture_pack: bool = False
        packet.game_rules: dict = {}
        packet.experiments: int = 0
        packet.has_used_experiments: bool = False
        packet.bonus_chest: bool = False
        packet.start_map: bool = False
        packet.permission_level: int = 1
        packet.chunk_tick_range: int = 0
        packet.locked_behavior_pack: bool = False
        packet.locked_texture_pack: bool = False
        packet.from_locked_template: bool = False
        packet.only_msa_gamer_tags: bool = False
        packet.from_world_template: bool = False
        packet.world_template_option_locked: bool = True
        packet.only_old_villagers: bool = False
        packet.game_version: str = mcbe_protocol_info.mcbe_version
        packet.limited_world_width: int = 0
        packet.limited_world_height: int = 0
        packet.new_nether: bool = False
        packet.experimental_gamplay: bool = False
        packet.level_id: str = ""
        packet.world_name: str = "Podrum"
        packet.premium_world_template_id: str = ""
        packet.trial: bool = False
        packet.movement_type: int = 0
        packet.movement_rewind_size: int = 0
        packet.server_authoritative_block_breaking: bool = False
        packet.current_tick: int = 0
        packet.enchantment_seed: int = 0
        packet.item_table: dict = get_mcbe_data.get_item_table()
        packet.multiplayer_correlation_id: str = ""
        packet.server_authoritative_inventories: bool = False
        packet.encode()
        self.send_packet(packet.data)
        
    def send_item_component_packet(self) -> None:
        packet: object = item_component_packet()
        packet.encode()
        self.send_packet(packet.data)
        
    def send_creative_content_packet(self) -> None:
        packet: object = creative_content_packet()
        packet.encode()
        self.send_packet(packet.data)
             
    def send_biome_definition_list_packet(self) -> None:
        packet: object = biome_definition_list_packet()
        packet.encode()
        self.send_packet(packet.data)
        
    def send_available_entity_identifiers_packet(self) -> None:
        packet: object = available_entity_identifiers_packet()
        packet.encode()
        self.send_packet(packet.data)

    def handle_login_packet(self, data: bytes) -> None:
        packet: object = login_packet(data)
        packet.decode()
        for chain in packet.chain_data:
            if "identityPublicKey" in chain:
                self.identity_public_key: str = chain["identityPublicKey"]
            if "extraData" in chain:
                self.xuid: str = chain["extraData"]["XUID"]
                self.username: str = chain["extraData"]["displayName"]
                self.identity: str = chain["extraData"]["identity"]
        self.send_play_status(login_status_type.success)
        packet: object = resource_packs_info_packet()
        packet.forced_to_accept: bool = False
        packet.scripting_enabled: bool = False
        packet.encode()
        self.send_packet(packet.data)
        self.spawned: bool = False
        self.server.logger.info(f"{self.username} logged in with uuid {self.identity}.")

    def handle_resource_pack_client_response_packet(self, data: bytes) -> None:
        packet: object = resource_pack_client_response_packet(data)
        packet.decode()
        if packet.status == resource_pack_client_response_type.none:
            packet: object = resource_pack_stack_packet()
            packet.forced_to_accept: bool = False
            packet.game_version: str = mcbe_protocol_info.mcbe_version
            packet.expirement_count: int = 0
            packet.experimental: bool = False
            packet.encode()
            self.send_packet(packet.data)
        elif packet.status == resource_pack_client_response_type.has_all_packs:
            packet: object = resource_pack_stack_packet()
            packet.forced_to_accept: bool = False
            packet.game_version: str = mcbe_protocol_info.mcbe_version
            packet.experiment_count: int = 0
            packet.experimental: bool = False
            packet.encode()
            self.send_packet(packet.data)
        elif packet.status == resource_pack_client_response_type.completed:
            self.server.logger.success(f"{self.username} has all packs.")
            self.send_start_game()
            self.send_creative_content_packet()
            self.send_biome_definition_list_packet()
            #self.send_item_component_packet()
            #self.send_available_entity_identifiers_packet()
            
    def handle_packet_violation_warning_packet(self, data: bytes) -> None:
        packet: object = packet_violation_warning_packet(data)
        packet.decode()
        if packet.type == 0:
            error_message: str = ""
            temp: str = f", due to malformed packet ({hex(packet.violated_packet_id)})"
            if packet.severity == 0:
                error_message += f"Warning{temp}"
            elif packet.severity == 1:
                error_message += f"Final Warning{temp}"
            elif packet.severity == 2:
                error_message += f"Terminating connectinon{temp}"
            self.server.logger.error(error_message)
            if len(packet.message) > 0:
                self.server.logger.error(packet.message)
                
    def handle_request_chunk_radius_packet(self, data: bytes) -> None:
        packet: object = request_chunk_radius_packet(data)
        packet.decode()
        new_packet: object = chunk_radius_updated_packet()
        new_packet.chunk_radius: int = 1
        new_packet.encode()
        self.send_packet(new_packet.data)
        distance: int = 1
        for chunk_x in range(-distance, distance + 1):
            for chunk_z in range(-distance, distance + 1):
                send_chunk: object = chunk(chunk_x, chunk_z)
                for x in range(0, 16):
                    for z in range(0, 16):
                        y: int = 0
                        send_chunk.set_block_id(x, y, z, 7)
                        y += 1
                        send_chunk.set_block_id(x, y, z, 3)
                        y += 1
                        send_chunk.set_block_id(x, y, z, 3)
                        y += 1
                        send_chunk.set_block_id(x, y, z, 2)
                        y += 1
                send_chunk.recalculate_height_map()
                self.send_chunk(send_chunk)
        if not self.spawned:
            self.send_play_status(login_status_type.spawn)
            self.spawned: bool = True
        
    def handle_packet(self, data: bytes) -> None:
        if data[0] == mcbe_protocol_info.login_packet:
            self.handle_login_packet(data)
        elif data[0] == mcbe_protocol_info.resource_pack_client_response_packet:
            self.handle_resource_pack_client_response_packet(data)
        elif data[0] == mcbe_protocol_info.packet_violation_warning_packet:
            self.handle_packet_violation_warning_packet(data)
        elif data[0] == mcbe_protocol_info.request_chunk_radius_packet:
            self.handle_request_chunk_radius_packet(data)
    
    def send_chunk(self, send_chunk: object) -> None:
        packet: object = level_chunk_packet()
        packet.chunk_x: int = send_chunk.x
        packet.chunk_z: int = send_chunk.z
        packet.sub_chunk_count: int = send_chunk.get_sub_chunk_send_count()
        packet.cache_enabled: bool = False
        packet.chunk_data: bytes = send_chunk.encode()
        packet.encode()
        self.send_packet(packet.data)

    def send_play_status(self, status: int) -> None:
        packet: object = play_status_packet()
        packet.status: int = status
        packet.encode()
        self.send_packet(packet.data)
    
    def send_packet(self, data: bytes) -> None:
        new_packet: object = game_packet()
        new_packet.write_packet_data(data)
        new_packet.encode()
        send_packet: object = frame()
        send_packet.reliability: int = 0
        send_packet.body: bytes = new_packet.data
        self.connection.add_to_queue(send_packet, False)
