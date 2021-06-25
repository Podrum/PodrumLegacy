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

from binary_utils.binary_stream import binary_stream
from podrum.protocol.mcbe.mcbe_protocol_info import mcbe_protocol_info
from podrum.protocol.mcbe.packet.mcbe_packet import mcbe_packet
import json
from podrum.jwt import jwt

class login_packet(mcbe_packet):
    def __init__(self, data: bytes = b"", pos: int = 0) -> None:
        super().__init__(data, pos)
        self.packet_id: int = mcbe_protocol_info.login_packet

    def decode_payload(self) -> None:
        self.protocol_version: int = self.read_unsigned_int_be()
        self.chain_data: list = []
        buffer: object = binary_stream(self.read_byte_array())
        raw_chain_data: dict = json.loads(buffer.read(buffer.read_unsigned_int_le()).decode())
        for chain in raw_chain_data["chain"]:
            self.chain_data.append(jwt.decode(chain))
        self.skin_data: dict = jwt.decode(buffer.read(buffer.read_unsigned_int_le()).decode())
        
    def encode_payload(self) -> None:
        self.write_unsigned_int_be(self.protocol_version)
        raw_chain_data: dict = {"chain": []}
        for chain in self.chain_data:
            jwt_data: str = jwt.encode({"alg": "HS256", "typ": "JWT"}, chain, mcbe_protocol_info.mojang_public_key)
            raw_chain_data["chain"].append(jwt_data)
        temp_stream = binary_stream()
        json_data: str = json.dumps(raw_chain_data)
        temp_stream.write_unsigned_int_le(len(json_data))
        temp_stream.write(json_data.encode())
        self.write_byte_array(temp_stream.data)
        jwt_data: str = jwt.encode({"alg": "HS256", "typ": "JWT"}, self.skin_data, mcbe_protocol_info.mojang_public_key)
        self.write_unsigned_int_le(len(jwt_data))
        self.write(jwt_data.encode())
