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

from binary_utils.binary_converter import binary_converter
import gzip
import os
import time
import zlib

class region:
    def __init__(self, path: str) -> None:
        self.path: str = path
        file_name: str = os.path.basename(path)
        file_name_shards: list = file_name.split(".")
        self.x: int = int(file_name_shards[1])
        self.z: int = int(file_name_shards[2])
        self.format: str = file_name_shards[3]
        if not os.path.isfile(path):
            file: object = open(path, "wb")
            file.write(b"\x00" * 8192)

    @staticmethod
    def get_location(x: int, z: int) -> int:
        return 4 * ((x & 31) + (z & 31) * 32)

    def get_chunk_data(self, x: int, z: int) -> bytes:
        file: object = open(self.path, "rb")
        index_location: int = region.get_location(x, z)
        file.seek(index_location)
        offset: int = binary_converter.read_unsigned_triad_be(file.read(3))
        sector_count: int = binary_converter.read_unsigned_byte(file.read(1))
        if offset == 0 and sector_count == 0:
            return b""
        file.seek(offset << 12)
        length: int = binary_converter.read_unsigned_int_be(file.read(4))
        compression_type: int = binary_converter.read_unsigned_byte(file.read(1))
        chunk_data: bytes = file.read(length)
        file.close()
        if compression_type == 1:
            return gzip.decompress(chunk_data)
        if compression_type == 2:
            return zlib.decompress(chunk_data)
        if compression_type == 3:
            return chunk_data

    def put_chunk_data(self, x: int, z: int, chunk_data: bytes, compression_type: int = 2) -> None:
        if compression_type == 1:
            cc: bytes = gzip.compress(chunk_data)
        elif compression_type == 2:
            cc: bytes = zlib.compress(chunk_data)
        elif compression_type == 3:
            cc: bytes = chunk_data
        else:
            return
        ccc: bytes = binary_converter.write_unsigned_int_be(len(cc))
        ccc += binary_converter.write_unsigned_byte(compression_type)
        ccc += cc
        size: int = 0
        while True:
            remaining: int = size - len(ccc)
            if remaining > 0:
                ccc += b"\x00" * remaining
                break
            size += 4096
        index_location: int = region.get_location(x, z)
        sector_count: int = len(ccc) >> 12
        file: object = open(self.path, "ab")
        offset: int = file.tell() >> 12
        file.write(ccc)
        file.close()
        index_location_data: bytes = binary_converter.write_unsigned_triad_be(offset)
        index_location_data += binary_converter.write_unsigned_byte(sector_count)
        timestamp_data = binary_converter.write_unsigned_int_be(int(time.time()))
        file: object = open(self.path, "+rb")
        ilo: int = (index_location << 2)
        for i in range(0, 4):
            file.seek(i + ilo)
            file.write(index_location_data)
            file.seek(i + ilo + 4096)
            file.write(timestamp_data)
        file.close()
        
    def remove_chunk_data(self, x: int, z: int) -> None:
        file: object = open(self.path, "r+b")
        index_location: int = self.get_location(x, z)
        index_location_data: bytes = b""
        timestamp_data: bytes = b""
        chunks_data: bytes = b""
        offset: int = 2
        for i in range(0, 1024):
            file.seek(i << 2)
            chunk_offset: int = binary_converter.read_unsigned_triad_be(file.read(3))
            sector_count: int = binary_converter.read_unsigned_byte(file.read(1))
            if chunk_offset > 0 and sector_count > 0 and i != (index_location >> 2):
                index_location_data += binary_converter.write_unsigned_triad_be(offset)
                index_location_data += binary_converter.write_unsigned_byte(sector_count)
                offset += sector_count
                file.seek((i << 2) + 4096)
                timestamp_data += file.read(4)
                file.seek(chunk_offset << 12)
                chunks_data += file.read(sector_count << 12)
            else:
                index_location_data += b"\x00" * 4
                timestamp_data += b"\x00" * 4
        file.seek(0)
        file.write(index_location_data + timestamp_data + chunks_data)
        file.close()
