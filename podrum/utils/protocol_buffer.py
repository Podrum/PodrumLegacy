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

from utils.context import context
from utils.raknet_address import raknet_address
import socket
import struct

class protocol_buffer:
    def __init__(self, data: bytes = b"", pos: int = 0) -> None:
        self.data: bytes = data
        self.pos: int = pos
        
    def read(self, byte_count: int) -> bytes:
        self.pos += byte_count
        return self.data[self.pos - byte_count: self.pos]

    def write(self, data: bytes) -> None:
        self.data += data

    def read_remaining(self) -> bytes:
        return self.read(len(self.data[self.pos:]))

    def pos_exceeded(self):
        return bool(len(self.data) <= self.pos)
        
    def read_char(self) -> int:
        return struct.unpack("b", self.read(1))[0]

    def write_char(self, value: int) -> None:
        self.write(struct.pack("b", value))
        
    def read_uchar(self) -> int:
        return struct.unpack("B", self.read(1))[0]

    def write_uchar(self, value: int) -> None:
        self.write(struct.pack("B", value))
        
    def read_bool(self) -> bool:
        return struct.unpack("?", self.read(1))[0]

    def write_bool(self, value: bool) -> None:
        self.write(struct.pack("?", value))

    def read_short(self, endianess: str) -> int:
        if endianess.lower() == "big":
            byte_order: str = ">"
        elif endianess.lower() == "little":
            byte_order: str = "<"
        else:
            return
        return struct.unpack(byte_order + "h", self.read(2))[0]

    def write_short(self, value: int, endianess: str) -> None:
        if endianess.lower() == "big":
            byte_order: str = ">"
        elif endianess.lower() == "little":
            byte_order: str = "<"
        else:
            return
        self.write(struct.pack(byte_order + "h", value))
        
    def read_ushort(self, endianess: str) -> int:
        if endianess.lower() == "big":
            byte_order: str = ">"
        elif endianess.lower() == "little":
            byte_order: str = "<"
        else:
            return
        return struct.unpack(byte_order + "H", self.read(2))[0]

    def write_ushort(self, value: int, endianess: str) -> None:
        if endianess.lower() == "big":
            byte_order: str = ">"
        elif endianess.lower() == "little":
            byte_order: str = "<"
        else:
            return
        self.write(struct.pack(byte_order + "H", value))
        
    def read_triad(self, endianess: str) -> int:
        if endianess.lower() == "big":
            return struct.unpack(">l", b"\x00" + self.read(3))[0]
        if endianess.lower() == "little":
            return struct.unpack("<l", self.read(3) + b"\x00")[0]
        
    def write_triad(self, value: int, endianess: str) -> None:
        if endianess.lower() == "big":
            self.write(struct.pack(">l", value)[1:])
        elif endianess.lower() == "little":
            self.write(struct.pack("<l", value)[:-1])
            
    def read_utriad(self, endianess: str) -> int:
        if endianess.lower() == "big":
            return struct.unpack(">L", b"\x00" + self.read(3))[0]
        if endianess.lower() == "little":
            return struct.unpack("<L", self.read(3) + b"\x00")[0]
        
    def write_utriad(self, value: int, endianess: str) -> None:
        if endianess.lower() == "big":
            self.write(struct.pack(">L", value)[1:])
        elif endianess.lower() == "little":
            self.write(struct.pack("<L", value)[:-1])

    def read_int(self, endianess: str) -> int:
        if endianess.lower() == "big":
            byte_order: str = ">"
        elif endianess.lower() == "little":
            byte_order: str = "<"
        else:
            return
        return struct.unpack(byte_order + "l", self.read(4))[0]

    def write_int(self, value: int, endianess: str) -> None:
        if endianess.lower() == "big":
            byte_order: str = ">"
        elif endianess.lower() == "little":
            byte_order: str = "<"
        else:
            return
        self.write(struct.pack(byte_order + "l", value))

    def read_uint(self, endianess: str) -> int:
        if endianess.lower() == "big":
            byte_order: str = ">"
        elif endianess.lower() == "little":
            byte_order: str = "<"
        else:
            return
        return struct.unpack(byte_order + "L", self.read(4))[0]

    def write_uint(self, value: int, endianess: str) -> None:
        if endianess.lower() == "big":
            byte_order: str = ">"
        elif endianess.lower() == "little":
            byte_order: str = "<"
        else:
            return
        self.write(struct.pack(byte_order + "L", value))

    def read_long(self, endianess: str) -> int:
        if endianess.lower() == "big":
            byte_order: str = ">"
        elif endianess.lower() == "little":
            byte_order: str = "<"
        else:
            return
        return struct.unpack(byte_order + "q", self.read(8))[0]

    def write_long(self, value: int, endianess: str) -> None:
        if endianess.lower() == "big":
            byte_order: str = ">"
        elif endianess.lower() == "little":
            byte_order: str = "<"
        else:
            return
        self.write(struct.pack(byte_order + "q", value))
        
    def read_ulong(self, endianess: str) -> int:
        if endianess.lower() == "big":
            byte_order: str = ">"
        elif endianess.lower() == "little":
            byte_order: str = "<"
        else:
            return
        return struct.unpack(byte_order + "Q", self.read(8))[0]

    def write_ulong(self, value: int, endianess: str) -> None:
        if endianess.lower() == "big":
            byte_order: str = ">"
        elif endianess.lower() == "little":
            byte_order: str = "<"
        else:
            return
        self.write(struct.pack(byte_order + "Q", value))

    def read_float(self, endianess: str) -> int:
        if endianess.lower() == "big":
            byte_order: str = ">"
        elif endianess.lower() == "little":
            byte_order: str = "<"
        else:
            return
        return struct.unpack(byte_order + "f", self.read(4))[0]

    def write_float(self, value: int, endianess: str) -> None:
        if endianess.lower() == "big":
            byte_order: str = ">"
        elif endianess.lower() == "little":
            byte_order: str = "<"
        else:
            return
        self.write(struct.pack(byte_order + "f", value))
        
    def read_double(self, endianess: str) -> int:
        if endianess.lower() == "big":
            byte_order: str = ">"
        elif endianess.lower() == "little":
            byte_order: str = "<"
        else:
            return
        return struct.unpack(byte_order + "d", self.read(8))[0]

    def write_double(self, value: int, endianess: str) -> None:
        if endianess.lower() == "big":
            byte_order: str = ">"
        elif endianess.lower() == "little":
            byte_order: str = "<"
        else:
            return
        self.write(struct.pack(byte_order + "d", value))
        
    def read_var_int(self) -> int:
        value: int = 0
        result: int = 0
        while True:
            char: int = self.read_uchar()
            result |= ((char & 0x7f) << (7 * value))
            value += 1
            if value > 5:
                raise Exception("VarInt is too big")
            if (char & 0x80) == 0:
                return result
            
    def write_var_int(self, value: int) -> None:
        while True:
            temp: int = value & 0x7f
            value >>= 7
            if value != 0:
                temp |= 0x80
            self.write_uchar(temp)
            if value == 0:
                break
                
    def read_signed_var_int(self) -> int:
        raw: int = self.read_var_int()
        temp: int = -(raw >> 1) - 1 if (raw & 1) else raw >> 1
        return temp
    
    def write_signed_var_int(self, value: int) -> None:
        write_var_int(value << 1 if value >= 0 else (-value - 1) << 1 | 1)
            
    def read_var_long(self) -> int:
        value: int = 0
        result: int = 0
        while True:
            char: int = self.read_uchar()
            result |= ((char & 0x7f) << (7 * value))
            value += 1
            if num_read > 10:
                raise Exception("VarLong is too big")
            if (char & 0x80) == 0:
                return result
            
    def write_var_long(self, value: int) -> None:
        while True:
            temp: int = value & 0x7f
            value >>= 7
            if value != 0:
                temp |= 0x80
            self.write_uchar(temp)
            if value == 0:
                break
                
    def read_signed_var_long(self) -> int:
        raw: int = self.read_var_long()
        temp: int = -(raw >> 1) - 1 if (raw & 1) else raw >> 1
        return temp
    
    def write_signed_var_long(self, value: int) -> None:
        write_signed_var_long(value << 1 if value >= 0 else (-value - 1) << 1 | 1)
        
    def read_mcbe_string(self) -> str:
        length: int = self.read_var_int()
        return self.read(length).decode()
    
    def write_mcbe_string(self, value: str) -> None:
        self.write_var_int(len(value))
        self.write(value.encode())
        
    def read_mcbe_byte_array(self) -> bytes:
        length: int = self.read_var_int()
        return self.read(length)
    
    def write_mcbe_byte_array(self, value: bytes) -> None:
        self.write_var_int(len(value))
        self.write(value)
        
    def read_mcbe_vector_2(self) -> object:
        value: object = context()
        value.x: int = self.read_float()
        value.y: int = self.read_float()
        return value
        
    def write_mcbe_vector_2(self, value: object) -> None:
        self.write_float(value.x)
        self.write_float(value.y)
        
    def read_mcbe_vector_3(self) -> object:
        value: object = context()
        value.x: int = self.read_float()
        value.y: int = self.read_float()
        value.z: int = self.read_float()
        return value
        
    def write_mcbe_vector_3(self, value: object) -> None:
        self.write_float(value.x)
        self.write_float(value.y)
        self.write_float(value.z)
        
    def read_mcbe_block_coordinates(self) -> object:
        value: object = context()
        value.x: int = self.read_signed_var_int()
        value.y: int = self.read_var_int()
        value.z: int = self.read_signed_var_int()
        return value
        
    def write_mcbe_block_coordinates(self, value: object) -> None:
        self.read_signed_var_int(value.x)
        self.read_var_int(value.y)
        self.read_signed_var_int(value.z)
        
    def read_mcbe_player_location(self) -> object:
        value: object = context()
        value.x: int = self.read_float()
        value.y: int = self.read_float()
        value.z: int = self.read_float()
        value.pitch: float = self.read_uchar() / 0.71
        value.head_yaw: float = self.read_uchar() / 0.71
        value.yaw: float = self.read_uchar() / 0.71
        return value
        
    def write_mcbe_player_location(self, value: object) -> None:
        self.write_float(value.x)
        self.write_float(value.y)
        self.write_float(value.z)
        self.write_uchar(int(value.pitch * 0.71))
        self.write_uchar(int(value.head_yaw * 0.71))
        self.write_uchar(int(value.yaw * 0.71))

    def read_raknet_string(self) -> str:
        length: int = self.read_ushort("big")
        return self.read(length).decode()
    
    def write_raknet_string(self, value: str) -> None:
        self.write_ushort(len(value), "big")
        self.write(value.encode())

    def read_raknet_address(self) -> object:
        version: int = self.read_uchar()
        if version == 4:
            host: str = ".".join([
                str(~self.read_uchar() & 0xff),
                str(~self.read_uchar() & 0xff),
                str(~self.read_uchar() & 0xff),
                str(~self.read_uchar() & 0xff)
            ])
            port: int = self.read_ushort("big")
            return raknet_address(host, port, version)
        if version == 6:
            self.read_ushort("little")
            port: int = self.read_ushort("big")
            self.read_int("big")
            host: str = socket.inet_ntop(socket.AF_INET6, self.read(16))
            self.read_int("big")
            return raknet_address(host, port, version)
    
    def write_raknet_address(self, value: object) -> None:
        self.write_uchar(value.version)
        if value.version == 4:
            for part in value.host.split("."):
                self.write_uchar(int(part))
            self.write_ushort(value.port, "big")
        elif value.version == 6:
            self.write_ushort(socket.AF_INET6, "little")
            self.write_ushort(value.port, "big")
            self.write_int(0, "big")
            self.write(socket.inet_pton(socket.AF_INET6, value.host))
            self.write_int(0, "big")
            
