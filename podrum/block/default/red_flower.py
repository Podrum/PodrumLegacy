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

from podrum.block.block import block
from podrum.block.tool import tool
from podrum.block.block_manager import block_manager

class red_flower(block):
    def __init__(self, meta="poppy") -> None:
        self.types = {"poppy": 0, "blue_orchid": 1, "allium": 2, "azure_bluet": 3, "red_tulip": 4, "orange_tulip": 5,
                      "white_tulip": 6, "pink_tulip": 7, "oxeye_daisy": 8, "cornflower": 9, "lily_of_the_valley": 10}
        super().__init__("minecraft:red_flower", self.types[meta] if isinstance(meta, str) else meta, 0, 0)
        self.stack_size: int = 64
        self.tool: int = tool.none
        self.transparent: bool = True
        self.flammable: bool = True
        self.catches_fire_from_lava = True

    def register(self) -> None:
        for i in range(0, len(self.types)):
            block_manager.register_block(block_manager(), red_flower(i))