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

from podrum.protocol.mcbe.mcbe_protocol_info import mcbe_protocol_info
from podrum.protocol.mcbe.packet.mcbe_packet import mcbe_packet


class player_action_packet(mcbe_packet):
    def __init__(self, data: bytes = b"", pos: int = 0) -> None:
        super().__init__(data, pos)
        self.packet_id: int = mcbe_protocol_info.player_action_packet
        self.action_start_sneak = 22
        self.action_end_sneak = 24

    def decode_payload(self) -> None:
        self.runtime_entity_id: int = self.read_var_long()
        self.action: int = self.read_var_int()
        self.face: int = self.read_var_int()


    def encode_payload(self) -> None:
        self.write_var_long(self.runtime_entity_id)
        self.write_var_int(self.action)
        self.write_block_coordinates(self.read_block_coordinates())
        self.write_var_int(self.face)
