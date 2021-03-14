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
from utils.context import context

class mcbe_binary_stream(binary_stream):
    def read_var_int(self) -> int:
        value: int = 0
        for i in range(0, 35, 7):
            if self.feos():
                raise Exception("Data position exceeded")
            number: int = self.read_unsigned_byte()
            value |= ((number & 0x7f) << i)
            if (number & 0x80) == 0:
                return value
        raise Exception("VarInt is too big")
            
    def write_var_int(self, value: int) -> None:
        data: bytes = b""
        value &= 0xffffffff
        for i in range(0, 5):
            if (value >> 7) != 0:
                self.write_unsigned_byte(value | 0x80)
            else:
                self.write_unsigned_byte(value & 0x7f)
                break
            value >>= 7
                
    def read_signed_var_int(self) -> int:
        raw: int = self.read_var_int()
        temp: int = -(raw >> 1) - 1 if (raw & 1) else raw >> 1
        return temp
    
    def write_signed_var_int(self, value: int) -> None:
        write_var_int(value << 1 if value >= 0 else (-value - 1) << 1 | 1)
            
    def read_var_long(self) -> int:
        value: int = 0
        for i in range(0, 70, 7):
            if self.feos():
                raise Exception("Data position exceeded")
            number: int = self.read_unsigned_byte()
            value |= ((number & 0x7f) << i)
            if (number & 0x80) == 0:
                return value
        raise Exception("VarLong is too big")
            
    def write_var_long(self, value: int) -> None:
        for i in range(0, 10):
            if (value >> 7) != 0:
                self.write_unsigned_byte(value | 0x80)
            else:
                self.write_unsigned_byte(value & 0x7f)
                break
            value >>= 7
                
    def read_signed_var_long(self) -> int:
        raw: int = self.read_var_long()
        temp: int = -(raw >> 1) - 1 if (raw & 1) else raw >> 1
        return temp
    
    def write_signed_var_long(self, value: int) -> None:
        write_signed_var_long(value << 1 if value >= 0 else (-value - 1) << 1 | 1)
  
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
        
    def read_vector_2(self) -> object:
        value: object = context()
        value.x: int = self.read_float()
        value.y: int = self.read_float()
        return value
        
    def write_vector_2(self, value: object) -> None:
        self.write_float(value.x)
        self.write_float(value.y)
        
    def read_vector_3(self) -> object:
        value: object = context()
        value.x: int = self.read_float()
        value.y: int = self.read_float()
        value.z: int = self.read_float()
        return value
        
    def write_vector_3(self, value: object) -> None:
        self.write_float(value.x)
        self.write_float(value.y)
        self.write_float(value.z)
        
    def read_block_coordinates(self) -> object:
        value: object = context()
        value.x: int = self.read_signed_var_int()
        value.y: int = self.read_var_int()
        value.z: int = self.read_signed_var_int()
        return value
        
    def write_block_coordinates(self, value: object) -> None:
        self.read_signed_var_int(value.x)
        self.read_var_int(value.y)
        self.read_signed_var_int(value.z)
        
    def read_player_location(self) -> object:
        value: object = context()
        value.x: int = self.read_float()
        value.y: int = self.read_float()
        value.z: int = self.read_float()
        value.pitch: float = self.read_unsigned_byte() / 0.71
        value.head_yaw: float = self.read_unsigned_byte() / 0.71
        value.yaw: float = self.read_unsigned_byte() / 0.71
        return value
        
    def write_player_location(self, value: object) -> None:
        self.write_float(value.x)
        self.write_float(value.y)
        self.write_float(value.z)
        self.write_unsigned_byte(int(value.pitch * 0.71))
        self.write_unsigned_byte(int(value.head_yaw * 0.71))
        self.write_unsigned_byte(int(value.yaw * 0.71))
