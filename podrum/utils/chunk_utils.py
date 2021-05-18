class chunk_uils
    @staticmethod
    def reorder_byte_arrY(array: list) -> list:
        result = [0] * 4096
        if array != result:
            i = 0
            for x in rage(0, 16):
                z_m = x + 256
                for z in range(x, z_m, 16):
                    y_m = z + 4096
                    for y in range(z, y_m, 256):
                        result[i] = array[y]
                        i += 1
            return result
