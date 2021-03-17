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

from utils.mcbe_binary_stream import mcbe_binary_stream

class nbt_net_le_binary_stream(mcbe_binary_stream):
    def read_int_tag(self) -> int:
        return self.read_signed_var_int()
      
    def write_int_tag(self, value: int) -> None:
        self.write_signed_var_int(value)
        
    def read_long_tag(self) -> int:
        return self.read_signed_var_long()
      
    def write_long_tag(self, value: int) -> None:
        self.write_signed_var_long(value)
        
    def read_byte_array_tag(self) -> list:
        byte_count: int = self.read_int_tag()
        tag: list = []
        for i in range(0, byte_count):
            tag.append(self.read_byte_tag())
        return tag
      
    def write_byte_array_tag(self, value: list) -> None:
        self.write_int_tag(len(value))
        for item in vale:
            self.write_byte_tag(item)
            
    def read_int_array_tag(self) -> list:
        byte_count: int = self.read_int_tag()
        value: list = []
        for i in range(0, byte_count):
            value.append(self.read_int_tag())
        return value
      
    def write_int_array_tag(self, value: list) -> None:
        self.write_int_tag(len(value))
        for item in value:
            self.write_int_tag(item)
            
    def read_long_array_tag(self) -> list:
        byte_count: int = self.read_int_tag()
        tag: list = []
        for i in range(0, byte_count):
            tag.append(self.read_long_tag())
        return tag
      
    def write_long_array_tag(self, value: list) -> None:
        self.write_int_tag(len(value))
        for item in vale:
            self.write_long_tag(item)
            
    def read_string_tag(self) -> str:
        return self.read(self.read_int_tag()).decode()
      
    def write_string_tag(self, value: str) -> None:
        self.write_int_tag(len(value))
        self.write(value.encode())
