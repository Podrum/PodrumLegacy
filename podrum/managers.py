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
import podrum.block.blocks as block
from podrum.command.command_manager import command_manager
from podrum.command.default.debug_command import debug_command
from podrum.command.default.help_command import help_command
from podrum.command.default.plugins_command import plugins_command
from podrum.command.default.reload_command import reload_command
from podrum.command.default.say_command import say_command
from podrum.command.default.stop_command import stop_command
from podrum.command.default.version_command import version_command
from podrum.event.default.player.player_join_event import player_join_event
from podrum.event.default.player.player_move_event import player_move_event
from podrum.event.default.player.player_quit_event import player_quit_event
from podrum.event.event_manager import event_manager
from podrum.item.default.stone import stone as stone_item
from podrum.item.item_manager import item_manager
from podrum.plugin_manager import plugin_manager
from podrum.world.generator.flat import flat
from podrum.world.generator.default import default
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
        self.item_manager: object = item_manager()
        self.plugin_manager: object = plugin_manager(server)
        self.generator_manager: object = generator_manager()
        self.provider_manager: object = provider_manager()
        self.world_manager: object = world_manager(server)
        self.register_defaults()
            
    def register_default_blocks(self) -> None:
        self.block_manager.register_block(block.air())
        self.block_manager.register_block(block.andesite())
        self.block_manager.register_block(block.andesite_smooth())
        self.block_manager.register_block(block.bedrock())
        self.block_manager.register_block(block.bone_block())
        self.block_manager.register_block(block.bookshelf())
        self.block_manager.register_block(block.brewing_stand())
        self.block_manager.register_block(block.brown_mushroom())
        self.block_manager.register_block(block.cactus())
        self.block_manager.register_block(block.clay())
        self.block_manager.register_block(block.coal_block())
        self.block_manager.register_block(block.coal_ore())
        self.block_manager.register_block(block.cobblestone())
        self.block_manager.register_block(block.cobweb())
        self.block_manager.register_block(block.crafting_table())
        self.block_manager.register_block(block.dandelion())
        self.block_manager.register_block(block.daylight_sensor())
        self.block_manager.register_block(block.deadbush())
        #self.block_manager.register_block(block.deepslate_gold_ore())
        #self.block_manager.register_block(block.deepslate_redstone_ore())
        #self.block_manager.register_block(block.deepslate_lapis_ore())
        #self.block_manager.register_block(block.deepslate_iron_ore())
        #self.block_manager.register_block(block.deepslate_coal_ore())
        #self.block_manager.register_block(block.deepslate_diamond_ore())
        #self.block_manager.register_block(block.deepslate_emerald_ore())
        self.block_manager.register_block(block.diamond_block())
        self.block_manager.register_block(block.diamond_ore())
        self.block_manager.register_block(block.diorite())
        self.block_manager.register_block(block.diorite_smooth())
        self.block_manager.register_block(block.dirt())
        self.block_manager.register_block(block.emerald_block())
        self.block_manager.register_block(block.emerald_ore())
        self.block_manager.register_block(block.end_stone())
        #self.block_manager.register_block(block.end_stone_brick())
        self.block_manager.register_block(block.enchanting_table())
        self.block_manager.register_block(block.flower_pot())
        self.block_manager.register_block(block.farmland())
        self.block_manager.register_block(block.fire())
        self.block_manager.register_block(block.glass())
        self.block_manager.register_block(block.glass_pane())
        #self.block_manager.register_block(block.glowing_obsidian())
        self.block_manager.register_block(block.gold_block())
        self.block_manager.register_block(block.gold_ore())
        self.block_manager.register_block(block.granite())
        self.block_manager.register_block(block.granite_smooth())
        self.block_manager.register_block(block.grass())
        self.block_manager.register_block(block.gravel())
        self.block_manager.register_block(block.hardened_clay())
        self.block_manager.register_block(block.hay_bale())
        self.block_manager.register_block(block.ice())
        #self.block_manager.register_block(block.invisible_bedrock())
        self.block_manager.register_block(block.iron_bars())
        self.block_manager.register_block(block.iron_block())
        self.block_manager.register_block(block.iron_ore())
        self.block_manager.register_block(block.lapis_block())
        self.block_manager.register_block(block.lapis_ore())
        self.block_manager.register_block(block.lava())
        self.block_manager.register_block(block.lit_pumpkin())
        self.block_manager.register_block(block.magma())
        self.block_manager.register_block(block.monster_spawner())
        self.block_manager.register_block(block.melon())
        self.block_manager.register_block(block.mossy_cobblestone())
        self.block_manager.register_block(block.mycelium())
        self.block_manager.register_block(block.nether_wart_block())
        self.block_manager.register_block(block.nether_brick_block())
        self.block_manager.register_block(block.nether_quartz_ore())
        self.block_manager.register_block(block.netherrack())
        self.block_manager.register_block(block.noteblock())
        self.block_manager.register_block(block.obsidian())
        self.block_manager.register_block(block.packed_ice())
        self.block_manager.register_block(block.podzol())
        self.block_manager.register_block(block.prismarine())
        self.block_manager.register_block(block.pumpkin())
        self.block_manager.register_block(block.purpur())
        self.block_manager.register_block(block.quartz_block())
        self.block_manager.register_block(block.red_mushroom())
        self.block_manager.register_block(block.red_sandstone())
        self.block_manager.register_block(block.redstone_block())
        self.block_manager.register_block(block.redstone_lamp())
        self.block_manager.register_block(block.redstone_ore())
        self.block_manager.register_block(block.sand())
        self.block_manager.register_block(block.sandstone())
        #self.block_manager.register_block(block.sea_lantern())
        self.block_manager.register_block(block.snow_block())
        self.block_manager.register_block(block.soul_sand())
        self.block_manager.register_block(block.sponge())
        self.block_manager.register_block(block.stone())
        self.block_manager.register_block(block.stone_bricks())
        #self.block_manager.register_block(block.sugar_cane())
        self.block_manager.register_block(block.tnt())
        self.block_manager.register_block(block.wooden_planks())
        self.block_manager.register_block(block.wool())
            
    def register_default_commands(self) -> None:
        self.command_manager.register(debug_command(self.server))
        self.command_manager.register(help_command(self.server))
        self.command_manager.register(plugins_command(self.server))
        self.command_manager.register(reload_command(self.server))
        self.command_manager.register(say_command(self.server))
        self.command_manager.register(stop_command(self.server))
        self.command_manager.register(version_command(self.server))
        
    def register_default_events(self) -> None:
        event_manager.register_event(player_join_event)
        event_manager.register_event(player_move_event)
        event_manager.register_event(player_quit_event)
        
    def register_default_items(self) -> None:
        self.item_manager.register_item(stone_item())
        
    def register_default_generators(self) -> None:
        self.generator_manager.register_generator(flat())
        self.generator_manager.register_generator(void())
        self.generator_manager.register_generator(default())
        
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
