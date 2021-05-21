class chunk_utils:
    @staticmethod
    def reorder_byte_array(array: list) -> list:
        result: list = [0] * 4096
        if array != result:
            i: int = 0
            for x in range(0, 16):
                z_m: int = x + 256
                for z in range(x, z_m, 16):
                    y_m: int = z + 4096
                    for y in range(z, y_m, 256):
                        result[i]: int = array[y]
                        i += 1
            return result
        
    @staticmethod
    def reorder_nibble_array(array: list, common_value: int = 0) -> list:
        result: list = [common_value] * 2048
        if array != result:
            i: int = 0
            for x in range(0, 8):
                for z in range(0, 16):
                    zx: int = ((z << 3) | x)
                    for y in range(0, 8):
                        j: int = ((y << 8) | zx)
                        j80: int = (j | 0x80)
                        if array[j] != common_value and array[j80] != common_value:
                            i1: int = array[j]
                            i2: int = array[j80]
                            result[i]: int = (i2 << 4) | (i1 & 0x0f)
                            result[i | 0x80]: int = (i1 >> 4) | (i2 & 0xf0)
                        i += 1
                i += 128
            return result

    @staticmethod
    def convert_biome_colors(array: list) -> list:
        result: list = [0] * 256
        for color in array:
            result.append((color >> 24) & 0xff)
        return result
