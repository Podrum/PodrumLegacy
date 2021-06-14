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

from nbt_utils.utils.nbt_net_le_binary_stream import nbt_net_le_binary_stream
import json

file: object = open("canonical_block_states.nbt", "rb")
stream: object = nbt_net_le_binary_stream(file.read())

block_states: list = []

while not stream.feos():
    root_tag: object = stream.read_root_tag()
    name: str = root_tag.get_tag("name").value
    states: list = root_tag.get_tag("states").value
    version: int = root_tag.get_tag("version").value
    parsed_states: dict = {}
    for state in states:
        parsed_states[state.name] = state.value
    block_states.append({
        "name": name,
        "states": parsed_states,
        "version": version
    })

json.dump(block_states, open("canonical_block_states.json", "w"), indent = 4)
