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
from packet.mcbe.game_packet import game_packet
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
        
    def send_start_game(self):
        packet: object = start_game_packet()
        packet.entity_id: int = 0
        packet.entity_runtime_id: int = 0
        packet.player_gamemode: int = 1
        packet.spawn: dict = {"x": 0, "y": 80, "z": 0}
        packet.rotation: dict = {"x": 0, "y": 0}
        packet.seed: int = 0
        packet.spawn_biome_type: int = 0
        packet.custom_biome_name: str = ""
        packet.dimension: int = 0
        packet.generator: int = 0
        packet.world_gamemode: int = 0
        packet.difficulty: int = 0
        packet.world_spawn: dict = {"x": 0, "y": 80, "z": 0}
        packet.has_achivements_disabled: bool = True
        packet.time: int = 0
        packet.edu_offer: int = 0
        packet.has_education_features_enabled: bool = False
        packet.education_production_id: str = ""
        packet.rain_level: float = 0
        packet.lighting_level: float = 0
        packet.has_confirmed_platform_locked_content: bool = False
        packet.is_multiplayer: bool = True
        packet.broadcast_to_lan: bool = True
        packet.xbox_live_broadcast_mode: int = 4
        packet.platform_broadcast_mode: int = 4
        packet.enable_commands: bool = True
        packet.are_texture_packs_required: bool = False
        packet.game_rules: list = {}
        packet.experiments: int = 0
        packet.has_used_experiments: bool = False
        packet.bonus_chest: bool = False
        packet.map_enabled: bool = False
        packet.permission_level: int = 0
        packet.server_chunk_tick_range: int = 0
        packet.has_locked_behavior_pack: bool = False
        packet.has_locked_resource_pack: bool = False
        packet.is_from_locked_world_template: bool = False
        packet.use_msa_gametags_only: bool = False
        packet.is_from_world_template: bool = False
        packet.is_world_template_option_locked: bool = True
        packet.only_v_1_villagers: bool = False
        packet.game_version: string = version.mcbe_version
        packet.limited_world_width: int = 16
        packet.limited_world_height: int = 16
        packet.is_nether_type: bool = False
        packet.is_force_experimental_gameplay: bool = False
        packet.level_id: str = ""
        packet.world_name: str = ""
        packet.premium_world_template: str = ""
        packet.is_trial: bool = False
        packet.movement_type: int = 0
        packet.movement_rewind_history_size: int = 0
        packet.enable_new_block_break_system: bool = False
        packet.current_tick: int = 0
        packet.enchantment_seed: int = 0
        packet.item_table: dict = get_mcbe_data.get_item_table()
        packet.multiplayer_correction_id: str = ""
        packet.new_inventory: bool = False
        packet.encode()
        self.send_packet(packet.data)

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
            packet.game_version: str = version.mcbe_version
            packet.expirement_count: int = 0
            packet.experimental: bool = False
            packet.encode()
            self.send_packet(packet.data)
        elif packet.status == 3:
            packet: object = resource_pack_stack_packet()
            packet.forced_to_accept: bool = False
            packet.game_version: str = version.mcbe_version
            packet.expirement_count: int = 0
            packet.experimental: bool = False
            packet.encode()
            self.send_packet(packet.data)
        elif packet.status == 4:
            self.server.logger.success(f"{self.username} has all packs.")
            self.send_start_game()
            
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
        self.connection.add_to_queue(send_packet)
