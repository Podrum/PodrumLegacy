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


class flowing_water(block):

    def __init__(self) -> None:
        super().__init__(
            "minecraft:flowing_water",
            0, -1, 100,
            "minecraft:flowing_water"
        )

        self.transparent: bool = True
        self.creates_sources: bool = True
        self.flow_speed: int = 8
        self.flow_speed: int = 5
