################################################################################
#                                                                              #
#  ____           _                                                            #
# |  _ \ ___   __| |_ __ _   _ _ __ ___                                        #
# | |_) / _ \ / _` | '__| | | | '_ ` _ \                                       #
# |  __/ (_) | (_| | |  | |_| | | | | | |                                      #
# |_|   \___/ \__,_|_|   \__,_|_| |_| |_|                                      #
#                                                                              #
# Copyright 2021 Podrum Studios                                                #
#                                                                              #
# Permission is hereby granted, free of charge, to any person                  #
# obtaining a copy of this software and associated documentation               #
# files (the "Software"), to deal in the Software without restriction,         #
# including without limitation the rights to use, copy, modify, merge,         #
# publish, distribute, sublicense, and/or sell copies of the Software,         #
# and to permit persons to whom the Software is furnished to do so,            #
# subject to the following conditions:                                         #
#                                                                              #
# The above copyright notice and this permission notice shall be included      #
# in all copies or substantial portions of the Software.                       #
#                                                                              #
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR   #
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,     #
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE  #
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER       #
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING      #
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS #
# IN THE SOFTWARE.                                                             #
#                                                                              #
################################################################################

from world.world import world
import os

class world_manager:
    def __init__(self, server: object) -> None:
        self.server: object = server
        self.worlds: dict = {}
        self.path_to_world_name = {}
        
    def get_default_world_path(self) -> str:
        return os.path.join(os.getcwd(), "worlds")
        
    def load_world(self, world_folder_name: str, worlds_path: str = "") -> None:
        if len(worlds_path) < 1:
            worlds_path: str = self.get_default_world_path()
        world_path: str = os.path.join(worlds_path, world_folder_name)
        world_obj: object = world(
            self.server.provider_manager.get_provider(
                self.server.config.data["world_provider"]
            )
            (world_path),
            self.server
        )
        world_name: str = world_obj.get_world_name()
        self.worlds[world_name]: object = world_obj
        self.path_to_world_name[world_path]: str = world_name
        self.server.logger.success(f"Loading world -> {world_name}")
        self.worlds[world_name].load_spawn_area()
        self.server.logger.success(f"Loaded world -> {world_name}")
        
    def get_world(self, name: str) -> object:
        return self.worlds[name]
    
    def get_world_from_folder_name(self, world_folder_name: str, worlds_path: str = "") -> None:
        if len(worlds_path) < 1:
            worlds_path: str = self.get_default_world_path()
        world_path: str = os.path.join(worlds_path, world_folder_name)
        return self.get_world(self.path_to_world_name[world_path])
        
    def unload_world(self, world_name: str) -> None:
        self.worlds[world_name].save()
        del self.worlds[world_name]

    def unload_all(self) -> None:
        for world_name in dict(self.worlds):
            self.unload_world(world_name)
