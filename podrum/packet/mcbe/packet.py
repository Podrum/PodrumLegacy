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

from binary_utils.binary_stream import binary_stream
from math.vector_2 import vector_2
from math.vector_3 import vector_3

class packet(binary_stream):
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

    def read_string(self) -> str:
        return self.read(self.read_var_int()).decode()
    
    def write_string(self, value: str) -> None:
        self.write_var_int(len(value))
        self.write(value.encode())
        
    def read_byte_array(self) -> bytes:
        return self.read(self.read_var_int())
    
    def write_byte_array(self, value: bytes) -> None:
        self.write_var_int(len(value))
        self.write(value)
        
    def read_vector_2(self) -> dict:
        value: dict = {}
        value["x"]: int = self.read_float_le()
        value["y"]: int = self.read_float_le()
        return value
        
    def write_vector_2(self, value: dict) -> None:
        self.write_float_le(value["x"])
        self.write_float_le(value["y"])
        
    def read_vector_3(self) -> dict:
        value: dict = {}
        value["x"]: int = self.read_float_le()
        value["y"]: int = self.read_float_le()
        value["z"]: int = self.read_float_le()
        return value
        
    def write_vector_3(self, value: dict) -> None:
        self.write_float_le(value["x"])
        self.write_float_le(value["y"])
        self.write_float_le(value["z"])
        
    def read_block_coordinates(self) -> dict:
        value: dict = {}
        value["x"]: int = self.read_signed_var_int()
        value["y"]: int = self.read_var_int()
        value["z"]: int = self.read_signed_var_int()
        return value
        
    def write_block_coordinates(self, value: dict) -> None:
        self.write_signed_var_int(value["x"])
        self.write_var_int(value["y"])
        self.write_signed_var_int(value["z"])
        
    def read_player_location(self) -> dict:
        value: dict = {}
        value["x"]: int = self.read_float_le()
        value["y"]: int = self.read_float_le()
        value["z"]: int = self.read_float_le()
        value["pitch"]: float = self.read_unsigned_byte() / 0.71
        value["head_yaw"]: float = self.read_unsigned_byte() / 0.71
        value["yaw"]: float = self.read_unsigned_byte() / 0.71
        return value
        
    def write_player_location(self, value: dict) -> None:
        self.write_float_le(value["x"])
        self.write_float_le(value["y"])
        self.write_float_le(value["z"])
        self.write_unsigned_byte(int(value["pitch"] * 0.71))
        self.write_unsigned_byte(int(value["head_yaw"] * 0.71))
        self.write_unsigned_byte(int(value["yaw"] * 0.71))

    def read_game_rules(self) -> dict:
        rules_count: int = self.read_var_int()
        rules: dict = {}
        for i in range(0, rules_count):
            rule_name: str = self.read_string()
            rule_type: int = self.read_var_int()
            if rule_type == 1:
                rules[rule_name]: bool = self.read_bool()
            elif rule_type == 2:
                rules[rule_name]: int = self.read_var_int()
            elif rule_type == 3:
                rules[rule_name]: float = self.read_float_le()
        return rules

    def write_game_rules(self, rules: dict) -> None:
        self.write_var_int(len(rules))
        for rule_name, rule_value in rules.items():
            self.write_string(rule_name)
            if isinstance(rule_value, bool):
                self.write_var_int(1)
                self.write_bool(rule_value)
            elif isinstance(rule_value, int):
                self.write_var_int(2)
                self.write_var_int(rule_value)
            elif isinstance(rule_value, float):
                self.write_var_int(3)
                self.write_float_le(rule_value)
