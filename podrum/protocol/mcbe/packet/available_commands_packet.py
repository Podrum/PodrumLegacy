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

from podrum.protocol.mcbe.mcbe_protocol_info import mcbe_protocol_info
from podrum.protocol.mcbe.packet.mcbe_packet import mcbe_packet

class available_commands_packet(mcbe_packet):
    def __init__(self, data: bytes = b"", pos: int = 0) -> None:
        super().__init__(data, pos)
        self.packet_id: int = mcbe_protocol_info.available_commands_packet
 
    def decode_payload(self) -> None:
        self.values_len: int = self.read_var_int()
        if self.values_len < 0xff:
            self.enum_type: str = "byte"
        elif values_len < 0xffff:
            self.enum_type: str = "short"
        elif values_len < 0xffffff:
            self.enum_type: str = "int"
        self.enum_values: list = []
        for i in range(0, self.values_len):
            self.enum_values.append(self.read_string())
        self.suffixes: list = []
        for i in range(0, self.read_var_int()):
            self.suffixes.append(self.read_string())
        self.enums: list = []
        for i in range(0, self.read_var_int()):
            enum: dict = []
            enum["name"] = self.read_string()
            enum["values"] = []
            for i in range(0, self.read_var_int()):
                if self.enum_type == "byte":
                    enum["values"].append(self.read_unsigned_byte())
                elif self.enum_type == "short":
                    enum["values"].append(self.read_unsigned_short_le())
                elif self.enum_type == "int":
                    enum["values"].append(self.read_unsigned_int_le())
            self.enums.append(enum)
        self.command_data: list = []
        for i in range(0, self.read_var_int()):
            command: dict = {}
            command["name"] = self.read_string()
            command["description"] = self.read_string()
            command["flags"] = self.read_unsigned_byte()
            command["permission_level"] = self.read_unsigned_byte()
            command["alias"] = self.read_int_le()
            command["overloads"] = []
            for i in range(0, self.read_var_int()):
                overload: list = []
                for i in range(0, self.read_var_int()):
                    overload_entry: dict = {}
                    overload_entry["paramater_name"] = self.read_string()
                    overload_entry["value_type"] = self.read_unsigned_short_le()
                    overload_entry["enum_type"] = self.read_unsigned_short_le()
                    overload_entry["optional"] = self.read_bool()
                    overload_entry["options"] = 0 # Need protocol info
            
    def encode_payload(self) -> None:
        pass
