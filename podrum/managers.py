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

from podrum.block.block_manager import block_manager
from podrum.block.default.air import air
from podrum.block.default.andesite import andesite
from podrum.block.default.andesite_smooth import andesite_smooth
from podrum.block.default.bedrock import bedrock
from podrum.block.default.cobblestone import cobblestone
from podrum.block.default.diorite import diorite
from podrum.block.default.diorite_smooth import diorite_smooth
from podrum.block.default.dirt import dirt
from podrum.block.default.granite import granite
from podrum.block.default.granite_smooth import granite_smooth
from podrum.block.default.grass import grass
from podrum.block.default.stone import stone
from podrum.command.command_manager import command_manager
from podrum.command.default.debug_command import debug_command
from podrum.command.default.help_command import help_command
from podrum.command.default.plugins_command import plugins_command
from podrum.command.default.reload_command import reload_command
from podrum.command.default.say_command import say_command
from podrum.command.default.stop_command import stop_command
from podrum.command.default.version_command import version_command
from podrum.event.default_events import default_events
from podrum.event.event_manager import event_manager
from podrum.item.default.stone import stone as stone_item
from podrum.item.item_manager import item_manager
from podrum.plugin_manager import plugin_manager
from podrum.world.generator.flat import flat
from podrum.world.generator.void import void
from podrum.world.generator_manager import generator_manager
from podrum.world.provider.anvil.anvil import anvil
from podrum.world.provider.pm_anvil.pm_anvil import pm_anvil
from podrum.world.provider_manager import provider_manager
from podrum.world.world_manager import world_manager

class managers:
    def __init__(self, server: object) -> None:
        self.server: object = server
        self.block_manager: object = block_manager()
        self.command_manager: object = command_manager()
        self.event_manager: object = event_manager()
        self.item_manager: object = item_manager()
        self.plugin_manager: object = plugin_manager(server)
        self.generator_manager: object = generator_manager()
        self.provider_manager: object = provider_manager()
        self.world_manager: object = world_manager(server)
        self.register_defaults()
            
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
            
    def register_default_commands(self) -> None:
        self.command_manager.register(debug_command(self.server))
        self.command_manager.register(help_command(self.server))
        self.command_manager.register(plugins_command(self.server))
        self.command_manager.register(reload_command(self.server))
        self.command_manager.register(say_command(self.server))
        self.command_manager.register(stop_command(self.server))
        self.command_manager.register(version_command(self.server))
        
    def register_default_events(self) -> None:
        self.event_manager.register_event("execute_command", default_events.execute_command_event)
        
    def register_default_items(self) -> None:
        self.item_manager.register_item(stone_item())
        
    def register_default_generators(self) -> None:
        self.generator_manager.register_generator(flat())
        self.generator_manager.register_generator(void())
        
    def register_default_providers(self) -> None:
        self.provider_manager.register_provider(anvil)
        self.provider_manager.register_provider(pm_anvil)
        
    def register_defaults(self) -> None:
        self.register_default_blocks()
        self.register_default_commands()
        self.register_default_events()
        self.register_default_items()
        self.register_default_generators()
        self.register_default_providers()
