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

from podrum.block.block_map import block_map
from podrum.game_data.mcbe.item_id_map import item_id_map
from podrum.item.item import item

class stone(item):
    def __init__(self, count: int = 1):
        super().__init__("minecraft:stone", item_id_map["minecraft:stone"], 0)
        self.block_runtime_id: int = block_map.get_runtime_id("minecraft:stone", self.meta)
        self.count: int = count
        self.is_creative_item: bool = True
        self.entry_id: int = 0
