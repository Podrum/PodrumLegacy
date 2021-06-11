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

from block.block_manager import block_manager
from block.block_map import block_map
from block.default.air import air
from block.default.andesite import andesite
from block.default.andesite_smooth import andesite_smooth
from block.default.bedrock import bedrock
from block.default.cobblestone import cobblestone
from block.default.diorite import diorite
from block.default.diorite_smooth import diorite_smooth
from block.default.dirt import dirt
from block.default.granite import granite
from block.default.granite_smooth import granite_smooth
from block.default.grass import grass
from block.default.stone import stone
from command.command_interface import command_interface
from command.command_manager import command_manager
from command.default.help_command import help_command
from command.default.plugins_command import plugins_command
from command.default.reload_command import reload_command
from command.default.say_command import say_command
from command.default.stop_command import stop_command
from command.default.version_command import version_command
from config import config
from console.logger import logger
from event.event_manager import event_manager
import os
from plugin_manager import plugin_manager
from protocol.mcbe.rak_net_interface import rak_net_interface
import time
from world.generator.flat import flat
from world.generator.void import void
from world.generator_manager import generator_manager
from world.provider.anvil.anvil import anvil
from world.provider.pm_anvil.pm_anvil import pm_anvil
from world.provider_manager import provider_manager
from world.world_manager import world_manager

class server:
    def __init__(self) -> None:
        self.setup_config()
        self.command_manager: object = command_manager(self)
        self.command_interface: object = command_interface(self)
        self.event_manager: object = event_manager(self)
        self.block_manager: object = block_manager()
        self.provider_manager: object = provider_manager()
        self.generator_manager: object = generator_manager()
        self.world_manager: object = world_manager(self)
        self.rak_net_interface: object = rak_net_interface(self)
        self.logger: object = logger()
        self.plugin_manager: object = plugin_manager(self)
        self.players: dict = {}
        self.current_entity_id: int = 1
        self.start()

    def register_default_commands(self) -> None:
        self.command_manager.register(help_command())
        self.command_manager.register(plugins_command())
        self.command_manager.register(reload_command())
        self.command_manager.register(say_command())
        self.command_manager.register(stop_command())
        self.command_manager.register(version_command())
        
    def register_default_providers(self) -> None:
        self.provider_manager.register_provider(anvil)
        self.provider_manager.register_provider(pm_anvil)
        
    def register_default_generators(self) -> None:
        self.generator_manager.register_generator(flat())
        self.generator_manager.register_generator(void())
        
    def register_default_blocks(self) -> None:
        self.block_manager.register_block(air())
        self.block_manager.register_block(andesite())
        self.block_manager.register_block(andesite_smooth())
        self.block_manager.register_block(bedrock())
        self.block_manager.register_block(cobblestone())
        self.block_manager.register_block(diorite())
        self.block_manager.register_block(diorite_smooth())
        self.block_manager.register_block(dirt())
        self.block_manager.register_block(granite())
        self.block_manager.register_block(granite_smooth())
        self.block_manager.register_block(grass())
        self.block_manager.register_block(stone())
        
    def register_events(self) -> None:
        pass

    def get_plugin_main(self, name):
        if name in self.plugin_manager.plugins:
            return self.plugin_manager.plugins[name]
        
    def get_root_path(self):
        return os.path.abspath(os.path.dirname(__file__))
    
    def setup_config(self) -> None:
        path: str = os.path.join(os.getcwd(), "server.json")
        self.config: object = config(path)
        if "ip_address" not in self.config.data:
            self.config.data["ip_address"]: dict = {}
        if "hostname" not in self.config.data["ip_address"]:
            self.config.data["ip_address"]["hostname"]: str = ".".join(["0"] * 4)
        if "port" not in self.config.data["ip_address"]:
            self.config.data["ip_address"]["port"]: int = 19132
        if "motd" not in self.config.data:
            self.config.data["motd"]: str = "Podrum Server"
        if "max_players" not in self.config.data:
            self.config.data["max_players"]: int = 20
        if "max_view_distance" not in self.config.data:
            self.config.data["max_view_distance"]: int = 8
        if "world_provider" not in self.config.data:
            self.config.data["world_provider"]: int = "anvil"
        if "world_name" not in self.config.data:
            self.config.data["world_name"]: int = "world"
        self.config.save()      

    def start(self) -> None:
        start_time: float = time.time()
        self.logger.info("Podrum is starting up...")
        block_map.load_map()
        self.register_default_blocks()
        self.register_default_generators()
        plugins_path: str = os.path.join(os.getcwd(), "plugins")
        if not os.path.isfile(plugins_path) and not os.path.isdir(plugins_path):
            os.mkdir(plugins_path)
        self.plugin_manager.load_all(plugins_path)
        self.register_default_providers()
        worlds_path: str = os.path.join(os.getcwd(), "worlds")
        if not os.path.isfile(worlds_path) and not os.path.isdir(worlds_path):
            os.mkdir(worlds_path)
        self.world_manager.load_world(self.config.data["world_name"])
        self.world: object = self.world_manager.get_world_from_folder_name(self.config.data["world_name"])
        self.register_default_commands()
        self.register_events()
        self.command_interface.start_interface()
        self.rak_net_interface.start_interface()
        finish_time: float = time.time()
        startup_time: float = "%.3f" % (finish_time - start_time)
        self.logger.success(f"Done in {startup_time}. Type help to view all available commands.")

    def stop(self) -> None:
        self.rak_net_interface.stop_interface()
        self.command_interface.stop_interface()
        self.plugin_manager.unload_all()
        self.world_manager.unload_all()

    def send_message(self, message: str) -> None:
        self.logger.info(message)
