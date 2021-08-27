r"""
  ____           _
 |  _ \ ___   __| |_ __ _   _ _ __ ___
 | |_) / _ \ / _` | '__| | | | '_ ` _ \
 |  __/ (_) | (_| | |  | |_| | | | | | |
 |_|   \___/ \__,_|_|   \__,_|_| |_| |_|

 Copyright 2021 Podrum Team.

 This file is licensed under the GPL v2.0 license.
 The license file is located in the root directory
 of the source code. If not you may not use this file.
"""

class chunk_utils:
    @staticmethod
    def get_nibble_4(items: list, index: int) -> int:
        if index % 2 == 0:
            return items[index >> 1] & 0x0f
        return (items[index >> 1] >> 4) & 0x0f
        
    @staticmethod
    def set_nibble_4(items: list, index: int, value: int) -> list:
        if index % 2 == 0:
            items[index >> 1] = chunk_utils.get_nibble_4(items, index - 1) << 4 | value
        else:
            items[index >> 1] = value << 4 | chunk_utils.get_nibble_4(items, index + 1)
