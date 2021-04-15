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
from mcbe_data.get import get as get_mcbe_data
from packet.mcbe.available_entity_identifiers_packet import available_entity_identifiers_packet
from packet.mcbe.biome_definition_list_packet import biome_definition_list_packet
from packet.mcbe.game_packet import game_packet
from packet.mcbe.creative_content_packet import creative_content_packet
from packet.mcbe.item_component_packet import item_component_packet
from packet.mcbe.login_packet import login_packet
from packet.mcbe.play_status_packet import play_status_packet
from packet.mcbe.resource_pack_client_response_packet import resource_pack_client_response_packet
from packet.mcbe.resource_pack_stack_packet import resource_pack_stack_packet
from packet.mcbe.resource_packs_info_packet import resource_packs_info_packet
from packet.mcbe.start_game_packet import start_game_packet
from packet.mcbe.packet_violation_warning_packet import packet_violation_warning_packet
from rak_net.protocol.frame import frame
import zlib

class bedrock_player:
    def __init__(self, connection, server):
        self.connection = connection
        self.server = server
        
    def send_start_game(self) -> None:
        packet: object = start_game_packet()
        packet.entity_id: int = 1
        packet.entity_runtime_id: int = 1
        packet.player_gamemode: int = 1
        packet.spawn_x: float = 0
        packet.spawn_y: float = 4
        packet.spawn_z: float = 0
        packet.pitch: int = 0
        packet.yaw: int = 0
        packet.seed: 0
        packet.spawn_biome_type: int = 0
        packet.custom_biome_name: str = "plains"
        packet.dimension: int = 0
        packet.generator: int = 2
        packet.world_gamemode: int = 1
        packet.world_spawn_x: int = 0
        packet.world_spawn_x: int = 4
        packet.world_spawn_z: int = 0
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
        packet.item_table: dict = get_mcbe_data.get_item_table()
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
        self.send_play_status(0)
        packet: object = resource_packs_info_packet()
        packet.forced_to_accept: bool = False
        packet.scripting_enabled: bool = False
        packet.encode()
        self.send_packet(packet.data)
        self.server.logger.info(f"{self.username} logged in with uuid {self.identity}.")

    def handle_resource_pack_client_response_packet(self, data: bytes) -> None:
        packet: object = resource_pack_client_response_packet(data)
        packet.decode()
        if packet.status == 0:
            packet: object = resource_pack_stack_packet()
            packet.forced_to_accept: bool = False
            packet.game_version: str = version.mcbe_version
            packet.expirement_count: int = 0
            packet.experimental: bool = False
            packet.encode()
            self.send_packet(packet.data)
        elif packet.status == 3:
            packet: object = resource_pack_stack_packet()
            packet.forced_to_accept: bool = False
            packet.game_version: str = version.mcbe_version
            packet.experiment_count: int = 0
            packet.experimental: bool = False
            packet.encode()
            self.send_packet(packet.data)
        elif packet.status == 4:
            self.server.logger.success(f"{self.username} has all packs.")
            self.send_start_game()
            self.send_item_component_packet()
            self.send_biome_definition_list_packet()
            self.send_available_entity_identifiers_packet()
            self.send_creative_content_packet()
            self.send_play_status(3)
            
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
        
    def handle_packet(self, data):
        if data[0] == mcbe_packet_ids.login_packet:
            self.handle_login_packet(data)
        elif data[0] == mcbe_packet_ids.resource_pack_client_response_packet:
            self.handle_resource_pack_client_response_packet(data)
        elif data[0] == mcbe_packet_ids.packet_violation_warning_packet:
            self.handle_packet_violation_warning_packet(data)
    
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
