from struct import unpack, pack
import uuid

class Binary

    BIG_ENDIAN = 0x00
    LITTLE_ENDIAN = 0x01

    @staticmethod
    def strlen(x):
        return len(x)
    
    @staticmethod
    def checkLength(str, expect):
        len = self.strlen(str)
        assert (len == expect), 'Expected ' + expect + ' bytes, got' + len

    @staticmethod
    def readTriad(str):
        self.checkLength(str, 3)
        return unpack('<i', b'\x00' + str)[0]
