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

from binary_utils.binary_stream import binary_stream
from geometry.vector_2 import vector_2
from geometry.vector_3 import vector_3
from nbt_utils.utils.nbt_le_binary_stream import nbt_le_binary_stream
from nbt_utils.utils.nbt_net_le_binary_stream import nbt_net_le_binary_stream
from protocol.mcbe.type.gamerule_type import gamerule_type
from protocol.mcbe.type.metadata_dictionary_type import metadata_dictionary_type

class mcbe_binary_stream(binary_stream):
    def read_string(self) -> str:
        return self.read(self.read_var_int()).decode()
    
    def write_string(self, value: str) -> None:
        self.write_var_int(len(value))
        self.write(value.encode())
        
    def read_little_string(self) -> str:
        return self.read(self.read_int_le()).decode()
    
    def write_little_string(self, value: str) -> None:
        self.write_int_le(len(value))
        self.write(value.encode())
        
    def read_byte_array(self) -> bytes:
        return self.read(self.read_var_int())
    
    def write_byte_array(self, value: bytes) -> None:
        self.write_var_int(len(value))
        self.write(value)
        
    def read_signed_byte_array(self) -> bytes:
        return self.read(self.read_signed_var_int())
    
    def write_signed_byte_array(self, value: bytes) -> None:
        self.write_signed_var_int(len(value))
        self.write(value)
        
    def read_short_array(self) -> bytes:
        return self.read(self.read_short_le())
    
    def write_short_array(self, value: bytes) -> None:
        self.write_short_le(len(value))
        self.write(value)
        
    def read_behavior_pack_infos(self) -> list:
        behavior_pack_infos: list = []
        length: int = self.read_short_le()
        for i in range(0, length):
            behavior_pack_infos.append({
                "uuid": self.read_string(),
                "version": self.read_string(),
                "size": self.read_unsigned_long_le(),
                "content_key": self.read_string(),
                "sub_pack_name": self.read_string(),
                "content_identity": self.read_string(),
                "has_scripts": self.read_bool()
            })
        return behavior_pack_infos
            
    def write_behavior_pack_infos(self, value: list) -> None:
        self.write_short_le(len(value))
        for behavior_pack_info in value:
            self.write_string(behavior_pack_info["uuid"])
            self.write_string(behavior_pack_info["version"])
            self.write_unsigned_long_le(behavior_pack_info["size"])
            self.write_string(behavior_pack_info["content_key"])
            self.write_string(behavior_pack_info["sub_pack_name"])
            self.write_string(behavior_pack_info["content_identity"])
            self.write_bool(behavior_pack_info["has_scripts"])
            
    def read_texture_pack_infos(self) -> list:
        texture_pack_infos: list = []
        length: int = self.read_short_le()
        for i in range(0, length):
            texture_pack_infos.append({
                "uuid": self.read_string(),
                "version": self.read_string(),
                "size": self.read_unsigned_long_le(),
                "content_key": self.read_string(),
                "sub_pack_name": self.read_string(),
                "content_identity": self.read_string(),
                "has_scripts": self.read_bool(),
                "rtx_enabled": self.read_bool()
            })
        return resource_pack_infos
            
    def write_texture_pack_infos(self, value: list) -> None:
        self.write_short_le(len(value))
        for texture_pack_info in value:
            self.write_string(texture_pack_info["uuid"])
            self.write_string(texture_pack_info["version"])
            self.write_unsigned_long_le(texture_pack_info["size"])
            self.write_string(texture_pack_info["content_key"])
            self.write_string(texture_pack_info["sub_pack_name"])
            self.write_string(texture_pack_info["content_identity"])
            self.write_bool(texture_pack_info["has_scripts"])
            self.write_bool(texture_pack_info["rtx_enabled"])
            
    def read_resource_pack_id_versions(self) -> list:
        resource_pack_id_versions: list = []
        length: int = self.read_var_int()
        for i in range(0, length):
            resource_pack_id_versions.append({
                "uuid": self.read_string(),
                "version": self.read_string(),
                "name": self.read_string()
            })
        return resource_pack_id_versions
        
    def write_resource_pack_id_versions(self, value: list) -> None:
        self.write_var_int(len(value))
        for resource_pack_id_version in value:
            self.write_string(resource_pack_id_version["uuid"])
            self.write_string(resource_pack_id_version["version"])
            self.write_string(resource_pack_id_version["name"])
            
    def read_resource_pack_ids(self) -> list:
        resource_pack_ids: list = []
        length: int = self.read_short_le()
        for i in range(0, length):
            resource_pack_ids.append(self.read_string())
        return resource_pack_ids
        
    def write_resource_pack_ids(self, value: list) -> None:
        self.write_short_le(len(value))
        for resource_pack_id in value:
            self.write_string(resource_pack_id)
            
    def read_experiment(self) -> dict:
        return {
            "name": self.read_string(),
            "enabled": self.read_bool()
        }
        
    def write_experiment(self, value: dict) -> None:
        self.write_string(value["name"])
        self.write_bool(value["enabled"])
        
    def read_experiments(self) -> list:
        experiments: list = []
        length: int = self.read_int_le()
        for i in range(0, length):
            experiments.append(self.read_experiment())
        return experiments
        
    def write_experiments(self, value: list) -> None:
        self.write_int_le(len(value))
        for experiment in value:
            self.write_experiment(experiment)
            
    def read_gamemode(self) -> int:
        return self.read_signed_var_int()
        
    def write_gamemode(self, value: int) -> None:
        self.write_signed_var_int(value)
        
    def read_game_rule(self) -> dict:
        game_rule: dict = {
            "name": self.read_string(),
            "editable": self.read_bool(),
            "type": self.read_var_int()
        }
        if game_rule["type"] == gamerule_type.type_bool:
            game_rule["value"]: bool = self.read_bool()
        elif game_rule["type"] == gamerule_type.type_int:
            game_rule["value"]: int = self.read_signed_var_int()
        elif game_rule["type"] == gamerule_type.type_float:
            game_rule["value"]: float = self.read_float_le()
        return game_rule
        
    def write_game_rule(self, value: dict) -> None:
        self.write_string(value["name"])
        self.write_bool(value["editable"])
        self.write_var_int(value["type"])
        if value["type"] == gamerule_type.type_bool:
            self.write_bool(value["value"])
        elif value["type"] == gamerule_type.type_int:
            self.write_signed_var_int(value["value"])
        elif value["type"] == gamerule_type.type_float:
            self.write_float_le(value["value"])
            
    def read_game_rules(self) -> list:
        game_rules: list = []
        length: int = self.read_var_int()
        for i in range(0, length):
            game_rules.append(self.read_game_rule())
        return game_rules
        
    def write_game_rules(self, value: list) -> None:
        self.write_var_int(len(value))
        for game_rule in value:
            self.write_game_rule(game_rule)
            
    def read_blob(self) -> dict:
        return {
            "hash": self.read_unsigned_long_le(),
            "payload": self.read_byte_array()
        }
        
    def write_blob(self, value: dict) -> None:
        self.write_unsigned_long_le(value["hash"])
        self.write_byte_array(value["payload"])

    def read_item_states(self) -> list:
        item_states: list = []
        length: int = self.read_var_int()
        for i in range(0, length):
            item_states.append({
                "name": self.read_string(),
                "runtime_id": self.read_short_le(),
                "component_based": self.read_bool()
            })
        return item_states

    def write_item_states(self, value: list) -> None:
        self.write_var_int(len(value))
        for item_state in value:
            self.write_string(item_state["name"])
            self.write_short_le(item_state["runtime_id"])
            self.write_bool(item_state["component_based"])

    def read_net_le_tag(self) -> object:
        stream: object = nbt_net_le_binary_stream(self.data, self.pos)
        tag: object = stream.read_root_tag()
        stream.pos: int = pos
        return tag
    
    def write_net_le_tag(self, value: object) -> None:
        stream: object = nbt_net_le_binary_stream()
        stream.write_root_tag(value)
        self.write(stream.data)
        
    def read_le_tag(self) -> object:
        stream: object = nbt_le_binary_stream(self.data, self.pos)
        tag: object = stream.read_root_tag()
        stream.pos: int = pos
        return tag
    
    def write_le_tag(self, value: object) -> None:
        stream: object = nbt_le_binary_stream()
        stream.write_root_tag(value)
        self.write(stream.data)

    def read_block_properties(self) -> list:
        block_properties: list = []
        length: int = self.read_var_int()
        for i in range(0, length):
            block_properties.append({
                "name": self.read_string(),
                "nbt": self.read_net_le_tag()
            })
            
    def write_block_properties(self, value: list) -> None:
        self.write_var_int(len(value))
        for block_property in value:
            self.write_string(block_property["name"])
            self.write_net_le_tag(block_property["nbt"])
            
    def read_item_extra_data_with_blocking_tick(self) -> dict:
        result: dict = {}
        result["has_nbt"]: bool = self.read_unsigned_short_le() > 0
        if result["has_nbt"]:
            result["version"]: int = self.read_unsigned_byte()
            result["nbt"]: object = self.read_le_tag()
        result["can_place_on"]: list = []
        can_place_on_count: int = self.read_int_le()
        for i in range(0, can_place_on_count):
            result["can_place_on"].append(self.read_short_array())
        result["can_destroy"]: list = []
        can_destroy_count: int = self.read_int_le()
        for i in range(0, can_destroy_count):
            result["can_destroy"].append(self.read_short_array())
        result["blocking_tick"]: int = self.read_long_le()
        return result
    
    def write_item_extra_data_with_blocking_tick(self, value: dict) -> None:
        if value["has_nbt"]:
            self.write_unsigned_short_le(65535)
            self.write_unsigned_byte(value["version"])
            self.write_le_tag(value["nbt"])
        else:
            self.write_unsigned_short_le(0)
        self.write_int_le(len(value["can_place_on"]))
        for item in value["can_place_on"]:
            self.write_short_array(item)
        self.write_int_le(len(value["can_destroy"]))
        for item in value["can_destroy"]:
            self.write_short_array(item)
        self.write_long_le(value["blocking_tick"])
        
    def read_item_extra_data_without_blocking_tick(self) -> dict:
        result: dict = {}
        result["has_nbt"]: bool = self.read_unsigned_short_le() > 0
        if result["has_nbt"]:
            result["version"]: int = self.read_unsigned_byte()
            result["nbt"]: object = self.read_le_tag()
        result["can_place_on"]: list = []
        can_place_on_count: int = self.read_int_le()
        for i in range(0, can_place_on_count):
            result["can_place_on"].append(self.read_short_array())
        result["can_destroy"]: list = []
        can_destroy_count: int = self.read_int_le()
        for i in range(0, can_destroy_count):
            result["can_destroy"].append(self.read_short_array())
        return result
    
    def write_item_extra_data_without_blocking_tick(self, value: dict) -> None:
        if value["has_nbt"]:
            self.write_unsigned_short_le(65535)
            self.write_unsigned_byte(value["version"])
            self.write_le_tag(value["nbt"])
        else:
            self.write_unsigned_short_le(0)
        self.write_int_le(len(value["can_place_on"]))
        for item in value["can_place_on"]:
            self.write_short_array(item)
        self.write_int_le(len(value["can_destroy"]))
        for item in value["can_destroy"]:
            self.write_short_array(item)
            
    def read_item_legacy(self) -> dict:
        result: dict = {
            "network_id": self.read_signed_var_int()
        }
        if result["network_id"] > 0:
            result["count"]: int = self.read_long_le()
            result["metadata"]: int = self.read_var_int()
            result["block_runtime_id"]: int = self.read_signed_var_int()
            result["extra"]: list = []
            extra_count: int = self.read_var_int()
            for i in range(0, extra_count):
                if result["network_id"] == 355:
                    result["extra"].append(self.read_item_extra_data_with_blocking_tick())
                else:
                    result["extra"].append(self.read_item_extra_data_without_blocking_tick())
        return result
                    
    def write_item_legacy(self, value: dict) -> None:
        self.write_signed_var_int(value["network_id"])
        if value["network_id"] > 0:
            self.write_long_le(value["count"])
            self.write_var_int(value["metadata"])
            self.write_signed_var_int(value["block_runtime_id"])
            self.write_var_int(len(value["extra"]))
            for extra in value["extra"]:
                if value["network_id"] == 355:
                    self.write_item_extra_data_with_blocking_tick(extra)
                else:
                    self.write_item_extra_data_without_blocking_tick(extra)
                    
    def read_item(self) -> dict:
        result: dict = {
            "network_id": self.read_signed_var_int()
        }
        if result["network_id"] > 0:
            result["count"]: int = self.read_long_le()
            result["metadata"]: int = self.read_var_int()
            result["has_stack_id"]: bool = self.read_bool()
            if result["has_stack_id"]:
                result["stack_id"]: int = self.read_signed_var_int()
            result["block_runtime_id"]: int = self.read_signed_var_int()
            result["extra"]: list = []
            extra_count: int = self.read_var_int()
            for i in range(0, extra_count):
                if result["network_id"] == 355:
                    result["extra"].append(self.read_item_extra_data_with_blocking_tick())
                else:
                    result["extra"].append(self.read_item_extra_data_without_blocking_tick())
        return result
                    
    def write_item(self, value: dict) -> None:
        self.write_signed_var_int(value["network_id"])
        if value["network_id"] > 0:
            self.write_long_le(value["count"])
            self.write_var_int(value["metadata"])
            if value["has_stack_id"]:
                self.write_signed_var_int(value["stack_id"])
            self.write_signed_var_int(value["block_runtime_id"])
            self.write_var_int(len(value["extra"]))
            for extra in value["extra"]:
                if value["network_id"] == 355:
                    self.write_item_extra_data_with_blocking_tick(extra)
                else:
                    self.write_item_extra_data_without_blocking_tick(extra)
                    
    def read_vector_3_int(self) -> object:
        return vector_3(
            self.read_signed_var_int(),
            self.read_signed_var_int(),
            self.read_signed_var_int()
        )
    
    def write_vector_3_int(self, value: object) -> None:
        self.write_signed_var_int(value.x)
        self.write_signed_var_int(value.y)
        self.write_signed_var_int(value.z)
        
    def read_vector_3_unsigned_int(self) -> object:
        return vector_3(
            self.read_var_int(),
            self.read_var_int(),
            self.read_var_int()
        )
    
    def write_vector_3_unsigned_int(self, value: object) -> None:
        self.write_var_int(value.x)
        self.write_var_int(value.y)
        self.write_var_int(value.z)
        
    def read_vector_3_float(self) -> object:
        return vector_3(
            self.read_float_le(),
            self.read_float_le(),
            self.read_float_le()
        )
    
    def write_vector_3_float(self, value: object) -> None:
        self.write_float_le(value.x)
        self.write_float_le(value.y)
        self.write_float_le(value.z)
        
    def read_vector_2_float(self) -> object:
        return vector_2(
            self.read_float_le(),
            self.read_float_le()
        )
    
    def write_vector_2_float(self, value: object) -> None:
        self.write_float_le(value.x)
        self.write_float_le(value.z)
        
    def read_metadata_dictionary(self) -> dict:
        metadata_dictionary: dict = {}
        length: int = self.read_var_int()
        for i in range(0, length):
            metadata_key: int = self.read_var_int()
            metadata_type: int = self.read_var_int()
            if metadata_type == metadata_dictionary_type.type_byte:
                metadata_value: int = self.read_byte()
            elif metadata_type == metadata_dictionary_type.type_short:
                metadata_value: int = self.read_short_le()
            elif metadata_type == metadata_dictionary_type.type_int:
                metadata_value: int = self.read_signed_var_int()
            elif metadata_type == metadata_dictionary_type.type_float:
                metadata_value: int = self.read_float_le()
            elif metadata_type == metadata_dictionary_type.type_string:
                metadata_value: int = self.read_string()
            elif metadata_type == metadata_dictionary_type.type_compound:
                metadata_value: int = self.read_net_le_tag()
            elif metadata_type == metadata_dictionary_type.type_vector_3_i:
                metadata_value: int = self.read_vector_3_int()
            elif metadata_type == metadata_dictionary_type.type_long:
                metadata_value: int = self.read_signed_var_long()
            elif metadata_type == metadata_dictionary_type.type_vector_3_f:
                metadata_value: int = self.read_vector_3_float()
            else:
                raise Exception("Invalid metadata type")
            metadata_dictionary[metadata_key]: dict = {"type": metadata_type, "value": metadata_value}
        return metadata_dictionary
    
    def write_metadata_dictionary(self, metadata_dictionary: dict) -> None:
        self.write_var_int(len(metadata_dictionary))
        for key, metadata in metadata_dictionary.items():
            self.write_var_int(key)
            self.write_var_int(metadata["type"])
            if metadata["type"] == metadata_dictionary_type.type_byte:
                self.write_byte(metadata["value"])
            elif metadata["type"] == metadata_dictionary_type.type_short:
                self.write_short_le(metadata["value"])
            elif metadata["type"] == metadata_dictionary_type.type_int:
                self.write_signed_var_int(metadata["value"])
            elif metadata["type"] == metadata_dictionary_type.type_float:
                self.write_float_le(metadata["value"])
            elif metadata["type"] == metadata_dictionary_type.type_string:
                self.write_string(metadata["value"])
            elif metadata["type"] == metadata_dictionary_type.type_compound:
                self.write_net_le_tag(metadata["value"])
            elif metadata["type"] == metadata_dictionary_type.type_vector_3_i:
                self.write_vector_3_int(metadata["value"])
            elif metadata["type"] == metadata_dictionary_type.type_long:
                self.write_signed_var_long(metadata["value"])
            elif metadata["type"] == metadata_dictionary_type.type_vector_3_f:
                self.write_vector_3_float(metadata["value"])
            else:
                raise Exception("Invalid metadata type")

    def read_link(self) -> dict:
        return {
            "ridden_entity_id": self.read_signed_var_long(),
            "rider_entity_id": self.read_signed_var_long(),
            "type": self.read_byte(),
            "immediate": self.read_bool(),
            "rider_initiated": self.read_bool()
        }
    
    def write_link(self, value: dict) -> None:
        self.write_signed_var_long(value["ridden_entity_id"])
        self.write_signed_var_long(value["rider_entity_id"])
        self.write_byte(value["type"])
        self.write_bool(value["immediate"])
        self.write_bool(value["rider_initiated"])
        
    def read_links(self) -> list:
        links: list = []
        length: int = self.read_var_int()
        for i in range(0, length):
            links.append(self.read_link())
        return links
        
    def write_links(self, value: list) -> None:
        self.write_var_int(len(value))
        for link in value:
            self.write_link(link)
            
    def read_entity_attributes(self) -> list:
        entity_attributes: list = []
        length: int = self.read_var_int()
        for i in range(0, length):
            entity_attributes.append({
                "name": self.read_string(),
                "min": self.read_float_le(),
                "value": self.read_float_le(),
                "max": self.read_float_le()
            })
        return entity_attributes
        
    def write_entity_attributes(self, value: list) -> None:
        self.write_var_int(len(value))
        for entity_attribute in value:
            self.write_string(entity_attribute["name"])
            self.write_float_le(entity_attribute["min"])
            self.write_float_le(entity_attribute["value"])
            self.write_float_le(entity_attribute["max"])

    def read_rotation(self) -> dict:
        return {
            "yaw": self.read_byte(),
            "pitch": self.read_byte(),
            "head_yaw": self.read_byte()
        }
    
    def write_rotation(self, value: dict) -> None:
        self.write_byte(value["yaw"])
        self.write_byte(value["pitch"])
        self.write_byte(value["head_yaw"])

    def read_block_coordinates(self) -> object:
        return vector_3(
            float(self.read_signed_var_int()),
            float(self.read_var_int()),
            float(self.read_signed_var_int())
        )
    
    def write_block_coordinates(self, value: object) -> None:
        self.write_signed_var_int(int(value.x))
        self.write_var_int(int(value.y))
        self.write_signed_var_int(int(value.z))
        
    def read_player_attributes(self) -> list:
        player_attributes: list = []
        length: int = self.read_var_int()
        for i in range(0, length):
            player_attributes.append({
                "min": self.read_float_le(),
                "max": self.read_float_le(),
                "current": self.read_float_le(),
                "default": self.read_float_le(),
                "name": self.read_string()
            })
        return player_attributes
        
    def write_player_attributes(self, value: list) -> None:
        self.write_var_int(len(value))
        for player_attribute in value:
            self.write_float_le(player_attribute["min"])
            self.write_float_le(player_attribute["max"])
            self.write_float_le(player_attribute["current"])
            self.write_float_le(player_attribute["default"])
            self.write_string(player_attribute["name"])
