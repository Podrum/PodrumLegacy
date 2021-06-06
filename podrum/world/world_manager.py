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
        self.load_world(self.server.config.data["world_name"])
        
    def get_default_world_path(self) -> str:
        return os.path.join(os.getcwd(), "worlds")
        
    def load_world(self, world_name: str, worlds_path: str = "") -> None:
        self.server.logger.info(f"Loading world -> {world_name}")
        if len(worlds_path) < 1:
            worlds_path: str = self.get_default_world_path()
        world_path: str = os.path.join(worlds_path, world_name)
        self.worlds[world_name]: object = world(
            self.server.provider_manager.get_provider(
                self.server.config.data["world_provider"]
            )
            (world_path),
            self.server
        )
        self.server.logger.success(f"Loaded world -> {world_name}")
        
    def unload_world(self, world_name: str) -> None:
        self.worlds[world_name].save()
        del self.worlds[world_name]
