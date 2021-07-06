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
from podrum.block import blocks
from podrum.command.command_manager import command_manager
from podrum.command import commands
from podrum.event.event_manager import event_manager
from podrum.event import events
from podrum.item.default.stone import stone as stone_item
from podrum.item.item_manager import item_manager
from podrum.plugin_manager import plugin_manager
from podrum.world.generator_manager import generator_manager
from podrum.world import generators
from podrum.world.provider_manager import provider_manager
from podrum.world import providers
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
    
    # [register_default_blocks]
    # :return: = None
    # Register the default blocks.
    def register_default_blocks(self) -> None:
        self.block_manager.register_block(blocks.air())
        self.block_manager.register_block(blocks.bedrock())
        self.block_manager.register_block(blocks.bone_block())
        self.block_manager.register_block(blocks.bookshelf())
        self.block_manager.register_block(blocks.brewing_stand())
        self.block_manager.register_block(blocks.brown_mushroom())
        self.block_manager.register_block(blocks.cactus())
        self.block_manager.register_block(blocks.clay())
        self.block_manager.register_block(blocks.coal_block())
        self.block_manager.register_block(blocks.coal_ore())
        self.block_manager.register_block(blocks.cobblestone())
        self.block_manager.register_block(blocks.cobweb())
        self.block_manager.register_block(blocks.crafting_table())
        self.block_manager.register_block(blocks.dandelion())
        self.block_manager.register_block(blocks.daylight_sensor())
        self.block_manager.register_block(blocks.deadbush())
        self.block_manager.register_block(blocks.diamond_block())
        self.block_manager.register_block(blocks.diamond_ore())
        self.block_manager.register_block(blocks.dirt())
        self.block_manager.register_block(blocks.emerald_block())
        self.block_manager.register_block(blocks.emerald_ore())
        self.block_manager.register_block(blocks.end_stone())
        self.block_manager.register_block(blocks.enchanting_table())
        self.block_manager.register_block(blocks.flower_pot())
        self.block_manager.register_block(blocks.farmland())
        self.block_manager.register_block(blocks.fire())
        self.block_manager.register_block(blocks.glass())
        self.block_manager.register_block(blocks.glass_pane())
        self.block_manager.register_block(blocks.gold_block())
        self.block_manager.register_block(blocks.gold_ore())
        self.block_manager.register_block(blocks.grass())
        self.block_manager.register_block(blocks.gravel())
        self.block_manager.register_block(blocks.hardened_clay())
        self.block_manager.register_block(blocks.hay_bale())
        self.block_manager.register_block(blocks.ice())
        self.block_manager.register_block(blocks.iron_bars())
        self.block_manager.register_block(blocks.iron_block())
        self.block_manager.register_block(blocks.iron_ore())
        self.block_manager.register_block(blocks.lapis_block())
        self.block_manager.register_block(blocks.lapis_ore())
        self.block_manager.register_block(blocks.lava())
        self.block_manager.register_block(blocks.lit_pumpkin())
        self.block_manager.register_block(blocks.magma())
        self.block_manager.register_block(blocks.monster_spawner())
        self.block_manager.register_block(blocks.melon())
        self.block_manager.register_block(blocks.mossy_cobblestone())
        self.block_manager.register_block(blocks.mycelium())
        self.block_manager.register_block(blocks.nether_wart_block())
        self.block_manager.register_block(blocks.nether_brick_block())
        self.block_manager.register_block(blocks.nether_quartz_ore())
        self.block_manager.register_block(blocks.netherrack())
        self.block_manager.register_block(blocks.noteblock())
        self.block_manager.register_block(blocks.obsidian())
        self.block_manager.register_block(blocks.packed_ice())
        self.block_manager.register_block(blocks.podzol())
        self.block_manager.register_block(blocks.prismarine())
        self.block_manager.register_block(blocks.pumpkin())
        self.block_manager.register_block(blocks.purpur())
        self.block_manager.register_block(blocks.quartz_block())
        self.block_manager.register_block(blocks.red_mushroom())
        self.block_manager.register_block(blocks.red_sandstone())
        self.block_manager.register_block(blocks.redstone_block())
        self.block_manager.register_block(blocks.redstone_lamp())
        self.block_manager.register_block(blocks.redstone_ore())
        self.block_manager.register_block(blocks.sand())
        self.block_manager.register_block(blocks.sandstone())
        self.block_manager.register_block(blocks.snow_block())
        self.block_manager.register_block(blocks.soul_sand())
        self.block_manager.register_block(blocks.sponge())
        self.block_manager.register_block(blocks.stone_bricks())
        self.block_manager.register_block(blocks.tnt())
        self.block_manager.register_block(blocks.wooden_planks())
        self.block_manager.register_block(blocks.water())
        self.block_manager.register_block(blocks.tallgrass())
        self.block_manager.register_block(blocks.sugar_cane())
        self.block_manager.register_block(blocks.glowing_obsidian())
        self.block_manager.register_block(blocks.yellow_flower())
        self.block_manager.register_block(blocks.double_plant())
        self.block_manager.register_block(blocks.anvil())
        self.block_manager.register_block(blocks.lily_pad())
        self.block_manager.register_block(blocks.end_stone_brick())
        self.block_manager.register_block(blocks.sea_lantern())
        self.block_manager.register_block(blocks.invisible_bedrock())
        self.block_manager.register_block(blocks.white_wool())
        self.block_manager.register_block(blocks.orange_wool())
        self.block_manager.register_block(blocks.magenta_wool())
        self.block_manager.register_block(blocks.lime_wool())
        self.block_manager.register_block(blocks.yellow_wool())
        self.block_manager.register_block(blocks.light_blue_wool())
        self.block_manager.register_block(blocks.pink_wool())
        self.block_manager.register_block(blocks.gray_wool())
        self.block_manager.register_block(blocks.light_gray_wool())
        self.block_manager.register_block(blocks.cyan_wool())
        self.block_manager.register_block(blocks.purple_wool())
        self.block_manager.register_block(blocks.blue_wool())
        self.block_manager.register_block(blocks.brown_wool())
        self.block_manager.register_block(blocks.green_wool())
        self.block_manager.register_block(blocks.red_wool())
        self.block_manager.register_block(blocks.black_wool())
        self.block_manager.register_block(blocks.stone())
        self.block_manager.register_block(blocks.granite())
        self.block_manager.register_block(blocks.polished_granite())
        self.block_manager.register_block(blocks.diorite())
        self.block_manager.register_block(blocks.polished_diorite())
        self.block_manager.register_block(blocks.andesite())
        self.block_manager.register_block(blocks.polished_andesite())
        self.block_manager.register_block(blocks.poppy())
        self.block_manager.register_block(blocks.blue_orchid())
        self.block_manager.register_block(blocks.oxeye_daisy())
        self.block_manager.register_block(blocks.azure_bluet())
        self.block_manager.register_block(blocks.white_tulip())
        self.block_manager.register_block(blocks.pink_tulip())
        self.block_manager.register_block(blocks.red_tulip())
        self.block_manager.register_block(blocks.orange_tulip())
        self.block_manager.register_block(blocks.cornflower())
        self.block_manager.register_block(blocks.lily_of_the_valley())
        self.block_manager.register_block(blocks.allium())

        blocks.concrete.register(blocks.concrete())

    
    # [register_default_commands]
    # :return: = None
    # Registers the default commands.
    def register_default_commands(self) -> None:
        self.command_manager.register(commands.debug_command(self.server))
        self.command_manager.register(commands.help_command(self.server))
        self.command_manager.register(commands.plugins_command(self.server))
        self.command_manager.register(commands.reload_command(self.server))
        self.command_manager.register(commands.say_command(self.server))
        self.command_manager.register(commands.stop_command(self.server))
        self.command_manager.register(commands.tell_command(self.server))
        self.command_manager.register(commands.version_command(self.server))
        self.command_manager.register(commands.kick_command(self.server))
    
    # [register_default_events]
    # :return: = None
    # Registers the default events.
    def register_default_events(self) -> None:
        event_manager.register_event(events.player_join_event)
        event_manager.register_event(events.player_move_event)
        event_manager.register_event(events.player_quit_event)
        event_manager.register_event(events.player_sneak_event)
        event_manager.register_event(events.player_sprint_event)
        event_manager.register_event(events.player_jump_event)
        event_manager.register_event(events.player_chat_event)
        event_manager.register_event(events.player_form_response_event)
    
    # [register_default_items]
    # :return: = None
    # Registers the default items.
    def register_default_items(self) -> None:
        self.item_manager.register_item(stone_item())
    
    # [register_default_generators]
    # :return: = None
    # Registers the default generators.
    def register_default_generators(self) -> None:
        self.generator_manager.register_generator(generators.flat())
        self.generator_manager.register_generator(generators.void())
        self.generator_manager.register_generator(generators.default())
    
    # [register_default_providers]
    # :return: = None
    # Registers the default providers.
    def register_default_providers(self) -> None:
        self.provider_manager.register_provider(providers.anvil)
        self.provider_manager.register_provider(providers.pm_anvil)
        
    
    # [register_defaults]
    # :return: = None
    # Registers all the defaults.
    def register_defaults(self) -> None:
        self.register_default_blocks()
        self.register_default_commands()
        self.register_default_events()
        self.register_default_items()
        self.register_default_generators()
        self.register_default_providers()
