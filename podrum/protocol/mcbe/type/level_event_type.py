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

class level_event_type:
    sound_click: int = 1000
    sound_click_fail: int = 1001
    sound_shoot: int = 1002
    sound_door: int = 1003
    sound_fizz: int = 1004
    sound_ignite: int = 1005

    sound_ghast: int = 1007
    sound_ghast_shoot: int = 1008
    sound_blaze_shoot: int = 1009
    sound_door_bump: int = 1010

    sound_door_crash: int = 1012

    sound_enderman_teleport: int = 1018

    sound_anvil_break: int = 1020
    sound_anvil_use: int = 1021
    sound_anvil_fail: int = 1022

    sound_pop: int = 1030

    sound_portal: int = 1032
    sound_itemframe_add_item: int = 1040
    sound_itemframe_place: int = 1042
    sound_itemframe_remove_item: int = 1043
    sound_itemframe_rotate_item: int = 1044

    sound_camera: int = 1050
    sound_orb: int = 1051
    sound_totem: int = 1052

    sound_armor_stand_break: int = 1060
    sound_armor_stand_hit: int = 1061
    sound_armor_stand_fall: int = 1062
    sound_armor_stand_place: int = 1063

    particle_shoot: int = 2000
    particle_destroy: int = 2001
    particle_splash: int = 2002
    particle_eye_despawn: int = 2003
    particle_spawn: int = 2004

    guardian_curse: int = 2006

    particle_block_force_field: int = 2008
    particle_projectile_hit: int = 2009
    particle_enderman_teleport: int = 2013
    particle_punch_block: int = 2014

    start_rain: int = 3001
    start_thunder: int = 3002
    stop_rain: int = 3003
    stop_thunder: int = 3004
    pause_game: int = 3005
    pause_game_no_screen: int = 3006
    set_game_speed: int = 3007

    redstone_trigger: int = 3500
    cauldron_explode: int = 3501
    cauldron_dye_armor: int = 3502
    cauldron_clean_armor: int = 3503
    cauldron_fill_potion: int = 3504
    cauldron_take_potion: int = 3505
    cauldron_fill_water: int = 3506
    cauldron_take_water: int = 3507
    cauldron_add_dye: int = 3508
    cauldron_clean_banner: int = 3509

    block_start_break: int = 3600
    block_stop_break: int = 3601

    set_data = 4000

    players_sleeping = 9800

    add_particle_mask = 0x4000


