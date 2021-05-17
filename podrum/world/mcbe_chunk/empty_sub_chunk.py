from world.mcbe_chunk.sub_chunk import sub_chunk

class empty_sub_chunk(sub_chunk):
    def set_block_id(self, x: int, y: int, z: int, block_id: int) -> None:
        pass

    def get_highest_block_at(self, x: int, z: int) -> int:
        return 0

    def encode(self) -> bytes:
        return b"\x00" * 6145
