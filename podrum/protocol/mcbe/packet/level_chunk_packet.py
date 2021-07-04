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

class level_chunk_packet(mcbe_packet):
    def __init__(self, data: bytes = b"", pos: int = 0) -> None:
        super().__init__(data, pos)
        self.packet_id: int = mcbe_protocol_info.level_chunk_packet
 
    def decode_payload(self) -> None:
        self.chunk_x: int = self.read_signed_var_int()
        self.chunk_z: int = self.read_signed_var_int()
        self.sub_chunk_count: int = self.read_var_int()
        self.use_caching: bool = self.read_bool()
        self.chunk_data: bytes = self.read_byte_array()
 
    def encode_payload(self) -> None:
        self.write_signed_var_int(self.chunk_x)
        self.write_signed_var_int(self.chunk_z)
        self.write_var_int(self.sub_chunk_count)
        self.write_bool(self.use_caching)
        self.write_byte_array(self.chunk_data)
