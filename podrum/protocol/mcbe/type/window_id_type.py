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

class window_id_type:
    drop_contents: int = -100
    beacon: int = -24
    trading_output: int = -23
    trading_use_inputs: int = -22
    trading_input_2: int = -21
    trading_input_1: int = -20
    enchant_output: int = -17
    enchant_material: int = -16
    enchant_input: int = -15
    anvil_output: int = -13
    anvil_result: int = -12
    anvil_material: int = -11
    container_input: int = -10
    crafting_use_ingredient: int = -5
    crafting_result: int = -4
    crafting_remove_ingredient: int = -3
    crafting_add_ingredient: int = -2
    none: int = -1
    inventory: int = 0
    first: int = 1
    last: int = 100
    offhand: int = 119
    armor: int = 120
    creative: int = 121
    hotbar: int = 122
    fixed_inventory: int = 123
    ui: int = 124
