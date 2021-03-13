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

import socket
from utils.binary_stream import binary_stream
from utils.raknet_address import raknet_address

class raknet_binary_stream(binary_stream):
    def read_address(self) -> raknet_address:
        version: int = self.read_unsigned_byte()
        if version == 4:
            host_parts: list = []
            for i in range(0, 4):
                host_parts.append(str(~self.read_unsigned_byte() & 0xff))
            host: str = ".".join(host_parts)
            port: int = self.read_unsigned_short_be()
            return raknet_address(host, port, version)
        if version == 6:
            self.read_unsigned_short_le() # Domain
            port: int = self.read_unsigned_short_be()
            self.read_unsigned_int_be() # Test out IPV4 (Family)
            host: str = socket.inet_ntop(socket.AF_INET6, self.read(16))
            self.read_unsigned_int_be() # Test out IPV6 (Family)
            return raknet_address(host, port, version)
      
    def write_address(self, address: raknet_address) -> None:
        if address.version == 4:
            self.write_unsigned_byte(address.version)
            host_parts: list = address.host.split(".")
            for part in host_parts:
                self.write_unsigned_byte(~int(part) & 0xff)
            self.write_unsigned_short_be(address.port)
        elif address.version == 6:
            self.write_unsigned_byte(address.version)
            self.write_unsigned_short_le(socket.AF_INET6) # Domain
            self.write_unsigned_short_be(address.port)
            self.write_unsigned_int_be(0) # Test out IPV4 (Family)
            self.write_unsigned_short_le(socket.inet_pton(socket.AF_INET6, address.host))
            self.write_unsigned_int_be(0) # Test out IPV6 (Family)
