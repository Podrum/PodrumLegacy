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

from constant.misc import misc
from utils.protocol_buffer import protocol_buffer
from utils.jwt import jwt

class login_packet(protocol_buffer):
    def read_data(self) -> None:
        self.packet_id: int = self.read_var_int()
        self.protocol_version: int = self.read_uint("big")
        self.chain_data: list = []
        buffer: object = protocol_buffer(self.read_mcbe_byte_array())
        raw_chain_data: dict = json.loads(buffer.read(buffer.read_uint("little")))
        for chain in raw_chain_data["chain"]:
            self.chain_data.append(jwt.decode(chain))
        self.skin_data: dict = jwt.decode(buffer.read(buffer.read_uint("little")))
        
    def write_data(self) -> None:
        self.write_var_int(self.packet_id)
        self.write_uint(self.protocol_version, "big")
        buffer: object = protocol_buffer(self.read_mcbe_byte_array())
        raw_chain_data: dict = {"chain": []}
        for chain in self.chain_data:
            raw_chain_data["chain"].append(jwt.encode({"alg": "HS256", "typ": "JWT"}, chain, misc.mojang_public_key))
        encoded_chain_data: bytes = json.dumps(raw_chain_data).encode()
        buffer.write_uint(len(encoded_chain_data), "little")
        buffer.write(encoded_chain_data)
        buffer.write(jwt.encode({"alg": "HS256", "typ": "JWT"}, self.skin_data, misc.mojang_public_key).encode())
