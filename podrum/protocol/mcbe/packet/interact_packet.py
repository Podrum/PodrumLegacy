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
from podrum.protocol.mcbe.type.interact_type import interact_type

class interact_packet(mcbe_packet):
    def __init__(self, data: bytes = b"", pos: int = 0) -> None:
        super().__init__(data, pos)
        self.packet_id: int = mcbe_protocol_info.interact_packet
 
    def decode_payload(self) -> None:
        self.action_id: int = self.read_byte()
        self.target_entity_id: int = self.read_var_long()
        if self.action_id == interact_type.mouse_over_entity or self.action_id == interact_type.leave_vehicle:
            self.position: object = self.read_vector_3_float()
 
    def encode_payload(self) -> None:
        self.write_byte(self.action_id)
        self.write_var_long(self.target_entity_id)
        if self.action_id == interact_type.mouse_over_entity or self.action_id == interact_type.leave_vehicle:
            self.write_vector_3_float(self.position)
