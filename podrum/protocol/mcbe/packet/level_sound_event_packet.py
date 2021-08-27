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

from podrum.protocol.mcbe.mcbe_protocol_info import mcbe_protocol_info
from podrum.protocol.mcbe.packet.mcbe_packet import mcbe_packet
from podrum.protocol.mcbe.type.interact_type import interact_type

class level_sound_event_packet(mcbe_packet):
    def __init__(self, data: bytes = b"", pos: int = 0) -> None:
        super().__init__(data, pos)
        self.packet_id: int = mcbe_protocol_info.level_sound_event_packet
 
    def decode_payload(self) -> None:
        self.sound_id: int = self.read_var_int()
        self.position: object = self.read_vector_3_float()
        self.extra_data: int = self.read_signed_var_int()
        self.entity_type: str = self.read_string()
        self.is_baby_mob: bool = self.read_bool()
        self.is_global: bool = self.read_bool()
 
    def encode_payload(self) -> None:
        self.write_var_int(self.sound_id)
        self.write_vector_3_float(self.position)
        self.write_signed_var_int(self.extra_data)
        self.write_string(self.entity_type)
        self.write_bool(self.is_baby_mob)
        self.write_bool(self.is_global)
