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

java_to_bedrock_map: dict = {
    'minecraft:acacia_door': 'minecraft:acacia_door',
    'minecraft:acacia_fence': 192,
    'minecraft:acacia_fence_gate': 'minecraft:acacia_fence_gate',
    'minecraft:acacia_stairs': 'minecraft:acacia_stairs',
    'minecraft:activator_rail': 'minecraft:activator_rail',
    'minecraft:air': 'minecraft:air',
    'minecraft:anvil': 'minecraft:anvil',
    'minecraft:barrier': 'minecraft:barrier',
    'minecraft:beacon': 'minecraft:beacon',
    'minecraft:bed': 'minecraft:bed',
    'minecraft:bedrock': 'minecraft:bedrock',
    'minecraft:beetroots': 207,
    'minecraft:birch_door': 'minecraft:birch_door',
    'minecraft:birch_fence': 189,
    'minecraft:birch_fence_gate': 'minecraft:birch_fence_gate',
    'minecraft:birch_stairs': 'minecraft:birch_stairs',
    'minecraft:black_glazed_terracotta': 'minecraft:black_glazed_terracotta',
    'minecraft:black_shulker_box': 234,
    'minecraft:blue_glazed_terracotta': 'minecraft:blue_glazed_terracotta',
    'minecraft:blue_shulker_box': 230,
    'minecraft:bone_block': 'minecraft:bone_block',
    'minecraft:bookshelf': 'minecraft:bookshelf',
    'minecraft:brewing_stand': 'minecraft:brewing_stand',
    'minecraft:brick_block': 'minecraft:brick_block',
    'minecraft:brick_stairs': 'minecraft:brick_stairs',
    'minecraft:brown_glazed_terracotta': 'minecraft:brown_glazed_terracotta',
    'minecraft:brown_mushroom': 'minecraft:brown_mushroom',
    'minecraft:brown_mushroom_block': 'minecraft:brown_mushroom_block',
    'minecraft:brown_shulker_box': 231,
    'minecraft:cactus': 'minecraft:cactus',
    'minecraft:cake': 'minecraft:cake',
    'minecraft:carpet': 'minecraft:carpet',
    'minecraft:carrots': 'minecraft:carrots',
    'minecraft:cauldron': 'minecraft:cauldron',
    'minecraft:chain_command_block': 'minecraft:chain_command_block',
    'minecraft:chest': 'minecraft:chest',
    'minecraft:chorus_flower': 'minecraft:chorus_flower',
    'minecraft:chorus_plant': 'minecraft:chorus_plant',
    'minecraft:clay': 'minecraft:clay',
    'minecraft:coal_block': 'minecraft:coal_block',
    'minecraft:coal_ore': 'minecraft:coal_ore',
    'minecraft:cobblestone': 'minecraft:cobblestone',
    'minecraft:cobblestone_wall': 'minecraft:cobblestone_wall',
    'minecraft:cocoa': 'minecraft:cocoa',
    'minecraft:command_block': 'minecraft:command_block',
    'minecraft:concrete': 'minecraft:concrete',
    'minecraft:concrete_powder': 252,
    'minecraft:crafting_table': 'minecraft:crafting_table',
    'minecraft:cyan_glazed_terracotta': 'minecraft:cyan_glazed_terracotta',
    'minecraft:cyan_shulker_box': 228,
    'minecraft:dark_oak_door': 'minecraft:dark_oak_door',
    'minecraft:dark_oak_fence': 191,
    'minecraft:dark_oak_fence_gate': 'minecraft:dark_oak_fence_gate',
    'minecraft:dark_oak_stairs': 'minecraft:dark_oak_stairs',
    'minecraft:daylight_detector': 'minecraft:daylight_detector',
    'minecraft:daylight_detector_inverted': 'minecraft:daylight_detector_inverted',
    'minecraft:deadbush': 'minecraft:deadbush',
    'minecraft:detector_rail': 'minecraft:detector_rail',
    'minecraft:diamond_block': 'minecraft:diamond_block',
    'minecraft:diamond_ore': 'minecraft:diamond_ore',
    'minecraft:dirt': 'minecraft:dirt',
    'minecraft:dispenser': 'minecraft:dispenser',
    'minecraft:double_plant': 'minecraft:double_plant',
    'minecraft:double_stone_slab': 'minecraft:double_stone_slab',
    'minecraft:double_stone_slab2': 'minecraft:double_stone_slab2',
    'minecraft:double_wooden_slab': 'minecraft:double_wooden_slab',
    'minecraft:dragon_egg': 'minecraft:dragon_egg',
    'minecraft:dropper': 'minecraft:dropper',
    'minecraft:emerald_block': 'minecraft:emerald_block',
    'minecraft:emerald_ore': 'minecraft:emerald_ore',
    'minecraft:enchanting_table': 'minecraft:enchanting_table',
    'minecraft:end_bricks': 'minecraft:end_bricks',
    'minecraft:end_gateway': 'minecraft:end_gateway',
    'minecraft:end_portal': 'minecraft:end_portal',
    'minecraft:end_portal_frame': 'minecraft:end_portal_frame',
    'minecraft:end_rod': 'minecraft:end_rod',
    'minecraft:end_stone': 'minecraft:end_stone',
    'minecraft:ender_chest': 'minecraft:ender_chest',
    'minecraft:farmland': 'minecraft:farmland',
    'minecraft:fence': 'minecraft:fence',
    'minecraft:fence_gate': 'minecraft:fence_gate',
    'minecraft:fire': 'minecraft:fire',
    'minecraft:flower_pot': 'minecraft:flower_pot',
    'minecraft:flowing_lava': 'minecraft:flowing_lava',
    'minecraft:flowing_water': 'minecraft:flowing_water',
    'minecraft:frosted_ice': 'minecraft:frosted_ice',
    'minecraft:furnace': 'minecraft:furnace',
    'minecraft:glass': 'minecraft:glass',
    'minecraft:glass_pane': 'minecraft:glass_pane',
    'minecraft:glowstone': 'minecraft:glowstone',
    'minecraft:gold_block': 'minecraft:gold_block',
    'minecraft:gold_ore': 'minecraft:gold_ore',
    'minecraft:golden_rail': 'minecraft:golden_rail',
    'minecraft:grass': 'minecraft:grass',
    'minecraft:grass_path': 'minecraft:grass_path',
    'minecraft:gravel': 'minecraft:gravel',
    'minecraft:gray_glazed_terracotta': 'minecraft:gray_glazed_terracotta',
    'minecraft:gray_shulker_box': 226,
    'minecraft:green_glazed_terracotta': 'minecraft:green_glazed_terracotta',
    'minecraft:green_shulker_box': 232,
    'minecraft:hardened_clay': 'minecraft:hardened_clay',
    'minecraft:hay_block': 'minecraft:hay_block',
    'minecraft:heavy_weighted_pressure_plate': 'minecraft:heavy_weighted_pressure_plate',
    'minecraft:hopper': 'minecraft:hopper',
    'minecraft:ice': 'minecraft:ice',
    'minecraft:iron_bars': 'minecraft:iron_bars',
    'minecraft:iron_block': 'minecraft:iron_block',
    'minecraft:iron_door': 'minecraft:iron_door',
    'minecraft:iron_ore': 'minecraft:iron_ore',
    'minecraft:iron_trapdoor': 'minecraft:iron_trapdoor',
    'minecraft:jukebox': 'minecraft:jukebox',
    'minecraft:jungle_door': 'minecraft:jungle_door',
    'minecraft:jungle_fence': 190,
    'minecraft:jungle_fence_gate': 'minecraft:jungle_fence_gate',
    'minecraft:jungle_stairs': 'minecraft:jungle_stairs',
    'minecraft:ladder': 'minecraft:ladder',
    'minecraft:lapis_block': 'minecraft:lapis_block',
    'minecraft:lapis_ore': 'minecraft:lapis_ore',
    'minecraft:lava': 'minecraft:lava',
    'minecraft:leaves': 'minecraft:leaves',
    'minecraft:leaves2': 'minecraft:leaves2',
    'minecraft:lever': 'minecraft:lever',
    'minecraft:light_blue_glazed_terracotta': 'minecraft:light_blue_glazed_terracotta',
    'minecraft:light_blue_shulker_box': 222,
    'minecraft:light_weighted_pressure_plate': 'minecraft:light_weighted_pressure_plate',
    'minecraft:lime_glazed_terracotta': 'minecraft:lime_glazed_terracotta',
    'minecraft:lime_shulker_box': 224,
    'minecraft:lit_furnace': 'minecraft:lit_furnace',
    'minecraft:lit_pumpkin': 'minecraft:lit_pumpkin',
    'minecraft:lit_redstone_lamp': 'minecraft:lit_redstone_lamp',
    'minecraft:lit_redstone_ore': 'minecraft:lit_redstone_ore',
    'minecraft:log': 'minecraft:log',
    'minecraft:log2': 'minecraft:log2',
    'minecraft:magenta_glazed_terracotta': 'minecraft:magenta_glazed_terracotta',
    'minecraft:magenta_shulker_box': 221,
    'minecraft:magma': 'minecraft:magma',
    'minecraft:melon_block': 'minecraft:melon_block',
    'minecraft:melon_stem': 'minecraft:melon_stem',
    'minecraft:mob_spawner': 'minecraft:mob_spawner',
    'minecraft:monster_egg': 'minecraft:monster_egg',
    'minecraft:mossy_cobblestone': 'minecraft:mossy_cobblestone',
    'minecraft:mycelium': 'minecraft:mycelium',
    'minecraft:nether_brick': 'minecraft:nether_brick',
    'minecraft:nether_brick_fence': 'minecraft:nether_brick_fence',
    'minecraft:nether_brick_stairs': 'minecraft:nether_brick_stairs',
    'minecraft:nether_wart': 'minecraft:nether_wart',
    'minecraft:nether_wart_block': 'minecraft:nether_wart_block',
    'minecraft:netherrack': 'minecraft:netherrack',
    'minecraft:noteblock': 'minecraft:noteblock',
    'minecraft:oak_button': 143,
    'minecraft:oak_stairs': 'minecraft:oak_stairs',
    'minecraft:observer': 'minecraft:observer',
    'minecraft:obsidian': 'minecraft:obsidian',
    'minecraft:orange_glazed_terracotta': 'minecraft:orange_glazed_terracotta',
    'minecraft:orange_shulker_box': 220,
    'minecraft:packed_ice': 'minecraft:packed_ice',
    'minecraft:pink_glazed_terracotta': 'minecraft:pink_glazed_terracotta',
    'minecraft:pink_shulker_box': 225,
    'minecraft:piston': 'minecraft:piston',
    'minecraft:piston_extension': 36,
    'minecraft:piston_head': 34,
    'minecraft:planks': 'minecraft:planks',
    'minecraft:portal': 'minecraft:portal',
    'minecraft:potatoes': 'minecraft:potatoes',
    'minecraft:powered_comparator': 'minecraft:powered_comparator',
    'minecraft:powered_repeater': 'minecraft:powered_repeater',
    'minecraft:prismarine': 'minecraft:prismarine',
    'minecraft:pumpkin': 'minecraft:pumpkin',
    'minecraft:pumpkin_stem': 'minecraft:pumpkin_stem',
    'minecraft:purple_glazed_terracotta': 'minecraft:purple_glazed_terracotta',
    'minecraft:purple_shulker_box': 229,
    'minecraft:purpur_block': 'minecraft:purpur_block',
    'minecraft:purpur_double_slab': 204,
    'minecraft:purpur_pillar': 202,
    'minecraft:purpur_slab': 205,
    'minecraft:purpur_stairs': 'minecraft:purpur_stairs',
    'minecraft:quartz_block': 'minecraft:quartz_block',
    'minecraft:quartz_ore': 'minecraft:quartz_ore',
    'minecraft:quartz_stairs': 'minecraft:quartz_stairs',
    'minecraft:rail': 'minecraft:rail',
    'minecraft:red_flower': 'minecraft:red_flower',
    'minecraft:red_glazed_terracotta': 'minecraft:red_glazed_terracotta',
    'minecraft:red_mushroom': 'minecraft:red_mushroom',
    'minecraft:red_mushroom_block': 'minecraft:red_mushroom_block',
    'minecraft:red_nether_brick': 'minecraft:red_nether_brick',
    'minecraft:red_sandstone': 'minecraft:red_sandstone',
    'minecraft:red_sandstone_stairs': 'minecraft:red_sandstone_stairs',
    'minecraft:red_shulker_box': 233,
    'minecraft:redstone_block': 'minecraft:redstone_block',
    'minecraft:redstone_lamp': 'minecraft:redstone_lamp',
    'minecraft:redstone_ore': 'minecraft:redstone_ore',
    'minecraft:redstone_torch': 'minecraft:redstone_torch',
    'minecraft:redstone_wire': 'minecraft:redstone_wire',
    'minecraft:reeds': 'minecraft:reeds',
    'minecraft:repeating_command_block': 'minecraft:repeating_command_block',
    'minecraft:sand': 'minecraft:sand',
    'minecraft:sandstone': 'minecraft:sandstone',
    'minecraft:sandstone_stairs': 'minecraft:sandstone_stairs',
    'minecraft:sapling': 'minecraft:sapling',
    'minecraft:sea_lantern': 169,
    'minecraft:silver_glazed_terracotta': 'minecraft:silver_glazed_terracotta',
    'minecraft:silver_shulker_box': 227,
    'minecraft:skull': 'minecraft:skull',
    'minecraft:slime': 'minecraft:slime',
    'minecraft:snow': 'minecraft:snow',
    'minecraft:snow_layer': 'minecraft:snow_layer',
    'minecraft:soul_sand': 'minecraft:soul_sand',
    'minecraft:sponge': 'minecraft:sponge',
    'minecraft:spruce_door': 'minecraft:spruce_door',
    'minecraft:spruce_fence': 188,
    'minecraft:spruce_fence_gate': 'minecraft:spruce_fence_gate',
    'minecraft:spruce_stairs': 'minecraft:spruce_stairs',
    'minecraft:stained_glass': 'minecraft:stained_glass',
    'minecraft:stained_glass_pane': 'minecraft:stained_glass_pane',
    'minecraft:stained_hardened_clay': 'minecraft:stained_hardened_clay',
    'minecraft:standing_banner': 'minecraft:standing_banner',
    'minecraft:standing_sign': 'minecraft:standing_sign',
    'minecraft:sticky_piston': 'minecraft:sticky_piston',
    'minecraft:stone': 'minecraft:stone',
    'minecraft:stone_brick_stairs': 'minecraft:stone_brick_stairs',
    'minecraft:stone_button': 'minecraft:stone_button',
    'minecraft:stone_pressure_plate': 'minecraft:stone_pressure_plate',
    'minecraft:stone_slab': 'minecraft:stone_slab',
    'minecraft:stone_slab2': 'minecraft:stone_slab2',
    'minecraft:stone_stairs': 'minecraft:stone_stairs',
    'minecraft:stonebrick': 'minecraft:stonebrick',
    'minecraft:structure_block': 'minecraft:structure_block',
    'minecraft:structure_void': 'minecraft:structure_void',
    'minecraft:tallgrass': 'minecraft:tallgrass',
    'minecraft:tnt': 'minecraft:tnt',
    'minecraft:torch': 'minecraft:torch',
    'minecraft:trapdoor': 'minecraft:trapdoor',
    'minecraft:trapped_chest': 'minecraft:trapped_chest',
    'minecraft:tripwire': 132,
    'minecraft:tripwire_hook': 'minecraft:tripwire_hook',
    'minecraft:unlit_redstone_torch': 'minecraft:unlit_redstone_torch',
    'minecraft:unpowered_comparator': 'minecraft:unpowered_comparator',
    'minecraft:unpowered_repeater': 'minecraft:unpowered_repeater',
    'minecraft:vine': 'minecraft:vine',
    'minecraft:wall_banner': 'minecraft:wall_banner',
    'minecraft:wall_sign': 'minecraft:wall_sign',
    'minecraft:water': 'minecraft:water',
    'minecraft:waterlily': 'minecraft:waterlily',
    'minecraft:web': 'minecraft:web',
    'minecraft:wheat': 'minecraft:wheat',
    'minecraft:white_glazed_terracotta': 'minecraft:white_glazed_terracotta',
    'minecraft:white_shulker_boxsponge': 219,
    'minecraft:wooden_door': 'minecraft:wooden_door',
    'minecraft:wooden_pressure_plate': 'minecraft:wooden_pressure_plate',
    'minecraft:wooden_slab': 'minecraft:wooden_slab',
    'minecraft:wool': 'minecraft:wool',
    'minecraft:yellow_flower': 'minecraft:yellow_flower',
    'minecraft:yellow_glazed_terracotta': 'minecraft:yellow_glazed_terracotta',
    'minecraft:yellow_shulker_box': 223
}
