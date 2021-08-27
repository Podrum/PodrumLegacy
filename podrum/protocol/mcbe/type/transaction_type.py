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

class transaction_type:
    type_normal: int = 0
    type_inventory_mismatch: int = 1
    type_item_use: int = 2
    type_item_use_on_entity: int = 3
    type_item_release: int = 4
    type_action_interact: int = 0
    type_action_attack: int = 1   
    type_action_release: int = 0
    type_action_consume: int = 1