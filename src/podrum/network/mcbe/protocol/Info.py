"""
*  ____           _
* |  _ \ ___   __| |_ __ _   _ _ __ ___
* | |_) / _ \ / _` | '__| | | | '_ ` _ \
* |  __/ (_) | (_| | |  | |_| | | | | | |
* |_|   \___/ \__,_|_|   \__,_|_| |_| |_|
*
* Licensed under the Mozilla Public License, Version 2.
* Permissions of this weak copyleft license are conditioned on making
* available source code of licensed files and modifications of those files 
* under the same license (or in certain cases, one of the GNU licenses).
* Copyright and license notices must be preserved. Contributors
* provide an express grant of patent rights. However, a larger work
* using the licensed work may be distributed under different terms and without 
* source code for files added in the larger work.
"""

class Info:
    MCBE_PROTOCOL_VERSION = 407
    MCBE_VERSION = "1.16.0"

    BATCH_PACKET = 0xfe
    LOGIN_PACKET = 0x01
    PLAY_STATUS_PACKET = 0x02
    SERVER_TO_CLIENT_HANDSHAKE_PACKET = 0x03
    CLIENT_TO_SERVER_HANDSHAKE_PACKET = 0x04
    DISCONNECT_PACKET = 0x05
    RESOURCE_PACKS_INFO_PACKET = 0x06
    RESOURCE_PACK_STACK_PACKET = 0x07
    RESOURCE_PACK_CLIENT_RESPONSE_PACKET = 0x08
    TEXT_PACKET = 0x09
    SET_TIME_PACKET = 0x0a
    START_GAME_PACKET = 0x0b
    ADD_PLAYER_PACKET = 0x0c
    ADD_ACTOR_PACKET = 0x0d
    REMOVE_ACTOR_PACKET = 0x0e
    ADD_ITEM_ACTOR_PACKET = 0x0f
    TAKE_ITEM_ACTOR_PACKET = 0x11
    MOVE_ACTOR_ABSOLUTE_PACKET = 0x12
    MOVE_PLAYER_PACKET = 0x13
    RIDER_JUMP_PACKET = 0x14
    UPDATE_BLOCK_PACKET = 0x15
    ADD_PAINTING_PACKET = 0x16