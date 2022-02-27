r"""
  ____           _
 |  _ \ ___   __| |_ __ _   _ _ __ ___
 | |_) / _ \ / _` | '__| | | | '_ ` _ \
 |  __/ (_) | (_| | |  | |_| | | | | | |
 |_|   \___/ \__,_|_|   \__,_|_| |_| |_|

 Copyright 2021 Podrum Team.

 This file is licensed under the GPL v2.0 license.
 The license file is located in the root directory
 of the source code. If not you may not use this file.
"""

from podrum.protocol.mcbe.mcbe_protocol_info import mcbe_protocol_info
from podrum.protocol.mcbe.packet.mcbe_packet import mcbe_packet


class start_game_packet(mcbe_packet):
    def __init__(self, data: bytes = b"", pos: int = 0) -> None:
        super().__init__(data, pos)

        self.multiplayer_game = None
        self.lan_broadcasting = None
        self.xbox_live_broadcast_mode = None
        self.platform_broadcast_mode = None
        self.enable_commands = None
        self.require_texture_pack = None
        self.game_rules = None
        self.experiments = None
        self.has_used_experiments = None
        self.bonus_chest = None
        self.start_map = None
        self.permission_level = None
        self.chunk_tick_range = None
        self.locked_behavior_pack = None
        self.locked_texture_pack = None
        self.from_locked_template = None
        self.only_msa_gamer_tags = None
        self.from_world_template = None
        self.world_template_option_locked = None
        self.only_old_villagers = None
        self.game_version = None
        self.limited_world_width = None
        self.limited_world_height = None
        self.new_nether = None
        self.edu_shared_uri_resource_bottom_name = None
        self.edu_shared_uri_resource_uri_link = None
        self.experimental_gameplay = None
        self.level_id = None
        self.world_name = None
        self.premium_world_template_id = None
        self.trial = None
        self.movement_type = None
        self.movement_rewind_size = None
        self.server_authoritative_block_breaking = None
        self.current_tick = None
        self.enchantment_seed = None
        self.item_states = None
        self.multiplayer_correlation_id = None
        self.server_authoritative_inventories = None
        self.server_engine = None

        self.entity_id = None
        self.entity_runtime_id = None
        self.player_gamemode = None
        self.spawn = None
        self.rotation = None
        self.seed = None
        self.spawn_biome_type = None

        self.packet_id: int = mcbe_protocol_info.start_game_packet

    def decode_payload(self):
        pass
        
    def encode_payload(self):
        self.write_signed_var_long(self.entity_id)
        self.write_var_long(self.entity_runtime_id)
        self.write_signed_var_int(self.player_gamemode)
        self.write_vector_3_float(self.spawn)
        self.write_vector_2_float(self.rotation)
        self.write_signed_var_int(self.seed)
        self.write_short_le(self.spawn_biome_type)
        self.write_string(self.custom_biome_name)
        self.write_signed_var_int(self.dimension)
        self.write_signed_var_int(self.generator)
        self.write_signed_var_int(self.world_gamemode)
        self.write_signed_var_int(self.difficulty)
        self.write_block_coordinates(self.world_spawn)
        self.write_byte(self.disable_achievements)
        self.write_signed_var_int(self.time)
        self.write_signed_var_int(self.edu_offer)
        self.write_byte(self.edu_features)
        self.write_string(self.edu_product_id)
        self.write_float_le(self.rain_level)
        self.write_float_le(self.lightning_level)
        self.write_bool(self.confirmed_platform_locked)
        self.write_bool(self.multiplayer_game)
        self.write_bool(self.lan_broadcasting)
        self.write_signed_var_int(self.xbox_live_broadcast_mode)
        self.write_signed_var_int(self.platform_broadcast_mode)
        self.write_bool(self.enable_commands)
        self.write_bool(self.require_texture_pack)
        self.write_game_rules(self.game_rules)
        self.write_experiments(self.experiments)
        self.write_bool(self.has_used_experiments)
        self.write_bool(self.bonus_chest)
        self.write_bool(self.start_map)
        self.write_signed_var_int(self.permission_level)
        self.write_int_le(self.chunk_tick_range)
        self.write_bool(self.locked_behavior_pack)
        self.write_bool(self.locked_texture_pack)
        self.write_bool(self.from_locked_template)
        self.write_bool(self.only_msa_gamer_tags)
        self.write_bool(self.from_world_template)
        self.write_bool(self.world_template_option_locked)
        self.write_bool(self.only_old_villagers)
        self.write_string(self.game_version)
        self.write_int_le(self.limited_world_width)
        self.write_int_le(self.limited_world_height)
        self.write_bool(self.new_nether)
        self.write_string(self.edu_shared_uri_resource_bottom_name)
        self.write_string(self.edu_shared_uri_resource_uri_link)
        self.write_bool(self.experimental_gameplay)
        self.write_string(self.level_id)
        self.write_string(self.world_name)
        self.write_string(self.premium_world_template_id)
        self.write_bool(self.trial)
        self.write_var_int(self.movement_type)
        self.write_signed_var_int(self.movement_rewind_size)
        self.write_bool(self.server_authoritative_block_breaking)
        self.write_long_le(self.current_tick)
        self.write_signed_var_int(self.enchantment_seed)
        self.write_var_int(0)  # block states length
        self.write_item_states(self.item_states)
        self.write_string(self.multiplayer_correlation_id)
        self.write_bool(self.server_authoritative_inventories)
        self.write_string(self.server_engine)
        self.write_long_le(0)
