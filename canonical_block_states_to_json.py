r"""
  ____           _
 |  _ \ ___   __| |_ __ _   _ _ __ ___
 | |_) / _ \ / _` | '__| | | | '_ ` _ \
 |  __/ (_) | (_| | |  | |_| | | | | | |
 |_|   \___/ \__,_|_|   \__,_|_| |_| |_|

 Copyright 2021 Podrum Team.

 This file is licensed under the GPL v2.0 license.
 The license file is located in the root directory
 of the source code. If not you may not use this file.
"""

from nbt_utils.utils.nbt_net_le_binary_stream import nbt_net_le_binary_stream
import json

with open("canonical_block_states.nbt", "rb") as f:
    stream = nbt_net_le_binary_stream(f.read())
    f.close()

block_states: list = []

while not stream.feos():
    root_tag = stream.read_root_tag()

    name: str = root_tag.get_tag("name").value
    states: list = root_tag.get_tag("states").value
    version: int = root_tag.get_tag("version").value

    parsed_states: list = [
        {
            "name": state.name,
            "type": state.id,
            "value": state.value
        } for state in states
    ]

    block_states.append(
        {
            "name": name,
            "states": parsed_states,
            "version": version
        }
    )

with open("canonical_block_states.json", "w") as f:
    json.dump(block_states, f, indent=4)
    f.close()
