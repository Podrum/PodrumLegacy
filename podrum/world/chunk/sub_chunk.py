class sub_chunk:
    def __init__(self, ids: list = [], data: list = [], sky_light: list = [], block_light: list = []) -> None:
        if len(ids) == 4096:
            self.ids: list = ids
        else:
            self.ids: list = [0] * 4096
        if len(data) == 2048:
            self.data: list = data
        else:
            self.data: list = [0] * 2048
        if len(sky_light) == 2048:
            self.sky_light: list = sky_light
        else:
            self.sky_light: list = [255] * 2048
        if len(block_light) == 2048:
            self.block_light: list = block_light
        else:
            self.block_light: list = [0] * 2048

    @staticmethod
    def get_id_index(x: int, y: int, z: int) -> int:
        return (x << 8) | (z << 4) | y

    @staticmethod
    def get_data_index(x: int, y: int, z: int) -> int:
        return (x << 7) + (z << 3) + (y >> 1)

    @staticmethod
    def get_light_index(x: int, y: int, z: int) -> int:
        return sub_chunk.get_data_index(x, y, z)

    def set_block_id(self, x: int, y: int, z: int, block_id: int) -> None:
        self.ids[sub_chunk.get_id_index(x, y, z)]: int = block_id

    def get_highest_block_at(self, x: int, z: int) -> int:
        low: int = (x << 8) | (z << 4)
        i: int = low | 0x0f
        while i >= low:
            if self.ids[i] != 0x00:
                return i & 0x0f
            i -= 1
        return -1

    def encode(self) -> bytes:
        return bytes([0] + self.ids + self.data)
