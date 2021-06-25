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
    def __init__(self, block_storages: dict = {}) -> None:
        if len(block_storages) < 2:
            self.block_storages: dict = {0: block_storage(), 1: block_storage()}
        else:
            self.block_storages: dict = block_storages
                
    def get_block_storage(self, layer: int) -> None:
        if layer not in self.block_storages:
            for i in range(0, layer + 1):
                if i not in self.block_storages:
                    self.block_storages[i] = block_storage()
        return self.block_storages[layer]
    
    def is_empty(self) -> bool:
        return bool(len(self.block_storages) == 0)
    
    def get_block_runtime_id(self, x: int, y: int, z: int, layer: int) -> int:
        return self.get_block_storage(layer).get_block_runtime_id(x, y, z)
    
    def set_block_runtime_id(self, x: int, y: int, z: int, runtime_id: int, layer: int) -> None:
        self.get_block_storage(layer).set_block_runtime_id(x, y, z, runtime_id)
        
    def get_highest_block_at(self, x: int, z: int, layer: int) -> int:
        return self.get_block_storage(layer).get_highest_block_at(x, z)

    async def network_serialize(self, stream: object) -> None:
        stream.write_unsigned_byte(8)
        stream.write_unsigned_byte(len(self.block_storages))
        for storage in self.block_storages.values():
            await storage.network_serialize(stream)
