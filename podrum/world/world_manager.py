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

import os
from podrum.world.world import world
from podrum.task.immediate_task import immediate_task

class world_manager:
    def __init__(self, server: object) -> None:
        self.server: object = server
        self.worlds: dict = {}
        self.path_to_world_name = {}
    
    # [get_default_world_path]
    # :return: = str
    # Gets the path of the default world
    def get_default_world_path(self) -> str:
        return os.path.join(os.getcwd(), "worlds")
        
    # [load_world]
    # :return: = None
    # Loads a world from the file location.
    def load_world(self, world_folder_name: str, worlds_path: str = "") -> None:
        if len(worlds_path) < 1:
            worlds_path: str = self.get_default_world_path()
        world_path: str = os.path.join(worlds_path, world_folder_name)
        world_obj: object = world(
            self.server.managers.provider_manager.get_provider(
                self.server.config.data["world_provider"]
            )
            (world_path),
            self.server
        )
        world_name: str = world_obj.get_world_name()
        self.worlds[world_name] = world_obj
        self.path_to_world_name[world_path] = world_name
        spawn_pos: object = self.worlds[world_name].get_spawn_position()
        self.server.logger.success(f"Loaded world -> {world_name}")
    
    # [get_world]
    # :return: = object
    # Gets a world by name
    def get_world(self, name: str) -> object:
        return self.worlds[name]
    
    # [get_world_from_folder_name]
    # :return: = object
    # Gets a world by folder name
    def get_world_from_folder_name(self, world_folder_name: str, worlds_path: str = "") -> object:
        if len(worlds_path) < 1:
            worlds_path: str = self.get_default_world_path()
        world_path: str = os.path.join(worlds_path, world_folder_name)
        return self.get_world(self.path_to_world_name[world_path])
    
    # [unload_world]
    # :return: = None
    # Unloads a world
    def unload_world(self, world_name: str) -> None:
        self.worlds[world_name].save()
        del self.worlds[world_name]

    # [unload_all]
    # :return: = None
    # Unloads all worlds
    def unload_all(self) -> None:
        tasks: list = []
        for world_name in dict(self.worlds):
            unload_task: object = immediate_task(self.unload_world, [world_name])
            unload_task.start()
            tasks.append(unload_task)
        for task in tasks:
            task.join()
