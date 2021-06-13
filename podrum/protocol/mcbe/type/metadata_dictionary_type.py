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

class metadata_dictionary_type:
    key_flags: int = 0
    key_health: int = 1
    key_variant: int = 2
    key_color: int = 3
    key_nametag: int = 4
    key_owner_eid: int = 5
    key_target_eid: int = 6
    key_air: int = 7
    key_potion_color: int = 8
    key_potion_ambient: int = 9
    key_jump_duration: int = 10
    key_hurt_time: int = 11
    key_hurt_direction: int = 12
    key_paddle_time_left: int = 13
    key_paddle_time_right: int = 14
    key_experience_value: int = 15
    key_minecart_display_block: int = 16
    key_minecart_display_offset: int = 17
    key_minecart_has_display: int = 18
    key_old_swell: int = 20
    key_swell_dir: int = 21
    key_charge_amount: int = 22
    key_enderman_held_runtime_id: int = 23
    key_entity_age: int = 24
    key_player_flags: int = 26
    key_player_index: int = 27
    key_player_bed_position: int = 28
    key_fireball_power_x: int = 29
    key_fireball_power_y: int = 30
    key_fireball_power_z: int = 31
    key_aux_power: int = 32
    key_fish_x: int = 33
    key_fish_z: int = 34
    key_fish_angle: int = 35
    key_potion_aux_value: int = 36
    key_lead_holder_eid: int = 37
    key_scale: int = 38
    key_interactive_tag: int = 39
    key_npc_skin_id: int = 40
    key_url_tag: int = 41
    key_max_air: int = 42
    key_mark_variant: int = 43
    key_container_type: int = 44
    key_container_base_size: int = 45
    key_container_extra_slots_per_strength: int = 46
    key_block_target: int = 47
    key_wither_invulnerable_ticks: int = 48
    key_wither_target_1: int = 49
    key_wither_target_2: int = 50
    key_wither_target_3: int = 51
    key_aerial_attack: int = 52
    key_boundingbox_width: int = 53
    key_boundingbox_height: int = 54
    key_fuse_length: int = 55
    key_rider_seat_position: int = 57
    key_rider_rotation_locked: int = 58
    key_rider_max_rotation: int = 58
    key_rider_min_rotation: int = 59
    key_rider_rotation_offset: int = 60
    key_area_effect_clound_radius: int = 61
    key_area_effect_clound_waiting: int = 62
    key_area_effect_clound_particle_id: int = 63
    key_shulker_peak_id: int = 64
    key_shulker_attach_face: int = 65
    key_shulker_attached: int = 66
    key_shulker_attach_pos: int = 67
    key_trading_player_eid: int = 68
    key_trading_career: int = 69
    key_has_command_block: int = 70
    key_command_block_command: int = 71
    key_command_block_last_output: int = 72
    key_command_block_track_output: int = 73
    key_controlling_rider_seat_number: int = 74
    key_strength: int = 75
    key_max_strength: int = 76
    key_spell_casting_color: int = 77
    key_limited_life: int = 78
    key_armor_stand_pose_index: int = 79
    key_ender_crystal_time_offset: int = 80
    key_always_show_nametag: int = 81
    key_color_2: int = 82
    key_name_author: int = 83
    key_score_tag: int = 84
    key_baloon_attached_entity: int = 85
    key_pufferfish_size: int = 86
    key_bubble_time: int = 87
    key_agent: int = 88
    key_sitting_amount: int = 89
    key_sitting_amount_previous: int = 90
    key_eating_counter: int = 91
    key_flags_extended: int = 92
    key_laying_amount: int = 93
    key_laying_amount_previous: int = 94
    key_duration: int = 95
    key_spawn_time: int = 96
    key_change_rate: int = 97
    key_change_on_pickup: int = 98
    key_pickup_count: int = 99
    key_interact_text: int = 100
    key_trade_tier: int = 101
    key_max_trade_tier: int = 102
    key_trade_experience: int = 103
    key_skin_id: int = 104
    key_spawning_flames: int = 105
    key_command_block_tick_delay: int = 106
    key_command_block_execute_on_first_tick: int = 107
    key_ambient_sound_interval: int = 108
    key_ambient_sound_interval_range: int = 109
    key_ambient_sound_event_name: int = 110
    key_fall_damage_multiplier: int = 111
    key_name_raw_text: int = 112
    key_can_ride_target: int = 113
    key_low_tier_cured_discount: int = 114
    key_high_tier_cured_discount: int = 115
    key_nearby_cured_discount: int = 116
    key_nearby_cured_discount_timestamp: int = 117
    key_hitbox: int = 118
    key_is_buoyant: int = 119
    key_base_runtime_id: int = 120
    key_freezing_effect_strength: int = 121
    key_buoyancy_data: int = 122
    key_goat_horn_count: int = 123
    key_update_properties: int = 124
    type_byte: int = 0
    type_short: int = 1
    type_int: int = 2
    type_float: int = 3
    type_string: int = 4
    type_compound: int = 5
    type_vector_3_i: int = 6
    type_long: int = 7
    type_vector_3_f: int = 8
