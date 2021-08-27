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

class action_type:
    start_break: int = 0
    abort_break: int = 1
    stop_break: int = 2
    get_updated_block: int = 3
    drop_item: int = 4
    start_sleeping: int = 5
    stop_sleeping: int = 6
    respawn: int = 7
    jump: int = 8
    start_sprint: int = 9
    stop_sprint: int = 10
    start_sneak: int = 11
    stop_sneak: int = 12
    creative_player_destroy_block: int = 13
    dimension_change_ack: int = 14
    start_glide: int = 15
    stop_glide: int = 16
    build_denied: int = 17
    crack_break: int = 18
    change_skin: int = 19
    set_enchatnment_seed: int = 20
    swimming: int = 21
    stop_swimming: int = 22
    start_spin_attack: int = 23
    stop_spin_attack: int = 24
    interact_block: int = 25
    predict_break: int = 26
    continue_break: int = 27