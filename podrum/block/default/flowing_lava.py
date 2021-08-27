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

from podrum.block.block import block
from podrum.block.tool import tool

class flowing_lava(block):
    def __init__(self) -> None:
        super().__init__("minecraft:flowing_lava", 0, -1, 100, "minecraft:flowing_lava")
        self.tool: int = tool.none
        self.flow_speed: int = 30
        self.flow_distance: int = 4
        self.luminant: int = 15