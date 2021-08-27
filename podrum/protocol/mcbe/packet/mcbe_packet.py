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

from podrum.protocol.mcbe.mcbe_binary_stream import mcbe_binary_stream

class mcbe_packet(mcbe_binary_stream):
    def decode_header(self) -> None:
        self.read_var_int()
      
    def decode(self) -> None:
        self.decode_header()
        if hasattr(self, "decode_payload"):
            self.decode_payload()
        
    def encode_header(self) -> None:
        self.write_var_int(self.packet_id)
      
    def encode(self) -> None:
        self.encode_header()
        if hasattr(self, "encode_payload"):
            self.encode_payload()
