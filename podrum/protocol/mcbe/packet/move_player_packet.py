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


class move_player_packet(mcbe_packet):
    def __init__(self, data: bytes = b"", pos: int = 0) -> None:
        super().__init__(data, pos)
        self.packet_id: int = mcbe_protocol_info.move_player_packet
 
    def decode_payload(self) -> None:
        self.runtime_entity_id: int = self.read_var_long()
        self.position: object = self.read_vector_3_float()
        self.pitch: float = self.read_float_le()
        self.yaw: float = self.read_float_le()
        self.head_yaw: float = self.read_float_le()
        self.mode: int = self.read_unsigned_byte()
        self.on_ground: bool = self.read_bool()
        self.riding_runtime_entity_id: int = self.read_var_int()
        if self.mode == 2:
            self.teleport_cause: int = self.read_int_le()
            self.teleport_item: int = self.read_int_le()
        self.tick: int = self.read_var_long()
 
    def encode_payload(self) -> None:
        self.write_var_long(self.runtime_entity_id)
        self.write_vector_3_float(self.position)
        self.write_float_le(self.pitch)
        self.write_float_le(self.yaw)
        self.write_float_le(self.head_yaw)
        self.write_unsigned_byte(self.mode)
        self.write_bool(self.on_ground)
        self.write_var_long(self.riding_runtime_entity_id)
        if self.mode == 2:
            self.write_int_le(self.teleport_cause)
            self.write_int_le(self.teleport_item)
        self.write_var_long(self.tick)
