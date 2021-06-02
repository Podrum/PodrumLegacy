from world.chunk.block_storage import block_storage

class sub_chunk:
    def __init__(self, block_storages: dict) -> None:
        self.block_storages: object = block_storages

    def get_block_storage(self, layer: int) -> object:
        temp: int = (len(self.block_storages) - 1) - layer
        needs: int = 0 if temp > 0 else abs(temp)
        for i in range(0, needs):
            self.block_storages.append(block_storage())
        return self.block_storages[layer]
    
    def is_empty(self) -> bool:
        return bool(len(self.block_storages))
    
    def get_block(self, x: int, y: int, z: int, layer: int) -> tuple:
        return self.get_block_storage(layer).get_block(x, y & 0x0f, z)
    
    def get_block(self, x: int, y: int, z: int, block_id: int, meta: int, layer: int) -> None:
        self.get_block_storage(layer).set_block(x, y & 0x0f, z, block_id, meta)

    def network_serialize(self, stream: object) -> None:
        stream.write_unsigned_byte(8)
        stream.write_unsigned_byte(len(self.block_storages))
        for block_storage in self.block_storages:
            block_storage.network_serialize(stream)
