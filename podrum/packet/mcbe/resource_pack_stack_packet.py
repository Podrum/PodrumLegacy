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

from constant.mcbe_packet_ids import mcbe_packet_ids
from packet.mcbe.packet import packet

class resource_pack_stack_packet(packet):
    def __init__(self, data: bytes = b"", pos: int = 0) -> None:
        super().__init__(data, pos)
        self.packet_id: int = mcbe_packet_ids.resource_pack_stack_packet

    def decode_payload(self):
        self.forced_to_accept: bool = self.read_bool()
        behavior_packs_count: int = self.read_var_int()
        for i in range(0, behavior_packs_count):
            if not hasattr(self, "behavior_pack_entries"):
                self.behavior_pack_entries = []
            behavior_pack_entry: dict = {}
            behavior_pack_entry["id"]: str = self.read_string()
            behavior_pack_entry["version"]: str = self.read_string()
            behavior_pack_entry["sub_name"]: str = self.read_string()
            self.behavior_pack_entries.append(behavior_pack_entry)
        resource_packs_count: int = self.read_var_int()
        for i in range(0, resource_packs_count):
            if not hasattr(self, "resource_pack_entries"):
                self.resource_pack_entries = []
            resource_pack_entry: dict = {}
            resource_pack_entry["id"]: str = self.read_string()
            resource_pack_entry["version"]: str = self.read_string()
            resource_pack_entry["sub_name"]: str = self.read_string()
            self.resource_pack_entries.append(resource_pack_entry)
        self.game_version: str = self.read_string()
        self.expirement_count: int = self.read_var_int()
        self.experimental: bool = self.read_bool()
        self.pos += 3
          
    def encode_payload(self):
        self.write_bool(self.forced_to_accept)
        if not hasattr(self, "behavior_pack_entries"):
            self.write_var_int(0)
        else:
            self.write_var_int(len(self.behavior_pack_entries))
            for pack in self.behavior_pack_entries:
                self.write_string(pack["id"])
                self.write_string(pack["version"])
                self.write_string(pack["sub_name"])
        if not hasattr(self, "resource_pack_entries"):
            self.write_var_int(0)
        else:
            self.write_var_int(len(self.resource_pack_entries))
            for pack in self.resource_pack_entries:
                self.write_string(pack["id"])
                self.write_string(pack["version"])
                self.write_string(pack["sub_name"])
        self.write_string(self.game_version)
        self.write_var_int(self.expirement_count)
        self.write_bool(self.experimental)
        self.write_unsigned_byte(0)
        self.write_unsigned_byte(0)
        self.write_unsigned_byte(0)
