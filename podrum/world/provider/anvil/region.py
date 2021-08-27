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

from binary_utils.binary_converter import binary_converter
import gzip
import math
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
        while True:
            if not os.path.isfile(path + ".lock"):
                break
        if not os.path.isfile(path):
            open(path + ".lock", "w").close()
            with open(path, "wb") as file:
                file.write(b"\x00" * 8192)
                file.close()
            try:
                os.remove(path + ".lock")
            except ( PermissionError, FileExistsError ) as e:
                return  
        
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
        file: object = open(self.path, "r+b")
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
        size: int = math.ceil(len(ccc) / 4096)
        remaining: int = (size << 12) - len(ccc)
        ccc += b"\x00" * remaining
        index_location: int = region.get_location(x, z)
        index_location_data: bytes = b""
        timestamp_data: bytes = b""
        chunks_data: bytes = b""
        offset: int = 2
        for i in range(1024):
            if i == (index_location >> 2):
                sector_count: int = size
                index_location_data += binary_converter.write_unsigned_triad_be(offset)
                index_location_data += binary_converter.write_unsigned_byte(sector_count)
                timestamp_data += binary_converter.write_unsigned_int_be(int(time.time()))
                chunks_data += ccc
                offset += sector_count
            else:
                file.seek(i << 2)
                chunk_offset: int = binary_converter.read_unsigned_triad_be(file.read(3))
                sector_count: int = binary_converter.read_unsigned_byte(file.read(1))
                if chunk_offset > 0 and sector_count > 0:
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
