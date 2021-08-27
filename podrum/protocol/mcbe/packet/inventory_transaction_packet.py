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

class inventory_transaction_packet(mcbe_packet):
    def __init__(self, data: bytes = b"", pos: int = 0) -> None:
        super().__init__(data, pos)
        self.packet_id: int = mcbe_protocol_info.inventory_transaction_packet
        
    def decode_payload(self) -> None:
        self.transaction: dict = self.read_transaction()
        
    def encode_payload(self) -> None:
        self.write_transaction(self.transaction)
        
