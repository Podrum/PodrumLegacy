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

from podrum.block.block import Block
from podrum.block.tool import tool


class PinkStainedGlass(Block):
    def __init__(self) -> None:
        super().__init__(
            "minecraft:stained_glass",
            6, 0.3, 0.3,
            "minecraft:stained_glass"
        )

        self.stack_size: int = 64
        self.tool: int = tool.none
        self.transparent: bool = True
