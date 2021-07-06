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

block_id_map: dict = {
    "minecraft:air": 0,
    "minecraft:stone": 1,
    "minecraft:grass": 2,
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
    "minecraft:pistonArmCollision": 34,
    "minecraft:wool": 35,
    "minecraft:element_0": 36,
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
    "minecraft:invisibleBedrock": 95,
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
    "minecraft:dropper": 125,
    "minecraft:activator_rail": 126,
    "minecraft:cocoa": 127,
    "minecraft:sandstone_stairs": 128,
    "minecraft:emerald_ore": 129,
    "minecraft:ender_chest": 130,
    "minecraft:tripwire_hook": 131,
    "minecraft:tripWire": 132,
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
    "minecraft:wooden_button": 143,
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
    "minecraft:double_wooden_slab": 157,
    "minecraft:wooden_slab": 158,
    "minecraft:stained_hardened_clay": 159,
    "minecraft:stained_glass_pane": 160,
    "minecraft:leaves2": 161,
    "minecraft:log2": 162,
    "minecraft:acacia_stairs": 163,
    "minecraft:dark_oak_stairs": 164,
    "minecraft:slime": 165,
    "minecraft:iron_trapdoor": 167,
    "minecraft:prismarine": 168,
    "minecraft:seaLantern": 169,
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
    "minecraft:repeating_command_block": 188,
    "minecraft:chain_command_block": 189,
    "minecraft:hard_glass_pane": 190,
    "minecraft:hard_stained_glass_pane": 191,
    "minecraft:chemical_heat": 192,
    "minecraft:spruce_door": 193,
    "minecraft:birch_door": 194,
    "minecraft:jungle_door": 195,
    "minecraft:acacia_door": 196,
    "minecraft:dark_oak_door": 197,
    "minecraft:grass_path": 198,
    "minecraft:frame": 199,
    "minecraft:chorus_flower": 200,
    "minecraft:purpur_block": 201,
    "minecraft:colored_torch_rg": 202,
    "minecraft:purpur_stairs": 203,
    "minecraft:colored_torch_bp": 204,
    "minecraft:undyed_shulker_box": 205,
    "minecraft:end_bricks": 206,
    "minecraft:frosted_ice": 207,
    "minecraft:end_rod": 208,
    "minecraft:end_gateway": 209,
    "minecraft:allow": 210,
    "minecraft:deny": 211,
    "minecraft:border_block": 212,
    "minecraft:magma": 213,
    "minecraft:nether_wart_block": 214,
    "minecraft:red_nether_brick": 215,
    "minecraft:bone_block": 216,
    "minecraft:structure_void": 217,
    "minecraft:shulker_box": 218,
    "minecraft:purple_glazed_terracotta": 219,
    "minecraft:white_glazed_terracotta": 220,
    "minecraft:orange_glazed_terracotta": 221,
    "minecraft:magenta_glazed_terracotta": 222,
    "minecraft:light_blue_glazed_terracotta": 223,
    "minecraft:yellow_glazed_terracotta": 224,
    "minecraft:lime_glazed_terracotta": 225,
    "minecraft:pink_glazed_terracotta": 226,
    "minecraft:gray_glazed_terracotta": 227,
    "minecraft:silver_glazed_terracotta": 228,
    "minecraft:cyan_glazed_terracotta": 229,
    "minecraft:blue_glazed_terracotta": 231,
    "minecraft:brown_glazed_terracotta": 232,
    "minecraft:green_glazed_terracotta": 233,
    "minecraft:red_glazed_terracotta": 234,
    "minecraft:black_glazed_terracotta": 235,
    "minecraft:concrete": 236,
    "minecraft:concretePowder": 237,
    "minecraft:chemistry_table": 238,
    "minecraft:underwater_torch": 239,
    "minecraft:chorus_plant": 240,
    "minecraft:stained_glass": 241,
    "minecraft:camera": 242,
    "minecraft:podzol": 243,
    "minecraft:beetroot": 244,
    "minecraft:stonecutter": 245,
    "minecraft:glowingobsidian": 246,
    "minecraft:netherreactor": 247,
    "minecraft:info_update": 248,
    "minecraft:info_update2": 249,
    "minecraft:movingBlock": 250,
    "minecraft:observer": 251,
    "minecraft:structure_block": 252,
    "minecraft:hard_glass": 253,
    "minecraft:hard_stained_glass": 254,
    "minecraft:reserved6": 255,
    "minecraft:prismarine_stairs": 257,
    "minecraft:dark_prismarine_stairs": 258,
    "minecraft:prismarine_bricks_stairs": 259,
    "minecraft:stripped_spruce_log": 260,
    "minecraft:stripped_birch_log": 261,
    "minecraft:stripped_jungle_log": 262,
    "minecraft:stripped_acacia_log": 263,
    "minecraft:stripped_dark_oak_log": 264,
    "minecraft:stripped_oak_log": 265,
    "minecraft:blue_ice": 266,
    "minecraft:element_1": 267,
    "minecraft:element_2": 268,
    "minecraft:element_3": 269,
    "minecraft:element_4": 270,
    "minecraft:element_5": 271,
    "minecraft:element_6": 272,
    "minecraft:element_7": 273,
    "minecraft:element_8": 274,
    "minecraft:element_9": 275,
    "minecraft:element_10": 276,
    "minecraft:element_11": 277,
    "minecraft:element_12": 278,
    "minecraft:element_13": 279,
    "minecraft:element_14": 280,
    "minecraft:element_15": 281,
    "minecraft:element_16": 282,
    "minecraft:element_17": 283,
    "minecraft:element_18": 284,
    "minecraft:element_19": 285,
    "minecraft:element_20": 286,
    "minecraft:element_21": 287,
    "minecraft:element_22": 288,
    "minecraft:element_23": 289,
    "minecraft:element_24": 290,
    "minecraft:element_25": 291,
    "minecraft:element_26": 292,
    "minecraft:element_27": 293,
    "minecraft:element_28": 294,
    "minecraft:element_29": 295,
    "minecraft:element_30": 296,
    "minecraft:element_31": 297,
    "minecraft:element_32": 298,
    "minecraft:element_33": 299,
    "minecraft:element_34": 300,
    "minecraft:element_35": 301,
    "minecraft:element_36": 302,
    "minecraft:element_37": 303,
    "minecraft:element_38": 304,
    "minecraft:element_39": 305,
    "minecraft:element_40": 306,
    "minecraft:element_41": 307,
    "minecraft:element_42": 308,
    "minecraft:element_43": 309,
    "minecraft:element_44": 310,
    "minecraft:element_45": 311,
    "minecraft:element_46": 312,
    "minecraft:element_47": 313,
    "minecraft:element_48": 314,
    "minecraft:element_49": 315,
    "minecraft:element_50": 316,
    "minecraft:element_51": 317,
    "minecraft:element_52": 318,
    "minecraft:element_53": 319,
    "minecraft:element_54": 320,
    "minecraft:element_55": 321,
    "minecraft:element_56": 322,
    "minecraft:element_57": 323,
    "minecraft:element_58": 324,
    "minecraft:element_59": 325,
    "minecraft:element_60": 326,
    "minecraft:element_61": 327,
    "minecraft:element_62": 328,
    "minecraft:element_63": 329,
    "minecraft:element_64": 330,
    "minecraft:element_65": 331,
    "minecraft:element_66": 332,
    "minecraft:element_67": 333,
    "minecraft:element_68": 334,
    "minecraft:element_69": 335,
    "minecraft:element_70": 336,
    "minecraft:element_71": 337,
    "minecraft:element_72": 338,
    "minecraft:element_73": 339,
    "minecraft:element_74": 340,
    "minecraft:element_75": 341,
    "minecraft:element_76": 342,
    "minecraft:element_77": 343,
    "minecraft:element_78": 344,
    "minecraft:element_79": 345,
    "minecraft:element_80": 346,
    "minecraft:element_81": 347,
    "minecraft:element_82": 348,
    "minecraft:element_83": 349,
    "minecraft:element_84": 350,
    "minecraft:element_85": 351,
    "minecraft:element_86": 352,
    "minecraft:element_87": 353,
    "minecraft:element_88": 354,
    "minecraft:element_89": 355,
    "minecraft:element_90": 356,
    "minecraft:element_91": 357,
    "minecraft:element_92": 358,
    "minecraft:element_93": 359,
    "minecraft:element_94": 360,
    "minecraft:element_95": 361,
    "minecraft:element_96": 362,
    "minecraft:element_97": 363,
    "minecraft:element_98": 364,
    "minecraft:element_99": 365,
    "minecraft:element_100": 366,
    "minecraft:element_101": 367,
    "minecraft:element_102": 368,
    "minecraft:element_103": 369,
    "minecraft:element_104": 370,
    "minecraft:element_105": 371,
    "minecraft:element_106": 372,
    "minecraft:element_107": 373,
    "minecraft:element_108": 374,
    "minecraft:element_109": 375,
    "minecraft:element_110": 376,
    "minecraft:element_111": 377,
    "minecraft:element_112": 378,
    "minecraft:element_113": 379,
    "minecraft:element_114": 380,
    "minecraft:element_115": 381,
    "minecraft:element_116": 382,
    "minecraft:element_117": 383,
    "minecraft:element_118": 384,
    "minecraft:seagrass": 385,
    "minecraft:coral": 386,
    "minecraft:coral_block": 387,
    "minecraft:coral_fan": 388,
    "minecraft:coral_fan_dead": 389,
    "minecraft:coral_fan_hang": 390,
    "minecraft:coral_fan_hang2": 391,
    "minecraft:coral_fan_hang3": 392,
    "minecraft:kelp": 393,
    "minecraft:dried_kelp_block": 394,
    "minecraft:acacia_button": 395,
    "minecraft:birch_button": 396,
    "minecraft:dark_oak_button": 397,
    "minecraft:jungle_button": 398,
    "minecraft:spruce_button": 399,
    "minecraft:acacia_trapdoor": 400,
    "minecraft:birch_trapdoor": 401,
    "minecraft:dark_oak_trapdoor": 402,
    "minecraft:jungle_trapdoor": 403,
    "minecraft:spruce_trapdoor": 404,
    "minecraft:acacia_pressure_plate": 405,
    "minecraft:birch_pressure_plate": 406,
    "minecraft:dark_oak_pressure_plate": 407,
    "minecraft:jungle_pressure_plate": 408,
    "minecraft:spruce_pressure_plate": 409,
    "minecraft:carved_pumpkin": 410,
    "minecraft:sea_pickle": 411,
    "minecraft:conduit": 412,
    "minecraft:turtle_egg": 414,
    "minecraft:bubble_column": 415,
    "minecraft:barrier": 416,
    "minecraft:stone_slab3": 417,
    "minecraft:bamboo": 418,
    "minecraft:bamboo_sapling": 419,
    "minecraft:scaffolding": 420,
    "minecraft:stone_slab4": 421,
    "minecraft:double_stone_slab3": 422,
    "minecraft:double_stone_slab4": 423,
    "minecraft:granite_stairs": 424,
    "minecraft:diorite_stairs": 425,
    "minecraft:andesite_stairs": 426,
    "minecraft:polished_granite_stairs": 427,
    "minecraft:polished_diorite_stairs": 428,
    "minecraft:polished_andesite_stairs": 429,
    "minecraft:mossy_stone_brick_stairs": 430,
    "minecraft:smooth_red_sandstone_stairs": 431,
    "minecraft:smooth_sandstone_stairs": 432,
    "minecraft:end_brick_stairs": 433,
    "minecraft:mossy_cobblestone_stairs": 434,
    "minecraft:normal_stone_stairs": 435,
    "minecraft:spruce_standing_sign": 436,
    "minecraft:spruce_wall_sign": 437,
    "minecraft:smooth_stone": 438,
    "minecraft:red_nether_brick_stairs": 439,
    "minecraft:smooth_quartz_stairs": 440,
    "minecraft:birch_standing_sign": 441,
    "minecraft:birch_wall_sign": 442,
    "minecraft:jungle_standing_sign": 443,
    "minecraft:jungle_wall_sign": 444,
    "minecraft:acacia_standing_sign": 445,
    "minecraft:acacia_wall_sign": 446,
    "minecraft:darkoak_standing_sign": 447,
    "minecraft:darkoak_wall_sign": 448,
    "minecraft:lectern": 449,
    "minecraft:grindstone": 450,
    "minecraft:blast_furnace": 451,
    "minecraft:stonecutter_block": 452,
    "minecraft:smoker": 453,
    "minecraft:lit_smoker": 454,
    "minecraft:cartography_table": 455,
    "minecraft:fletching_table": 456,
    "minecraft:smithing_table": 457,
    "minecraft:barrel": 458,
    "minecraft:loom": 459,
    "minecraft:bell": 461,
    "minecraft:sweet_berry_bush": 462,
    "minecraft:lantern": 463,
    "minecraft:campfire": 464,
    "minecraft:lava_cauldron": 465,
    "minecraft:jigsaw": 466,
    "minecraft:wood": 467,
    "minecraft:composter": 468,
    "minecraft:lit_blast_furnace": 469,
    "minecraft:light_block": 470,
    "minecraft:wither_rose": 471,
    "minecraft:stickyPistonArmCollision": 472,
    "minecraft:bee_nest": 473,
    "minecraft:beehive": 474,
    "minecraft:honey_block": 475,
    "minecraft:honeycomb_block": 476,
    "minecraft:lodestone": 477,
    "minecraft:crimson_roots": 478,
    "minecraft:warped_roots": 479,
    "minecraft:crimson_stem": 480,
    "minecraft:warped_stem": 481,
    "minecraft:warped_wart_block": 482,
    "minecraft:crimson_fungus": 483,
    "minecraft:warped_fungus": 484,
    "minecraft:shroomlight": 485,
    "minecraft:weeping_vines": 486,
    "minecraft:crimson_nylium": 487,
    "minecraft:warped_nylium": 488,
    "minecraft:basalt": 489,
    "minecraft:polished_basalt": 490,
    "minecraft:soul_soil": 491,
    "minecraft:soul_fire": 492,
    "minecraft:nether_sprouts": 493,
    "minecraft:target": 494,
    "minecraft:stripped_crimson_stem": 495,
    "minecraft:stripped_warped_stem": 496,
    "minecraft:crimson_planks": 497,
    "minecraft:warped_planks": 498,
    "minecraft:crimson_door": 499,
    "minecraft:warped_door": 500,
    "minecraft:crimson_trapdoor": 501,
    "minecraft:warped_trapdoor": 502,
    "minecraft:crimson_standing_sign": 505,
    "minecraft:warped_standing_sign": 506,
    "minecraft:crimson_wall_sign": 507,
    "minecraft:warped_wall_sign": 508,
    "minecraft:crimson_stairs": 509,
    "minecraft:warped_stairs": 510,
    "minecraft:crimson_fence": 511,
    "minecraft:warped_fence": 512,
    "minecraft:crimson_fence_gate": 513,
    "minecraft:warped_fence_gate": 514,
    "minecraft:crimson_button": 515,
    "minecraft:warped_button": 516,
    "minecraft:crimson_pressure_plate": 517,
    "minecraft:warped_pressure_plate": 518,
    "minecraft:crimson_slab": 519,
    "minecraft:warped_slab": 520,
    "minecraft:crimson_double_slab": 521,
    "minecraft:warped_double_slab": 522,
    "minecraft:soul_torch": 523,
    "minecraft:soul_lantern": 524,
    "minecraft:netherite_block": 525,
    "minecraft:ancient_debris": 526,
    "minecraft:respawn_anchor": 527,
    "minecraft:blackstone": 528,
    "minecraft:polished_blackstone_bricks": 529,
    "minecraft:polished_blackstone_brick_stairs": 530,
    "minecraft:blackstone_stairs": 531,
    "minecraft:blackstone_wall": 532,
    "minecraft:polished_blackstone_brick_wall": 533,
    "minecraft:chiseled_polished_blackstone": 534,
    "minecraft:cracked_polished_blackstone_bricks": 535,
    "minecraft:gilded_blackstone": 536,
    "minecraft:blackstone_slab": 537,
    "minecraft:blackstone_double_slab": 538,
    "minecraft:polished_blackstone_brick_slab": 539,
    "minecraft:polished_blackstone_brick_double_slab": 540,
    "minecraft:chain": 541,
    "minecraft:twisting_vines": 542,
    "minecraft:nether_gold_ore": 543,
    "minecraft:crying_obsidian": 544,
    "minecraft:soul_campfire": 545,
    "minecraft:polished_blackstone": 546,
    "minecraft:polished_blackstone_stairs": 547,
    "minecraft:polished_blackstone_slab": 548,
    "minecraft:polished_blackstone_double_slab": 549,
    "minecraft:polished_blackstone_pressure_plate": 550,
    "minecraft:polished_blackstone_button": 551,
    "minecraft:polished_blackstone_wall": 552,
    "minecraft:warped_hyphae": 553,
    "minecraft:crimson_hyphae": 554,
    "minecraft:stripped_crimson_hyphae": 555,
    "minecraft:stripped_warped_hyphae": 556,
    "minecraft:chiseled_nether_bricks": 557,
    "minecraft:cracked_nether_bricks": 558,
    "minecraft:quartz_bricks": 559,
    "minecraft:deepslate": 633,
    "minecraft:deepslate_lapis_ore": 655,
    "minecraft:deepslate_iron_ore": 656,
    "minecraft:deepslate_gold_ore": 657,
    "minecraft:deepslate_redstone_ore": 658,
    "minecraft:lit_deepslate_redstone_ore": 659,
    "minecraft:deepslate_diamond_ore": 660,
    "minecraft:deepslate_emerald_ore": 662
}