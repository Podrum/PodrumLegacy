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

from podrum.block.block_map import block_map
from podrum.block.tool import tool
from podrum.game_data.mcbe.item_states import item_states
from podrum.item.item_map import item_map

class block:

    def __init__(
            self,
            name: str,
            meta: int,
            hardness: float,
            blast_resistance: float,
            item_name: str = ""
    ) -> None:
        self.name: str = name
        self.meta: int = meta
        self.hardness: float = hardness
        self.blast_resistance: float = blast_resistance
        self.item_name: str = item_name
        self.runtime_id: int = block_map.get_runtime_id(name, meta)
        self.network_id: int = item_map.name_to_runtime_id(item_name)
        self.stack_size: int = 0
        self.tool: int = tool.none
        self.luminant: bool = False
        self.transparent: bool = False
        self.flammable: bool = False
        self.catches_fire_from_lava: bool = False
        self.creates_sources: bool = False
        self.flow_distance: int = 0
        self.flow_speed: int = 0
