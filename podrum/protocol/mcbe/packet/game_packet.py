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
from rak_net.protocol.packet import packet
import zlib

class game_packet(packet):
    def __init__(self, data: bytes = b"", pos: int = 0) -> None:
        super().__init__(data, pos)
        self.packet_id: int = 0xfe

    def decode_payload(self):
        self.body: bytes = zlib.decompress(self.read_remaining(), -zlib.MAX_WBITS, 1024 * 1024 * 8)
        
    def encode_payload(self):
        compress: object = zlib.compressobj(1, zlib.DEFLATED, -zlib.MAX_WBITS)
        compressed_data: bytes = compress.compress(self.body)
        compressed_data += compress.flush()
        self.write(compressed_data)
  
    def write_packet_data(self, data):
        buffer: object = binary_stream()
        buffer.write_var_int(len(data))
        buffer.write(data)
        if hasattr(self, "body"):
            self.body += buffer.data
        else:
            self.body: bytes = buffer.data
            
    def read_packets_data(self):
        buffer: object = binary_stream(self.body)
        packets_data: list = []
        while not buffer.feos():
            packets_data.append(buffer.read(buffer.read_var_int()))
        return packets_data
