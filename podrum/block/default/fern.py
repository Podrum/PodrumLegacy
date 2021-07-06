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

class fern(block):
    def __init__(self) -> None:
        super().__init__("minecraft:tallgrass", 2, 0, 0, "minecraft:tallgrass")
        self.stack_size: int = 64
        self.tool: int = tool.shears
        self.transparent: bool = True
        self.flammable: bool = True
        self.catches_fire_from_lava = True