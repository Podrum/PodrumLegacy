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
from podrum.block.default.colors import colors

class wool(block):
    def __init__(self, meta="white") -> None:
        super().__init__("minecraft:wool", colors(meta).color if isinstance(meta, str) else meta, 0.8, 0.8)
        self.stack_size: int = 64
        self.tool: int = tool.shears
        self.flammable: bool = True
        self.catches_fire_from_lava: bool = True

    def register(self) -> None:
        for i in range(0, len(colors().types)):
            block_manager.register_block(block_manager(), wool(i))