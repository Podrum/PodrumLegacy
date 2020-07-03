"""
*  ____           _
* |  _ \ ___   __| |_ __ _   _ _ __ ___
* | |_) / _ \ / _` | '__| | | | '_ ` _ \
* |  __/ (_) | (_| | |  | |_| | | | | | |
* |_|   \___/ \__,_|_|   \__,_|_| |_| |_|
*
* This program is free software: you can redistribute it and/or modify
* it under the terms of the GNU Lesser General Public License as published by
* the Free Software Foundation, either version 3 of the License, or
* (at your option) any later version.
"""

class ProtocolInfo:
    # Version info
    CURRENT_PROTOCOL = 407
    MINECRAFTBE_VERSION = 'v1.16.0'
    MINECRAFTBE_VERSION_NETWORK = '1.16.0'
    
    # MCBE protocol info
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
    TICK_SYNC_PACKET = 0x17
    LEVEL_SOUND_EVENT_PACKET_V1 = 0x18
    LEVEL_EVENT_PACKET = 0x19
    BLOCK_EVENT_PACKET = 0x1a
    ACTOR_EVENT_PACKET = 0x1b
    MOB_EFFECT_PACKET = 0x1c
    UPDATE_ATTRIBUTES_PACKET = 0x1d
    
    
