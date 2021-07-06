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

class stone(block):
    def __init__(self, meta="stone") -> None:
        self.types = {"stone": 0, "granite": 1, "polished_granite": 2, "diorite": 3, "polished_diorite": 4, "andesite": 5, "polished_andesite": 6}
        super().__init__("minecraft:stone", self.types[(str(meta).lower()).replace(" ", "_")] if isinstance(meta, str) else meta, 1.5, 6)
        self.stack_size: int = 64
        self.tool: int = tool.pickaxe

    def register(self) -> None:
        for i in range(0, len(self.types)):
            block_manager.register_block(block_manager(), stone(i))