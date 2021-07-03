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
                if self.values_len < 0xff:
                    enum["values"].append(self.read_unsigned_byte())
                elif self.values_len < 0xffff:
                    enum["values"].append(self.read_unsigned_short_le())
                elif self.values_len < 0xffffff:
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
                    overload_entry["options"] = self.read_unsigned_byte()
                    overload.append(overload_entry)
                command["overloads"].append(overload)
        self.dynamic_enums: list = []
        for i in range(0, self.read_var_int()):
            dynamic_enum: dict = {}
            dynamic_enum["name"] = self.read_string()
            dynamic_enum["values"] = []
            for i in range(0, self.read_var_int()):
                dynamic_enum["values"].append(self.read_string())
            self.dynamic_enums.append(dynamic_enum)
        self.enum_constraints: list = []
        for i in range(0, self.read_var_int()):
            enum_constraint: dict = {}
            enum_constraint["value_index"] = self.read_int_le()
            enum_constraint["enum_index"] = self.read_int_le()
            enum_constraint["constraints"] = []
            for i in range(0, self.read_var_int()):
                enum_constraint["constraints"].append(self.read_unsigned_byte())
            self.enum_constraints.append(enum_constraint)
            
    def encode_payload(self) -> None:
        self.write_var_int(self.values_len)
        self.write_var_int(len(self.enum_values))
        for enum_value in self.enum_values:
            self.write_string(enum_value)
        self.write_var_int(len(self.suffixes))
        for suffix in self.suffixes:
            self.write_string(suffix)
