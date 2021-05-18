from world.chunk.empty_sub_chunk import empty_sub_chunk
from world.chunk.sub_chunk import sub_chunk

class chunk:
    def __init__(self, x: int, z: int, sub_chunks: dict = {}, entities: dict = {}, tiles: list = [], biomes: list = [], height_map: list = []) -> None:
        self.x: int = x
        self.z: int = z
        self.has_changed: bool = False
        self.height: int = 16
        self.sub_chunks: dict = {}
        self.entities: dict = entities
        self.tiles: list = tiles
        for y in range(0, self.height):
            if y in self.sub_chunks:
                self.sub_chunks[y]: object = sub_chunks[y]
            else:
                self.sub_chunks[y]: object = empty_sub_chunk()
        if len(height_map) == 256:
            self.height_map: list = height_map
        else:
            self.height_map: list = [self.height * 16] * 256
        if len(biomes) == 256:
            self.biomes: list = biomes
        else:
            self.biomes: list = [0] * 256

    @staticmethod
    def get_id_index(x: int, y: int, z: int) -> int:
        return (x << 12) | (z << 8) | y

    @staticmethod
    def get_biome_index(x: int, z: int) -> int:
        return (x << 4) | z

    @staticmethod
    def get_height_map_index(x: int, z: int) -> int:
        return (z << 4) | z
        
    def set_block_id(self, x: int, y: int, z: int, block_id: int) -> None:
        if self.get_sub_chunk(y >> 4, True).set_block_id(x, y & 0x0f, z, block_id):
            self.has_changed: bool = True

    def get_sub_chunk(self, y: int, generate_new: bool = False) -> object:
        if y < 0 or y >= self.height:
            return empty_sub_chunk()
        if generate_new and isinstance(self.sub_chunks[y], empty_sub_chunk):
            self.sub_chunks[y] = sub_chunk()
        return self.sub_chunks[y]

    def set_height_map(self, x: int, z: int, value: int) -> None:
        self.height_map[chunk.get_height_map_index(x, z)]: int = value

    def get_highest_sub_chunk_index(self) -> int:
        for y in range(len(self.sub_chunks) - 1, -1, -1):
            if isinstance(self.sub_chunks[y], empty_sub_chunk):
                continue
            return y

    def get_highest_block(self, x: int, z: int) -> int:
        index: int = self.get_highest_sub_chunk_index()
        if index is None:
            return -1
        for y in range(index, -1, -1):
            height: int = self.get_sub_chunk(y).get_highest_block_at(x, z) | (y << 4)
            if height is not None:
                return height
        return -1

    def get_sub_chunk_send_count(self) -> int:
        index: int = self.get_highest_sub_chunk_index()
        if index is not None:
            return index + 1
        return 0

    def recalculate_height_map(self) -> None:
        for x in range(0, 16):
            for z in range(0, 16):
                self.set_height_map(x, z, self.get_highest_block(x, z) + 1)

    def encode(self) -> bytes:
        data: bytes = b""
        sub_chunk_count: int = self.get_sub_chunk_send_count()
        for y in range(0, sub_chunk_count):
            data += self.sub_chunks[y].encode()
        for biome in self.biomes:
            data += bytes([biome])
        data += b"\x00"
        return data
