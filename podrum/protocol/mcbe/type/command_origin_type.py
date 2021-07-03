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

class command_origin_type:
    player: int = 0
    block: int = 1
    minecart_block: int = 2
    dev_console: int = 3
    test: int = 4
    automation_player: int = 5
    client_automation: int = 6
    dedicated_server: int = 7
    entity: int = 8
    virtual: int = 9
    game_argument: int = 10
    entity_server: int = 11
    precompiled: int = 12
    game_director_entity_server: int = 13
    script: int = 14