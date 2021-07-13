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

import binascii
from podrum.protocol.mcbe.mcbe_protocol_info import mcbe_protocol_info
from podrum.protocol.mcbe.packet.mcbe_packet import mcbe_packet

class creative_content_packet(mcbe_packet):
    def __init__(self, data: bytes = b"", pos: int = 0) -> None:
        super().__init__(data, pos)
        self.packet_id: int = mcbe_protocol_info.creative_content_packet
        
    def decode_payload(self) -> None:
        self.entries: list = []
        for i in range(0, self.read_signed_var_int()):
            self.entries.append({
                "entry_id": self.read_var_int(),
                "item": self.read_item_legacy()
            })
        
    def encode_payload(self) -> None:
        self.write_var_int(len(self.entries))
        for entry in self.entries:
            self.write_signed_var_int(entry["entry_id"])
            self.write_item_legacy(entry["item"])
