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

from utils.protocol_buffer import protocol_buffer

class connection_request_accepted(protocol_buffer):
    def read_data(self) -> None:
        self.packet_id: int = self.read_uchar()
        self.client_address: object = self.read_raknet_address()
        self.system_index: int = self.read_ushort("big")
        self.system_addresses: list = []
        for i in range(0, 20):
            self.system_addresses.append(self.read_raknet_address())
        self.request_timestamp: int = self.read_ulong("big")
        self.accepted_timestamp: int = self.read_ulong("big")
        
    def write_data(self) -> None:
        self.write_uchar(self.packet_id)
        self.write_raknet_address(self.client_address)
        self.write_ushort(self.system_index, "big")
        for address in self.system_addresses:
            self.write_raknet_address(address)
        self.write_ulong(self.request_timestamp, "big")
        self.write_ulong(self.accepted_timestamp, "big")
