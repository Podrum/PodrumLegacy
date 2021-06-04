################################################################################
#                                                                              #
#  ____           _                                                            #
# |  _ \ ___   __| |_ __ _   _ _ __ ___                                        #
# | |_) / _ \ / _` | '__| | | | '_ ` _ \                                       #
# |  __/ (_) | (_| | |  | |_| | | | | | |                                      #
# |_|   \___/ \__,_|_|   \__,_|_| |_| |_|                                      #
#                                                                              #
# Copyright 2021 Podrum Studios                                                #
#                                                                              #
# Permission is hereby granted, free of charge, to any person                  #
# obtaining a copy of this software and associated documentation               #
# files (the "Software"), to deal in the Software without restriction,         #
# including without limitation the rights to use, copy, modify, merge,         #
# publish, distribute, sublicense, and/or sell copies of the Software,         #
# and to permit persons to whom the Software is furnished to do so,            #
# subject to the following conditions:                                         #
#                                                                              #
# The above copyright notice and this permission notice shall be included      #
# in all copies or substantial portions of the Software.                       #
#                                                                              #
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR   #
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,     #
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE  #
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER       #
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING      #
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS #
# IN THE SOFTWARE.                                                             #
#                                                                              #
################################################################################

from protocol.mcbe.mcbe_protocol_info import mcbe_protocol_info
from protocol.mcbe.packet.mcbe_packet import mcbe_packet

class move_player_packet(mcbe_packet):
    def __init__(self, data: bytes = b"", pos: int = 0) -> None:
        super().__init__(data, pos)
        self.packet_id: int = mcbe_protocol_info.move_player_packet
 
    def decode_payload(self) -> None:
        self.runtime_entity_id: int = self.read_var_long()
        self.position: object = self.read_vector_3_float()
        self.rotation: object = self.read_vector_3_float()
        self.mode: int = self.read_unsigned_byte()
        self.on_ground: bool = self.read_bool()
        if not self.feos:
            self.riding_runtime_entity_id: int = self.read_float_le()
            self.teleportation_cause: int = self.read_var_long()
            self.entity_type: int = self.read_unsigned_byte()
 
    def encode_payload(self) -> None:
        self.write_var_long(self.runtime_entity_id)
        self.write_vector_3_float(self.position)
        self.write_vector_3_float(self.rotation)
        self.write_unsigned_byte(self.mode)
        self.write_bool(self.on_ground)
        self.write_float_le(self.riding_runtime_entity_id)
        self.write_var_long(self.teleportation_cause)
        self.write_unsigned_byte(self.entity_type)
