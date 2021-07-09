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

from podrum.world.chunk.block_storage import block_storage

class sub_chunk:
    def __init__(self, block_storages: list = []) -> None:
        if len(block_storages) < 2:
            self.block_storages: list = [block_storage(), block_storage()]
        else:
            self.block_storages: list = block_storages
    
    def get_block_runtime_id(self, x: int, y: int, z: int, layer: int) -> int:
        return self.block_storages[layer].get_block_runtime_id(x, y, z)
    
    def set_block_runtime_id(self, x: int, y: int, z: int, runtime_id: int, layer: int) -> None:
        self.block_storages[layer].set_block_runtime_id(x, y, z, runtime_id)
        
    def get_highest_block_at(self, x: int, z: int, layer: int) -> int:
        return self.get_block_storage(layer).get_highest_block_at(x, z)
    
    def is_empty(self) -> bool:
        for storage in self.block_storages:
            if not storage.is_empty():
                return False
        return True

    def network_deserialize(self, stream: object) -> None:
        version: int = stream.read_unsigned_byte()
        if version != 8:
            raise Exception("Unsupported SubChunk version.")
        self.block_storages: dict = {}
        for i in range(0, stream.read_unsigned_byte()):
            storage: object = block_storage()
            storage.network_deserialize(stream)
            self.block_storages[i] = storage
    
    def network_serialize(self, stream: object) -> None:
        stream.write_unsigned_byte(8)
        stream.write_unsigned_byte(len(self.block_storages))
        for storage in self.block_storages.values():
            storage.network_serialize(stream)
