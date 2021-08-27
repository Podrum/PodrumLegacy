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

from podrum.item.item import item

class block_manager:

    def __init__(self, managers) -> None:
        self.managers = managers
        self.blocks: dict = {}

    def register_block(self, block_obj: object) -> None:
        self.blocks[f"{block_obj.name} {block_obj.meta}"] = block_obj
        item_obj: object = item(block_obj.item_name, block_obj.network_id, block_obj.meta)
        item_obj.block_runtime_id = block_obj.runtime_id
        self.managers.item_manager.register_item(item_obj)
        
    def remove_block(self, name: str, meta: int) -> None:
        if f"{name} {meta}" in self.blocks:
            del self.blocks[f"{name} {meta}"]

    def get_block(self, name: str, meta: int) -> object:
        if f"{name} {meta}" in self.blocks:
            return self.blocks[f"{name} {meta}"]
