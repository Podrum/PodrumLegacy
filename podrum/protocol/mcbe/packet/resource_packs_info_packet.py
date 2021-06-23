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

class resource_packs_info_packet(mcbe_packet):
    def __init__(self, data: bytes = b"", pos: int = 0) -> None:
        super().__init__(data, pos)
        self.packet_id: int = mcbe_protocol_info.resource_packs_info_packet

    def decode_payload(self):
        self.forced_to_accept: bool = self.read_bool()
        self.scripting_enabled: bool = self.read_bool()
        self.behavior_pack_infos: list = self.read_behavior_pack_infos()
        self.texture_pack_infos: list = self.read_texture_pack_infos()
          
    def encode_payload(self):
        self.write_bool(self.forced_to_accept)
        self.write_bool(self.scripting_enabled)
        self.write_behavior_pack_infos(self.behavior_pack_infos)
        self.write_texture_pack_infos(self.texture_pack_infos)
