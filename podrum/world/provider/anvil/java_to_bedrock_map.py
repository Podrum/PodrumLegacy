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

java_to_bedrock_map: dict = ################################################################################
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

name_to_id_map: dict = {
    "minecraft:air 0": "minecraft:air 0",
    "minecraft:stone 0": "minecraft:stone 0",
    "minecraft:stone 1": "minecraft:stone 1",
    "minecraft:stone 2": "minecraft:stone 2",
    "minecraft:stone 3": "minecraft:stone 3",
    "minecraft:stone 4": "minecraft:stone 4",
    "minecraft:stone 5": "minecraft:stone 5",
    "minecraft:stone 6": "minecraft:stone 6",
    "minecraft:grass 0": "minecraft:grass 0",
    "minecraft:dirt": 3,
    "minecraft:cobblestone": 4,
    "minecraft:planks": 5,
    "minecraft:sapling": 6,
    "minecraft:bedrock": 7,
    "minecraft:flowing_water": 8,
    "minecraft:water": 9,
    "minecraft:flowing_lava": 10,
    "minecraft:lava": 11,
    "minecraft:sand": 12,
    "minecraft:gravel": 13,
    "minecraft:gold_ore": 14,
    "minecraft:iron_ore": 15,
    "minecraft:coal_ore": 16,
    "minecraft:log": 17,
    "minecraft:leaves": 18,
    "minecraft:sponge": 19,
    "minecraft:glass": 20,
    "minecraft:lapis_ore": 21,
    "minecraft:lapis_block": 22,
    "minecraft:dispenser": 23,
    "minecraft:sandstone": 24,
    "minecraft:noteblock": 25,
    "minecraft:bed": 26,
    "minecraft:golden_rail": 27,
    "minecraft:detector_rail": 28,
    "minecraft:sticky_piston": 29,
    "minecraft:web": 30,
    "minecraft:tallgrass": 31,
    "minecraft:deadbush": 32,
    "minecraft:piston": 33,
    "minecraft:piston_head": 34,
    "minecraft:wool": 35,
    "minecraft:piston_extension": 36,
    "minecraft:yellow_flower": 37,
    "minecraft:red_flower": 38,
    "minecraft:brown_mushroom": 39,
    "minecraft:red_mushroom": 40,
    "minecraft:gold_block": 41,
    "minecraft:iron_block": 42,
    "minecraft:double_stone_slab": 43,
    "minecraft:stone_slab": 44,
    "minecraft:brick_block": 45,
    "minecraft:tnt": 46,
    "minecraft:bookshelf": 47,
    "minecraft:mossy_cobblestone": 48,
    "minecraft:obsidian": 49,
    "minecraft:torch": 50,
    "minecraft:fire": 51,
    "minecraft:mob_spawner": 52,
    "minecraft:oak_stairs": 53,
    "minecraft:chest": 54,
    "minecraft:redstone_wire": 55,
    "minecraft:diamond_ore": 56,
    "minecraft:diamond_block": 57,
    "minecraft:crafting_table": 58,
    "minecraft:wheat": 59,
    "minecraft:farmland": 60,
    "minecraft:furnace": 61,
    "minecraft:lit_furnace": 62,
    "minecraft:standing_sign": 63,
    "minecraft:wooden_door": 64,
    "minecraft:ladder": 65,
    "minecraft:rail": 66,
    "minecraft:stone_stairs": 67,
    "minecraft:wall_sign": 68,
    "minecraft:lever": 69,
    "minecraft:stone_pressure_plate": 70,
    "minecraft:iron_door": 71,
    "minecraft:wooden_pressure_plate": 72,
    "minecraft:redstone_ore": 73,
    "minecraft:lit_redstone_ore": 74,
    "minecraft:unlit_redstone_torch": 75,
    "minecraft:redstone_torch": 76,
    "minecraft:stone_button": 77,
    "minecraft:snow_layer": 78,
    "minecraft:ice": 79,
    "minecraft:snow": 80,
    "minecraft:cactus": 81,
    "minecraft:clay": 82,
    "minecraft:reeds": 83,
    "minecraft:jukebox": 84,
    "minecraft:fence": 85,
    "minecraft:pumpkin": 86,
    "minecraft:netherrack": 87,
    "minecraft:soul_sand": 88,
    "minecraft:glowstone": 89,
    "minecraft:portal": 90,
    "minecraft:lit_pumpkin": 91,
    "minecraft:cake": 92,
    "minecraft:unpowered_repeater": 93,
    "minecraft:powered_repeater": 94,
    "minecraft:stained_glass": 95,
    "minecraft:trapdoor": 96,
    "minecraft:monster_egg": 97,
    "minecraft:stonebrick": 98,
    "minecraft:brown_mushroom_block": 99,
    "minecraft:red_mushroom_block": 100,
    "minecraft:iron_bars": 101,
    "minecraft:glass_pane": 102,
    "minecraft:melon_block": 103,
    "minecraft:pumpkin_stem": 104,
    "minecraft:melon_stem": 105,
    "minecraft:vine": 106,
    "minecraft:fence_gate": 107,
    "minecraft:brick_stairs": 108,
    "minecraft:stone_brick_stairs": 109,
    "minecraft:mycelium": 110,
    "minecraft:waterlily": 111,
    "minecraft:nether_brick": 112,
    "minecraft:nether_brick_fence": 113,
    "minecraft:nether_brick_stairs": 114,
    "minecraft:nether_wart": 115,
    "minecraft:enchanting_table": 116,
    "minecraft:brewing_stand": 117,
    "minecraft:cauldron": 118,
    "minecraft:end_portal": 119,
    "minecraft:end_portal_frame": 120,
    "minecraft:end_stone": 121,
    "minecraft:dragon_egg": 122,
    "minecraft:redstone_lamp": 123,
    "minecraft:lit_redstone_lamp": 124,
    "minecraft:double_wooden_slab": 125,
    "minecraft:wooden_slab": 126,
    "minecraft:cocoa": 127,
    "minecraft:sandstone_stairs": 128,
    "minecraft:emerald_ore": 129,
    "minecraft:ender_chest": 130,
    "minecraft:tripwire_hook": 131,
    "minecraft:tripwire": 132,
    "minecraft:emerald_block": 133,
    "minecraft:spruce_stairs": 134,
    "minecraft:birch_stairs": 135,
    "minecraft:jungle_stairs": 136,
    "minecraft:command_block": 137,
    "minecraft:beacon": 138,
    "minecraft:cobblestone_wall": 139,
    "minecraft:flower_pot": 140,
    "minecraft:carrots": 141,
    "minecraft:potatoes": 142,
    "minecraft:oak_button": 143,
    "minecraft:skull": 144,
    "minecraft:anvil": 145,
    "minecraft:trapped_chest": 146,
    "minecraft:light_weighted_pressure_plate": 147,
    "minecraft:heavy_weighted_pressure_plate": 148,
    "minecraft:unpowered_comparator": 149,
    "minecraft:powered_comparator": 150,
    "minecraft:daylight_detector": 151,
    "minecraft:redstone_block": 152,
    "minecraft:quartz_ore": 153,
    "minecraft:hopper": 154,
    "minecraft:quartz_block": 155,
    "minecraft:quartz_stairs": 156,
    "minecraft:activator_rail": 157,
    "minecraft:dropper": 158,
    "minecraft:stained_hardened_clay": 159,
    "minecraft:stained_glass_pane": 160,
    "minecraft:leaves2": 161,
    "minecraft:log2": 162,
    "minecraft:acacia_stairs": 163,
    "minecraft:dark_oak_stairs": 164,
    "minecraft:slime": 165,
    "minecraft:barrier": 166,
    "minecraft:iron_trapdoor": 167,
    "minecraft:prismarine": 168,
    "minecraft:sea_lantern": 169,
    "minecraft:hay_block": 170,
    "minecraft:carpet": 171,
    "minecraft:hardened_clay": 172,
    "minecraft:coal_block": 173,
    "minecraft:packed_ice": 174,
    "minecraft:double_plant": 175,
    "minecraft:standing_banner": 176,
    "minecraft:wall_banner": 177,
    "minecraft:daylight_detector_inverted": 178,
    "minecraft:red_sandstone": 179,
    "minecraft:red_sandstone_stairs": 180,
    "minecraft:double_stone_slab2": 181,
    "minecraft:stone_slab2": 182,
    "minecraft:spruce_fence_gate": 183,
    "minecraft:birch_fence_gate": 184,
    "minecraft:jungle_fence_gate": 185,
    "minecraft:dark_oak_fence_gate": 186,
    "minecraft:acacia_fence_gate": 187,
    "minecraft:spruce_fence": 188,
    "minecraft:birch_fence": 189,
    "minecraft:jungle_fence": 190,
    "minecraft:dark_oak_fence": 191,
    "minecraft:acacia_fence": 192,
    "minecraft:spruce_door": 193,
    "minecraft:birch_door": 194,
    "minecraft:jungle_door": 195,
    "minecraft:acacia_door": 196,
    "minecraft:dark_oak_door": 197,
    "minecraft:end_rod": 198,
    "minecraft:chorus_plant": 199,
    "minecraft:chorus_flower": 200,
    "minecraft:purpur_block": 201,
    "minecraft:purpur_pillar": 202,
    "minecraft:purpur_stairs": 203,
    "minecraft:purpur_double_slab": 204,
    "minecraft:purpur_slab": 205,
    "minecraft:end_bricks": 206,
    "minecraft:beetroots": 207,
    "minecraft:grass_path": 208,
    "minecraft:end_gateway": 209,
    "minecraft:repeating_command_block": 210,
    "minecraft:chain_command_block": 211,
    "minecraft:frosted_ice": 212,
    "minecraft:magma": 213,
    "minecraft:nether_wart_block": 214,
    "minecraft:red_nether_brick": 215,
    "minecraft:bone_block": 216,
    "minecraft:structure_void": 217,
    "minecraft:observer": 218,
    "minecraft:white_shulker_boxsponge": 219,
    "minecraft:orange_shulker_box": 220,
    "minecraft:magenta_shulker_box": 221,
    "minecraft:light_blue_shulker_box": 222,
    "minecraft:yellow_shulker_box": 223,
    "minecraft:lime_shulker_box": 224,
    "minecraft:pink_shulker_box": 225,
    "minecraft:gray_shulker_box": 226,
    "minecraft:silver_shulker_box": 227,
    "minecraft:cyan_shulker_box": 228,
    "minecraft:purple_shulker_box": 229,
    "minecraft:blue_shulker_box": 230,
    "minecraft:brown_shulker_box": 231,
    "minecraft:green_shulker_box": 232,
    "minecraft:red_shulker_box": 233,
    "minecraft:black_shulker_box": 234,
    "minecraft:white_glazed_terracotta": 235,
    "minecraft:orange_glazed_terracotta": 236,
    "minecraft:magenta_glazed_terracotta": 237,
    "minecraft:light_blue_glazed_terracotta": 238,
    "minecraft:yellow_glazed_terracotta": 239,
    "minecraft:lime_glazed_terracotta": 240,
    "minecraft:pink_glazed_terracotta": 241,
    "minecraft:gray_glazed_terracotta": 242,
    "minecraft:silver_glazed_terracotta": 243,
    "minecraft:cyan_glazed_terracotta": 244,
    "minecraft:purple_glazed_terracotta": 245,
    "minecraft:blue_glazed_terracotta": 246,
    "minecraft:brown_glazed_terracotta": 247,
    "minecraft:green_glazed_terracotta": 248,
    "minecraft:red_glazed_terracotta": 249,
    "minecraft:black_glazed_terracotta": 250,
    "minecraft:concrete": 251,
    "minecraft:concrete_powder": 252,

    
    "minecraft:structure_block": 255
}
