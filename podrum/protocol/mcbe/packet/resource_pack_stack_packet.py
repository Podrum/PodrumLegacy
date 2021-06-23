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

class resource_pack_stack_packet(mcbe_packet):
    def __init__(self, data: bytes = b"", pos: int = 0) -> None:
        super().__init__(data, pos)
        self.packet_id: int = mcbe_protocol_info.resource_pack_stack_packet

    def decode_payload(self):
        self.forced_to_accept: bool = self.read_bool()
        self.behavior_pack_id_versions: list = self.read_resource_pack_id_versions()
        self.texture_pack_id_versions: list = self.read_resource_pack_id_versions()
        self.game_version: str = self.read_string()
        self.experiment_count: int = self.read_int_le()
        self.experimental: bool = self.read_bool()
          
    def encode_payload(self):
        self.write_bool(self.forced_to_accept)
        self.write_resource_pack_id_versions(self.behavior_pack_id_versions)
        self.write_resource_pack_id_versions(self.texture_pack_id_versions)
        self.write_string(self.game_version)
        self.write_int_le(self.experiment_count)
        self.write_bool(self.experimental)
