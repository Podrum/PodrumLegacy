#########################################################                        
#  ____           _                                     #
# |  _ \ ___   __| |_ __ _   _ _ __ ___                 #
# | |_) / _ \ / _` | '__| | | | '_ ` _ \                #
# |  __/ (_) | (_| | |  | |_| | | | | | |               #
# |_|   \___/ \__,_|_|   \__,_|_| |_| |_|               #
#                                                       #
# Copyright 2021 Podrum Team.                           #
#                                                       #
# This file is licensed under the GPL v2.0 license.     #
# The license file is located in the root directory     #
# of the source code. If not you may not use this file. #
#                                                       #
#########################################################

import math
from podrum.event.default.player.player_join_event import player_join_event
from podrum.game_data.mcbe.item_id_map import item_id_map
from podrum.geometry.vector_2 import vector_2
from podrum.geometry.vector_3 import vector_3
from podrum.protocol.mcbe.entity.metadata_storage import metadata_storage
from podrum.protocol.mcbe.mcbe_protocol_info import mcbe_protocol_info
from podrum.protocol.mcbe.packet.available_entity_identifiers_packet import available_entity_identifiers_packet
from podrum.protocol.mcbe.packet.biome_definition_list_packet import biome_definition_list_packet
from podrum.protocol.mcbe.packet.chunk_radius_updated_packet import chunk_radius_updated_packet
from podrum.protocol.mcbe.packet.game_packet import game_packet
from podrum.protocol.mcbe.packet.creative_content_packet import creative_content_packet
from podrum.protocol.mcbe.packet.item_component_packet import item_component_packet
from podrum.protocol.mcbe.packet.level_chunk_packet import level_chunk_packet
from podrum.protocol.mcbe.packet.login_packet import login_packet
from podrum.protocol.mcbe.packet.move_player_packet import move_player_packet
from podrum.protocol.mcbe.packet.network_chunk_publisher_update_packet import network_chunk_publisher_update_packet
from podrum.protocol.mcbe.packet.packet_violation_warning_packet import packet_violation_warning_packet
from podrum.protocol.mcbe.packet.play_status_packet import play_status_packet
from podrum.protocol.mcbe.packet.resource_pack_client_response_packet import resource_pack_client_response_packet
from podrum.protocol.mcbe.packet.resource_pack_stack_packet import resource_pack_stack_packet
from podrum.protocol.mcbe.packet.resource_packs_info_packet import resource_packs_info_packet
from podrum.protocol.mcbe.packet.request_chunk_radius_packet import request_chunk_radius_packet
from podrum.protocol.mcbe.packet.set_entity_data_packet import set_entity_data_packet
from podrum.protocol.mcbe.packet.start_game_packet import start_game_packet
from podrum.protocol.mcbe.packet.text_packet import text_packet
from podrum.protocol.mcbe.packet.update_attributes_packet import update_attributes_packet
from podrum.protocol.mcbe.type.login_status_type import login_status_type
from podrum.protocol.mcbe.type.resource_pack_client_response_type import resource_pack_client_response_type
from podrum.protocol.mcbe.type.text_type import text_type
from podrum.task.immediate_task import immediate_task
from podrum.world.chunk.chunk import chunk
from rak_net.protocol.frame import frame
import zlib

class mcbe_player:
    def __init__(self, connection: object, server: object, entity_id: int) -> None:
        self.connection: object = connection
        self.server: object = server
        self.entity_id: int = entity_id
        self.world: object = server.world
        self.metadata_storage: object = metadata_storage()
        self.attributes: list = []
        self.message_format: str = "<%username> %message"
        
    def send_start_game(self) -> None:
        if not self.world.has_player(self.identity):
            self.world.create_player(self.identity)
        self.position: object = self.world.get_player_position(self.identity)
        self.position.y += 1
        packet: object = start_game_packet()
        packet.entity_id = self.entity_id
        packet.entity_runtime_id = self.entity_id
        packet.player_gamemode = 1
        packet.spawn = self.position
        packet.rotation = vector_2(0, 0)
        packet.seed = 0
        packet.spawn_biome_type = 0
        packet.custom_biome_name = "plains"
        packet.dimension = 0
        packet.generator = 2
        packet.world_gamemode = self.world.get_world_gamemode()
        packet.difficulty = 0
        packet.world_spawn = vector_3(0, 4.0, 0)
        packet.disable_achivements = False
        packet.time = 0
        packet.edu_offer = 0
        packet.edu_features = False
        packet.edu_product_id = ""
        packet.rain_level = 0
        packet.lightning_level = 0
        packet.confirmed_platform_locked = False
        packet.multiplayer_game = True
        packet.lan_broadcasting = True
        packet.xbox_live_broadcast_mode = 4
        packet.platform_broadcast_mode = 4
        packet.enable_commands = True
        packet.require_texture_pack = False
        packet.game_rules = {}
        packet.experiments = []
        packet.has_used_experiments = False
        packet.bonus_chest = False
        packet.start_map = False
        packet.permission_level = 1
        packet.chunk_tick_range = 0
        packet.locked_behavior_pack = False
        packet.locked_texture_pack = False
        packet.from_locked_template = False
        packet.only_msa_gamer_tags = False
        packet.from_world_template = False
        packet.world_template_option_locked = True
        packet.only_old_villagers = False
        packet.game_version = mcbe_protocol_info.mcbe_version
        packet.limited_world_width = 0
        packet.limited_world_height = 0
        packet.new_nether = False
        packet.experimental_gamplay = False
        packet.level_id = ""
        packet.world_name = self.world.get_world_name()
        packet.premium_world_template_id = ""
        packet.trial = False
        packet.movement_type = 0
        packet.movement_rewind_size = 0
        packet.server_authoritative_block_breaking = False
        packet.current_tick = 0
        packet.enchantment_seed = 0
        packet.item_table = item_id_map
        packet.multiplayer_correlation_id = ""
        packet.server_authoritative_inventories = False
        packet.server_engine = "Podrum"
        packet.encode()
        self.send_packet(packet.data)
        
    def send_item_component_packet(self) -> None:
        packet: object = item_component_packet()
        packet.encode()
        self.send_packet(packet.data)
        
    def send_creative_content_packet(self) -> None:
        packet: object = creative_content_packet()
        packet.entries = self.server.managers.item_manager.creative_items.values()
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
        packet.forced_to_accept = False
        packet.scripting_enabled = False
        packet.behavior_pack_infos = []
        packet.texture_pack_infos = []
        packet.encode()
        self.send_packet(packet.data)
        self.spawned: bool = False
        self.server.logger.info(f"{self.username} logged in with uuid {self.identity}.")

    def handle_resource_pack_client_response_packet(self, data: bytes) -> None:
        packet: object = resource_pack_client_response_packet(data)
        packet.decode()
        if packet.status == resource_pack_client_response_type.none:
            packet: object = resource_pack_stack_packet()
            packet.forced_to_accept = False
            packet.behavior_pack_id_versions = []
            packet.texture_pack_id_versions = []
            packet.game_version = mcbe_protocol_info.mcbe_version
            packet.expirement_count = 0
            packet.experimental = False
            packet.encode()
            self.send_packet(packet.data)
        elif packet.status == resource_pack_client_response_type.has_all_packs:
            packet: object = resource_pack_stack_packet()
            packet.forced_to_accept = False
            packet.behavior_pack_id_versions = []
            packet.texture_pack_id_versions = []
            packet.game_version = mcbe_protocol_info.mcbe_version
            packet.experiment_count = 0
            packet.experimental = False
            packet.encode()
            self.send_packet(packet.data)
        elif packet.status == resource_pack_client_response_type.completed:
            self.server.logger.success(f"{self.username} has all packs.")
            self.send_start_game()
            self.send_creative_content_packet()
            self.send_biome_definition_list_packet()
            self.send_metadata()
            self.send_attributes()
            self.send_item_component_packet()
            self.send_available_entity_identifiers_packet()
            
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
        self.view_distance: int = min(self.server.config.data["max_view_distance"], packet.chunk_radius)
        new_packet: object = chunk_radius_updated_packet()
        new_packet.chunk_radius = self.view_distance
        new_packet.encode()
        self.send_packet(new_packet.data)
        self.send_chunks()
        if not self.spawned:
            self.send_play_status(login_status_type.spawn)
            self.spawned: bool = True  
            join_event: object = player_join_event(self)
            join_event.call()
                
    def handle_move_player_packet(self, data):
        packet: object = move_player_packet(data)
        packet.decode()
        if math.floor(packet.position.x / (8 * 16)) != math.floor(self.position.x / (8 * 16)) or math.floor(packet.position.z / (8 * 16)) != math.floor(self.position.z / (8 * 16)):
            self.send_chunks()
        self.position: object = packet.position
            
    def send_message(self, message: str, xuid: str = "", needs_translation: bool = False) -> None:
        new_packet: object = text_packet()
        new_packet.type = text_type.raw
        new_packet.needs_translation = needs_translation
        new_packet.message = message
        new_packet.xuid = xuid
        new_packet.platform_chat_id = ""
        new_packet.encode()
        self.send_packet(new_packet.data)
        
    def broadcast_message(self, message: str, xuid: str = "", needs_translation: bool = False) -> None:
        self.server.send_message(message)
        for p in self.server.players.values():
            p.send_message(message, xuid, needs_translation)
            
    def send_chat_message(self, message: str) -> None:
        self.broadcast_message(self.message_format.replace("%username", self.username).replace("%message", message), self.xuid)
            
    def handle_text_packet(self, data):
        packet: object = text_packet(data)
        packet.decode()
        if packet.type == text_type.chat:
            self.send_chat_message(packet.message)
        
    def handle_packet(self, data: bytes) -> None:
        if data[0] == mcbe_protocol_info.login_packet:
            self.handle_login_packet(data)
        elif data[0] == mcbe_protocol_info.resource_pack_client_response_packet:
            self.handle_resource_pack_client_response_packet(data)
        elif data[0] == mcbe_protocol_info.packet_violation_warning_packet:
            self.handle_packet_violation_warning_packet(data)
        elif data[0] == mcbe_protocol_info.request_chunk_radius_packet:
            self.handle_request_chunk_radius_packet(data)
        elif data[0] == mcbe_protocol_info.move_player_packet:
            self.handle_move_player_packet(data)
        elif data[0] == mcbe_protocol_info.text_packet:
            self.handle_text_packet(data)
            
    def send_chunks(self) -> None:
        chunk_task: object = immediate_task(self.world.send_radius, [self.position.x, self.position.z, self.view_distance, self])
        chunk_task.start()
            
    def send_network_chunk_publisher_update(self) -> None:
        new_packet: object = network_chunk_publisher_update_packet()
        new_packet.x = math.floor(self.position.x)
        new_packet.y = math.floor(self.position.y)
        new_packet.z = math.floor(self.position.z)
        new_packet.chunk_radius = self.view_distance << 4
        new_packet.encode()
        self.send_packet(new_packet.data)
    
    def send_chunk(self, send_chunk: object) -> None:
        packet: object = level_chunk_packet()
        packet.chunk_x = send_chunk.x
        packet.chunk_z = send_chunk.z
        packet.sub_chunk_count = send_chunk.get_sub_chunk_send_count()
        packet.cache_enabled = False
        packet.chunk_data = send_chunk.network_serialize()
        packet.encode()
        self.send_packet(packet.data)

    def send_play_status(self, status: int) -> None:
        packet: object = play_status_packet()
        packet.status = status
        packet.encode()
        self.send_packet(packet.data)
        
    def send_metadata(self) -> None:
        packet: object = set_entity_data_packet()
        packet.runtime_entity_id = self.entity_id
        packet.metadata = self.metadata_storage.metadata
        packet.tick = 0
        packet.encode()
        self.send_packet(packet.data)
            
    def send_attributes(self) -> None:
        packet: object = update_attributes_packet()
        packet.runtime_entity_id = self.entity_id
        packet.attributes = self.attributes
        packet.tick = 0
        packet.encode()
        self.send_packet(packet.data)
    
    def send_packet(self, data: bytes) -> None:
        new_packet: object = game_packet()
        new_packet.write_packet_data(data)
        new_packet.encode()
        send_packet: object = frame()
        send_packet.reliability = 0
        send_packet.body = new_packet.data
        self.connection.add_to_queue(send_packet, False)
