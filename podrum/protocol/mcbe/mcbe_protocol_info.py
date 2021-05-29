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

class mcbe_protocol_info:
    login_packet: int = 0x01
    play_status_packet: int = 0x02
    server_to_client_handshake_packet: int = 0x03
    client_to_server_handshake_packet: int = 0x04
    disconnect_packet: int = 0x05
    resource_packs_info_packet: int = 0x06
    resource_pack_stack_packet: int = 0x07
    resource_pack_client_response_packet: int = 0x08
    text_packet: int = 0x09
    set_time_packet: int = 0x0a
    start_game_packet: int = 0x0b
    add_player_packet: int = 0x0c
    add_actor_packet: int = 0x0d
    remove_actor_packet: int = 0x0e
    add_item_actor_packet: int = 0x0f
    take_item_actor_packet: int = 0x11
    move_actor_absolute_packet: int = 0x12
    move_player_packet: int = 0x13
    rider_jump_packet: int = 0x14
    update_block_packet: int = 0x15
    add_painting_packet: int = 0x16
    tick_sync_packet: int = 0x17
    level_sound_event_packet_v1: int = 0x18
    level_event_packet: int = 0x19
    block_event_packet: int = 0x1a
    actor_event_packet: int = 0x1b
    mob_effect_packet: int = 0x1c
    update_attributes_packet: int = 0x1d
    inventory_transaction_packet: int = 0x1e
    mob_equipment_packet: int = 0x1f
    mob_armor_equipment_packet: int = 0x20
    interact_packet: int = 0x21
    block_pick_request_packet: int = 0x22
    actor_pick_request_packet: int = 0x23
    player_action_packet: int = 0x24
    hurt_armor_packet: int = 0x26
    set_actor_data_packet: int = 0x27
    set_actor_motion_packet: int = 0x28
    set_actor_link_packet: int = 0x29
    set_health_packet: int = 0x2a
    set_spawn_position_packet: int = 0x2b
    animate_packet: int = 0x2c
    respawn_packet: int = 0x2d
    container_open_packet: int = 0x2e
    container_close_packet: int = 0x2f
    player_hotbar_packet: int = 0x30
    inventory_content_packet: int = 0x31
    inventory_slot_packet: int = 0x32
    container_set_data_packet: int = 0x33
    crafting_data_packet: int = 0x34
    crafting_event_packet: int = 0x35
    gui_data_pick_item_packet: int = 0x36
    adventure_settings_packet: int = 0x37
    block_actor_data_packet: int = 0x38
    player_input_packet: int = 0x39
    level_chunk_packet: int = 0x3a
    set_commands_enabled_packet: int = 0x3b
    set_difficulty_packet: int = 0x3c
    change_dimension_packet: int = 0x3d
    set_player_game_type_packet: int = 0x3e
    player_list_packet: int = 0x3f
    simple_event_packet: int = 0x40
    event_packet: int = 0x41
    spawn_experience_orb_packet: int = 0x42
    clientbound_map_item_data_packet: int = 0x43
    map_info_request_packet: int = 0x44
    request_chunk_radius_packet: int = 0x45
    chunk_radius_updated_packet: int = 0x46
    item_frame_drop_item_packet: int = 0x47
    game_rules_changed_packet: int = 0x48
    camera_packet: int = 0x49
    boss_event_packet: int = 0x4a
    show_credits_packet: int = 0x4b
    available_commands_packet: int = 0x4c
    command_request_packet: int = 0x4d
    command_block_update_packet: int = 0x4e
    command_output_packet: int = 0x4f
    update_trade_packet: int = 0x50
    update_equip_packet: int = 0x51
    resource_pack_data_info_packet: int = 0x52
    resource_pack_chunk_data_packet: int = 0x53
    resource_pack_chunk_request_packet: int = 0x54
    transfer_packet: int = 0x55
    play_sound_packet: int = 0x56
    stop_sound_packet: int = 0x57
    set_title_packet: int = 0x58
    add_behavior_tree_packet: int = 0x59
    structure_block_update_packet: int = 0x5a
    show_store_offer_packet: int = 0x5b
    purchase_receipt_packet: int = 0x5c
    player_skin_packet: int = 0x5d
    sub_client_login_packet: int = 0x5e
    automation_client_connect_packet: int = 0x5f
    set_last_hurt_by_packet: int = 0x60
    book_edit_packet: int = 0x61
    npc_request_packet: int = 0x62
    photo_transfer_packet: int = 0x63
    modal_form_request_packet: int = 0x64
    modal_form_response_packet: int = 0x65
    server_settings_request_packet: int = 0x66
    server_settings_response_packet: int = 0x67
    show_profile_packet: int = 0x68
    set_default_game_type_packet: int = 0x69
    remove_objective_packet: int = 0x6a
    set_display_objective_packet: int = 0x6b
    set_score_packet: int = 0x6c
    lab_table_packet: int = 0x6d
    update_block_synced_packet: int = 0x6e
    move_actor_delta_packet: int = 0x6f
    set_scoreboard_identity_packet: int = 0x70
    set_local_player_as_initialized_packet: int = 0x71
    update_soft_enum_packet: int = 0x72
    network_stack_latency_packet: int = 0x73
    script_custom_event_packet: int = 0x75
    spawn_particle_effect_packet: int = 0x76
    available_actor_identifiers_packet: int = 0x77
    level_sound_event_packet_v2: int = 0x78
    network_chunk_publisher_update_packet: int = 0x79
    biome_definition_list_packet: int = 0x7a
    level_sound_event_packet: int = 0x7b
    level_event_generic_packet: int = 0x7c
    lectern_update_packet: int = 0x7d
    add_entity_packet: int = 0x7f
    remove_entity_packet: int = 0x80
    client_cache_status_packet: int = 0x81
    on_screen_texture_animation_packet: int = 0x82
    map_create_locked_copy_packet: int = 0x83
    structure_template_data_request_packet: int = 0x84
    structure_template_data_response_packet: int = 0x85
    client_cache_blob_status_packet: int = 0x87
    client_cache_miss_response_packet: int = 0x88
    education_settings_packet: int = 0x89
    emote_packet: int = 0x8a
    multiplayer_settings_packet: int = 0x8b
    settings_command_packet: int = 0x8c
    anvil_damage_packet: int = 0x8d
    completed_using_item_packet: int = 0x8e
    network_settings_packet: int = 0x8f
    player_auth_input_packet: int = 0x90
    creative_content_packet: int = 0x91
    player_enchant_options_packet: int = 0x92
    item_stack_request_packet: int = 0x93
    item_stack_response_packet: int = 0x94
    player_armor_damage_packet: int = 0x95
    code_builder_packet: int = 0x96
    update_player_game_type_packet: int = 0x97
    emote_list_packet: int = 0x98
    position_tracking_d_b_server_broadcast_packet: int = 0x99
    position_tracking_d_b_client_request_packet: int = 0x9a
    debug_info_packet: int = 0x9b
    packet_violation_warning_packet: int = 0x9c
    motion_prediction_hints_packet: int = 0x9d
    animate_entity_packet: int = 0x9e
    camera_shake_packet: int = 0x9f
    player_fog_packet: int = 0xa0
    correct_player_move_prediction_packet: int = 0xa1
    item_component_packet: int = 0xa2
    filter_text_packet: int = 0xa3