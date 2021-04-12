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
from packet.mcbe.packet import packet

class start_game_packet(packet):
    def __init__(self, data: bytes = b"", pos: int = 0) -> None:
        super().__init__(data, pos)
        self.packet_id: int = mcbe_packet_ids.start_game_packet

    def decode_payload(self):
        pass
          
    """def encode_payload(self):
        self.write_signed_var_long(self.entity_id)
        self.write_var_long(self.entity_runtime_id)
        self.write_signed_var_int(self.player_gamemode)
        self.write_vector_3(self.spawn)
        self.write_vector_2(self.rotation)
        #ifndef LEVEL_SETTINGS
        self.write_signed_var_int(self.seed)
        self.write_short_le(self.spawn_biome_type)
        self.write_string(self.custom_biome_name)
        self.write_signed_var_int(self.dimension)
        self.write_signed_var_int(self.generator)
        self.write_signed_var_int(self.world_gamemode)
        self.write_signed_var_int(self.difficulty)
        self.write_block_coordinates(self.world_spawn)
        self.write_bool(self.has_achivements_disabled)
        self.write_signed_var_int(self.time)
        self.write_signed_var_int(self.edu_offer)
        self.write_bool(self.has_education_features_enabled)
        self.write_string(self.education_production_id)
        self.write_float_le(self.rain_level)
        self.write_float_le(self.lighting_level)
        self.write_bool(self.has_confirmed_platform_locked_content)
        self.write_bool(self.is_multiplayer)
        self.write_bool(self.broadcast_to_lan)
        self.write_signed_var_int(self.xbox_live_broadcast_mode)
        self.write_signed_var_int(self.platform_broadcast_mode)
        self.write_bool(self.enable_commands)
        self.write_bool(self.are_texture_packs_required)
        self.write_game_rules(self.game_rules)
        self.write_int_le(self.experiments)
        self.write_bool(self.has_used_experiments)
        self.write_bool(self.bonus_chest)
        self.write_bool(self.map_enabled)
        self.write_signed_var_int(self.permission_level)
        self.write_int_le(self.server_chunk_tick_range)
        self.write_bool(self.has_locked_behavior_pack)
        self.write_bool(self.has_locked_resource_pack)
        self.write_bool(self.is_from_locked_world_template)
        self.write_bool(self.use_msa_gametags_only)
        self.write_bool(self.is_from_world_template)
        self.write_bool(self.is_world_template_option_locked)
        self.write_bool(self.only_v_1_villagers)
        self.write_string(self.game_version)
        #endif LEVEL_SETTINGS
        self.write_int_le(self.limited_world_width)
        self.write_int_le(self.limited_world_height)
        self.write_bool(self.is_nether_type)
        self.write_bool(self.is_force_experimental_gameplay)
        self.write_string(self.level_id)
        self.write_string(self.world_name)
        self.write_string(self.premium_world_template)
        self.write_bool(self.is_trial)
        self.write_var_int(self.movement_type)
        self.write_signed_var_int(self.movement_rewind_history_size)
        self.write_bool(self.enable_new_block_break_system)
        self.write_unsigned_long_le(self.current_tick)
        self.write_signed_var_int(self.enchantment_seed)
        self.write_var_int(0) # Block Pallet
        self.write_var_int(0) # Item Pallet
        #for string_id, numeric_id in self.item_table.items():
            #self.write_string(string_id)
            #self.write_short_le(numeric_id)
            #self.write_bool(False)
        self.write_string(self.multiplayer_correction_id)
        self.write_bool(self.new_inventory)
"""
    def encode_payload(self):
        self.write_signed_var_long(self.entity_id)
        self.write_var_long(self.entity_runtime_id)

        self.write_signed_var_int(0) # game mode

        # vector 3
        self.write_float_le(0)
        self.write_float_le(4)
        self.write_float_le(0)

        self.write_float_le(0) # pitch
        self.write_float_le(0) # yaw

        self.write_signed_var_int(0) #  seed

        self.write_short_le(0) # default biome type
        self.write_string('plains') # biome name
        self.write_signed_var_int(0) # dimension

        self.write_signed_var_int(2) # generator
        self.write_signed_var_int(0) # world gamemode
        self.write_signed_var_int(0) # difficulty

        # world spawn vector 3
        self.write_signed_var_int(0)
        self.write_var_int(4)
        self.write_signed_var_int(0)

        self.write_byte(1) # achievement disabled

        self.write_signed_var_int(0) # day cycle / time
        self.write_signed_var_int(0) # edu edition offer
        self.write_byte(0) # edu features
        self.write_string('') # edu product id

        self.write_float_le(0) # rain lvl
        self.write_float_le(0) # lightning lvl

        self.write_byte(0) # confirmed platform locked
        self.write_byte(1) # multi player game
        self.write_byte(1) # broadcast to lan

        self.write_signed_var_int(4) # xbl broadcast mode
        self.write_signed_var_int(4) # platform broadcast mode

        self.write_byte(1) # commands enabled
        self.write_byte(0) # texture required

        self.write_var_int(0) # game rules length

        self.write_int_le(0) # experiments
        self.write_byte(0) # has used experiments?

        self.write_byte(0) # bonus chest
        self.write_byte(0) # start with chest

        self.write_signed_var_int(1) # player perms

        self.write_int_le(4) # chunk tick range
        self.write_byte(0) # locked behavior
        self.write_byte(0) # locked texture
        self.write_byte(0) # from locked template
        self.write_byte(0) # msa gamer tags only
        self.write_byte(0) # from world template
        self.write_byte(0) # world template option locked
        self.write_byte(1) # only spawn v1 villagers
        self.write_string('1.16.210') # vanilla version
        self.write_int_le(0) # limited world height
        self.write_int_le(0) # limited world length
        self.write_bool(False) # has new nether
        self.write_bool(False) # experimental gameplay

        self.write_string('') # random level uuid
        self.write_string('test') # world name
        self.write_string('') # template content identity

        self.write_byte(0) # is trial
        self.write_var_int(0) # movement type
        self.write_signed_var_int(0) # movement rewind history size
        self.write_byte(0) # new block break system
        self.write_long_le(0) # level time

        self.write_signed_var_int(0) # enchantment seed

        self.write_var_int(0) # block pallet
        self.write_var_int(0) # item pallete

        #for string_id, numeric_id in self.item_table.items():
        #    self.write_string(string_id)
        #    self.write_short_le(numeric_id)
        #    self.write_bool(False)

        self.write_string('')
        self.write_bool(False)
