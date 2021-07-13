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

class item_manager:
    def __init__(self, server: object) -> None:
        self.items: dict = {}
        self.server: object = server

    def register_item(self, item_obj: object) -> None:
        self.items[f"{item_obj.name} {item_obj.meta}"] = item_obj
        
    def remove_item(self, name: str, meta: int) -> None:
        if f"{name} {meta}" in self.items:
            del self.items[f"{name} {meta}"]

    def get_item(self, name: str, meta: int) -> object:
        if f"{name} {meta}" in self.items:
            return self.items[f"{name} {meta}"]
