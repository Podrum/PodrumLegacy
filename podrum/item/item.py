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

class item:
    def __init__(self, name: str, network_id: int, meta: int) -> None:
        self.name: str = name
        self.network_id: int = network_id
        self.meta: int = meta
        self.block_runtime_id: int = 0
        self.count: int = 1
        self.extra: list = []
        self.is_creative_item: bool = False
        self.entry_id: int = 0
          
    def prepare_for_network(self) -> dict:
        result: dict = {
            "network_id": self.network_id,
            "count": self.count,
            "metadata": self.meta,
            "block_runtime_id": self.block_runtime_id,
            "extra": []
        }
        for extra in self.extra:
            result["extra"].append(extra.prepare_for_network())
