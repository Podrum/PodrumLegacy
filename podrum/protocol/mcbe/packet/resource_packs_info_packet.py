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

class resource_packs_info_packet(mcbe_packet):
    def __init__(self, data: bytes = b"", pos: int = 0) -> None:
        super().__init__(data, pos)
        self.packet_id: int = mcbe_protocol_info.resource_packs_info_packet

    def decode_payload(self):
        self.forced_to_accept: bool = self.read_bool()
        self.scripting_enabled: bool = self.read_bool()
        behavior_packs_count: int = self.read_unsigned_short_le()
        for i in range(0, behavior_packs_count):
            if not hasattr(self, "behavior_packs_info"):
                self.behavior_packs_info = []
            behavior_pack_info: dict = {}
            behavior_pack_info["id"]: str = self.read_string()
            behavior_pack_info["version"]: str = self.read_string()
            behavior_pack_info["size"]: int = self.read_unsigned_long_le()
            behavior_pack_info["encryption_key"]: str = self.read_string()
            behavior_pack_info["sub_name"]: str = self.read_string()
            behavior_pack_info["content_identity"]: str = self.read_string()
            behavior_pack_info["has_scripts"]: bool = self.read_bool()
            self.behavior_packs_info.append(behavior_pack_info)
        resource_packs_count: int = self.read_unsigned_short_le()
        for i in range(0, resource_packs_count):
            if not hasattr(self, "resource_packs_info"):
                self.resource_packs_info = []
            resource_pack_info: dict = {}
            resource_pack_info["id"]: str = self.read_string()
            resource_pack_info["version"]: str = self.read_string()
            resource_pack_info["size"]: int = self.read_unsigned_long_le()
            resource_pack_info["encryption_key"]: str = self.read_string()
            resource_pack_info["sub_name"]: str = self.read_string()
            resource_pack_info["content_identity"]: str = self.read_string()
            behavior_pack_info["has_scripts"]: bool = self.read_bool()
            resource_pack_info["rtx"]: bool = self.read_bool()
            self.resource_packs_info.append(resource_pack_info)
          
    def encode_payload(self):
        self.write_bool(self.forced_to_accept)
        self.write_bool(self.scripting_enabled)
        if not hasattr(self, "behavior_packs_info"):
            self.write_unsigned_short_le(0)
        else:
            self.write_unsigned_short_le(len(self.behavior_packs_info))
            for pack in self.behavior_packs_info:
                self.write_string(pack["id"])
                self.write_string(pack["version"])
                self.write_unsigned_long_le(pack["size"])
                self.write_string(pack["encryption_key"])
                self.write_string(pack["sub_name"])
                self.write_string(pack["content_identity"])
                self.write_bool(pack["has_scripts"])
        if not hasattr(self, "resource_packs_info"):
            self.write_unsigned_short_le(0)
        else:
            self.write_unsigned_short_le(len(self.resource_packs_info))
            for pack in self.resource_packs_info:
                self.write_string(pack["id"])
                self.write_string(pack["version"])
                self.write_unsigned_long_le(pack["size"])
                self.write_string(pack["encryption_key"])
                self.write_string(pack["sub_name"])
                self.write_string(pack["content_identity"])
                self.write_bool(pack["has_scripts"])
                self.write_bool(pack["rtx"])
