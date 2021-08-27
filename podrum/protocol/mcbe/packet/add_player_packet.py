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

class add_player_packet(mcbe_packet):
    def __init__(self, data: bytes = b"", pos: int = 0) -> None:
        super().__init__(data, pos)
        self.packet_id: int = mcbe_protocol_info.add_player_packet
 
    def decode_payload(self) -> None:
        self.uuid: str = self.read_uuid()
        self.username: str = self.read_string()
        self.entity_id_self: int = self.read_signed_var_long()
        self.runtime_entity_id: int = self.read_var_long()
        self.platform_chat_id: str = self.read_string()
        self.position: object = self.read_vector_3_float()
        self.velocity: object = self.read_vector_3_float()
        self.pitch: float = self.read_float_le()
        self.yaw: float = self.read_float_le()
        self.head_yaw: float = self.read_float_le()
        self.held_item: object = self.read_item()
        self.metadata: dict = self.read_metadata_dictionary()
        self.flags: int = self.read_var_int()
        self.command_permission: int = self.read_var_int()
        self.action_permissions: int = self.read_var_int()
        self.permission_level: int = self.read_var_int()
        self.custom_stored_permissions: int = self.read_var_int()
        self.user_id: int = self.read_long_le()
        self.links: list = self.read_links()
        self.device_id: str = self.read_string()
        self.device_os: int = self.read_int_le()
 
    def encode_payload(self) -> None:
        pass
