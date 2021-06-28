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

import binascii
from binary_utils.binary_stream import binary_stream
from nbt_utils.utils.nbt_le_binary_stream import nbt_le_binary_stream
from nbt_utils.utils.nbt_net_le_binary_stream import nbt_net_le_binary_stream
from podrum.geometry.vector_2 import vector_2
from podrum.geometry.vector_3 import vector_3
from podrum.protocol.mcbe.type.gamerule_type import gamerule_type
from podrum.protocol.mcbe.type.metadata_dictionary_type import metadata_dictionary_type
from podrum.protocol.mcbe.type.recipes_type import recipes_type
from podrum.protocol.mcbe.type.transaction_actions_type import transaction_actions_type
from podrum.protocol.mcbe.type.transaction_type import transaction_type

class mcbe_binary_stream(binary_stream):
    def read_uuid(self) -> str:
        stream: object = binary_stream()
        for i in range(0, 4):
            stream.write_int_be(self.read_int_le())
        return "-".join([
            binascii.hexlify(stream.read(4)),
            binascii.hexlify(stream.read(2)),
            binascii.hexlify(stream.read(2)),
            binascii.hexlify(stream.read(2)),
            binascii.hexlify(stream.read(6))
        ])
    
    def write_uuid(self, uuid: str) -> None:
        stream: object = binary_stream(binascii.unhexlify(uuid.replace("-", "")))
        for i in range(0, 4):
            self.write_int_le(stream.read_int_be())
    
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
        for i in range(0, self.read_short_le()):
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
        for i in range(0, self.read_short_le()):
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
        return texture_pack_infos
            
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
        for i in range(0, self.read_var_int()):
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
        for i in range(0, self.read_short_le()):
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
        for i in range(0, self.read_int_le()):
            experiments.append(self.read_experiment())
        return experiments
        
    def write_experiments(self, value: list) -> None:
        self.write_int_le(len(value))
        for experiment in value:
            self.write_experiment(experiment)
        
    def read_game_rule(self) -> dict:
        game_rule: dict = {
            "name": self.read_string(),
            "editable": self.read_bool(),
            "type": self.read_var_int()
        }
        if game_rule["type"] == gamerule_type.type_bool:
            game_rule["value"] = self.read_bool()
        elif game_rule["type"] == gamerule_type.type_int:
            game_rule["value"] = self.read_signed_var_int()
        elif game_rule["type"] == gamerule_type.type_float:
            game_rule["value"] = self.read_float_le()
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
        for i in range(0, self.read_var_int()):
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
        for i in range(0, self.read_var_int()):
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
        self.pos = stream.pos
        return tag
    
    def write_net_le_tag(self, value: object) -> None:
        stream: object = nbt_net_le_binary_stream()
        stream.write_root_tag(value)
        self.write(stream.data)
        
    def read_le_tag(self) -> object:
        stream: object = nbt_le_binary_stream(self.data, self.pos)
        tag: object = stream.read_root_tag()
        self.pos = stream.pos
        return tag
    
    def write_le_tag(self, value: object) -> None:
        stream: object = nbt_le_binary_stream()
        stream.write_root_tag(value)
        self.write(stream.data)

    def read_block_properties(self) -> list:
        block_properties: list = []
        for i in range(0, self.read_var_int()):
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
        result["has_nbt"] = self.read_unsigned_short_le() > 0
        if result["has_nbt"]:
            result["version"] = self.read_unsigned_byte()
            result["nbt"] = self.read_le_tag()
        result["can_place_on"] = []
        for i in range(0, self.read_int_le()):
            result["can_place_on"].append(self.read_short_array())
        result["can_destroy"] = []
        for i in range(0, self.read_int_le()):
            result["can_destroy"].append(self.read_short_array())
        result["blocking_tick"] = self.read_long_le()
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
        result["has_nbt"] = self.read_unsigned_short_le() > 0
        if result["has_nbt"]:
            result["version"] = self.read_unsigned_byte()
            result["nbt"] = self.read_le_tag()
        result["can_place_on"] = []
        for i in range(0, self.read_int_le()):
            result["can_place_on"].append(self.read_short_array())
        result["can_destroy"] = []
        for i in range(0, self.read_int_le()):
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
            result["count"] = self.read_long_le()
            result["metadata"] = self.read_var_int()
            result["block_runtime_id"] = self.read_signed_var_int()
            result["extra"] = []
            for i in range(0, self.read_var_int()):
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
            result["count"] = self.read_long_le()
            result["metadata"] = self.read_var_int()
            result["has_stack_id"] = self.read_bool()
            if result["has_stack_id"]:
                result["stack_id"] = self.read_signed_var_int()
            result["block_runtime_id"] = self.read_signed_var_int()
            result["extra"] = []
            for i in range(0, self.read_var_int()):
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
        for i in range(0, self.read_var_int()):
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
            elif metadata_type == metadata_dictionary_type.type_vector_3_int:
                metadata_value: int = self.read_vector_3_int()
            elif metadata_type == metadata_dictionary_type.type_long:
                metadata_value: int = self.read_signed_var_long()
            elif metadata_type == metadata_dictionary_type.type_vector_3_float:
                metadata_value: int = self.read_vector_3_float()
            else:
                raise Exception("Invalid metadata type")
            metadata_dictionary[metadata_key] = {"type": metadata_type, "value": metadata_value}
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
            elif metadata["type"] == metadata_dictionary_type.type_vector_3_int:
                self.write_vector_3_int(metadata["value"])
            elif metadata["type"] == metadata_dictionary_type.type_long:
                self.write_signed_var_long(metadata["value"])
            elif metadata["type"] == metadata_dictionary_type.type_vector_3_float:
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
        for i in range(0, self.read_var_int()):
            links.append(self.read_link())
        return links
        
    def write_links(self, value: list) -> None:
        self.write_var_int(len(value))
        for link in value:
            self.write_link(link)
            
    def read_entity_attributes(self) -> list:
        entity_attributes: list = []
        for i in range(0, self.read_var_int()):
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
        for i in range(0, self.read_var_int()):
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
            
    def read_transaction_use_item(self) -> dict:
        return {
            "action_type": self.read_var_int(),
            "block_position": self.read_vector_3_int(),
            "face": self.read_var_int(),
            "hotbar_slot": self.read_var_int(),
            "held_item": self.read_item(),
            "player_position": self.read_vector_3_float(),
            "click_position": self.read_vector_3_float(),
            "block_runtime_id": self.read_var_int()
        }
    
    def write_transaction_use_item(self, value: dict) -> None:
        self.write_var_int(value["action_type"])
        self.write_vector_3_int(value["block_position"])
        self.write_var_int(value["face"])
        self.write_var_int(value["hotbar_slot"])
        self.write_item(value["held_item"])
        self.write_vector_3_float(value["player_position"])
        self.write_vector_3_float(value["click_position"])
        self.write_var_int(value["block_runtime_id"])
        
    def read_transaction_actions(self) -> list:
        transaction_actions: list = []
        for i in range(0, self.read_var_int()):
            transaction_action: dict = {}
            transaction_action["source_type"] = self.read_var_int()
            if transaction_action["source_type"] == transaction_actions_type.type_container or transaction_action["source_type"] == transaction_actions_type.type_craft:
                transaction_action["inventory_id"] = self.read_var_int()
            if transaction_action["source_type"] == transaction_actions_type.type_world_interaction:
                transaction_action["flags"] = self.read_var_int()
            if transaction_action["source_type"] == transaction_actions_type.type_craft_slot or transaction_action["source_type"] == transaction_actions_type.type_craft:
                transaction_action["action"] = self.read_var_int()
            transaction_action["old_item"] = self.read_item()
            transaction_action["new_item"] = self.read_item()
            transaction_actions.append(transaction_action)
        return transaction_actions
    
    def write_transaction_actions(self, transaction_actions: list) -> None:
        self.write_var_int(len(transaction_actions))
        for transaction_action in transaction_actions:
            self.write_var_int(transaction_action["source_type"])
            if transaction_action["source_type"] == transaction_actions_type.type_container or transaction_action["source_type"] == transaction_actions_type.type_craft:
                self.write_var_int(transaction_action["inventory_id"])
            if transaction_action["source_type"] == transaction_actions_type.type_world_interaction:
                self.write_var_int(transaction_action["flags"])
            if transaction_action["source_type"] == transaction_actions_type.type_craft_slot or transaction_action["source_type"] == transaction_actions_type.type_craft:
                self.write_var_int(transaction_action["action"])
            self.write_item(transaction_action["old_item"])
            self.write_item(transaction_action["new_item"])
            
    def read_transaction_legacy(self) -> dict:
        transaction_legacy: dict = {}
        transaction_legacy["legacy_request_id"] = self.read_signed_var_int()
        if transaction_legacy["legacy_request_id"] > 0:
            legacy_transactions: list = []
            for i in range(0, self.read_var_int()):
                legacy_transaction: dict = {}
                legacy_transaction["container_id"] = self.read_unsigned_byte()
                legacy_transaction["changed_slots"] = []
                for i in range(0, self.read_var_int()):
                    legacy_transaction["changed_slots"].append(self.read_unsigned_byte())
                legacy_transactions.append(legacy_transaction)
            transaction_legacy["legacy_transactions"] = legacy_transactions
        return transaction_legacy
    
    def write_transaction_legacy(self, transaction_legacy: dict) -> None:
        self.write_signed_var_int(transaction_legacy["legacy_request_id"])
        if transaction_legacy["legacy_request_id"] > 0:
            self.write_var_int(len(transaction_legacy["legacy_transactions"]))
            for legacy_transaction in transaction_legacy["legacy_transactions"]:
                self.write_unsigned_byte(legacy_transaction["container_id"])
                self.write_var_int(len(legacy_transaction["changed_slots"]))
                for changed_slot in legacy_transaction["changed_slots"]:
                    self.write_unsigned_byte(changed_slot)
                    
    def read_transaction(self) -> dict:
        transaction: dict = {}
        transaction["legacy"] = self.read_transaction_legacy()
        transaction["transaction_type"] = self.read_var_int()
        transaction["actions"] = self.read_transaction_actions()
        if transaction["transaction_type"] == transaction_type.type_item_use:
            transaction["transaction_data"] = self.read_transaction_use_item()
        if transaction["transaction_type"] == transaction_type.type_item_use_on_entity:
            transaction["transaction_data"] = {
                "entity_runtime_id": self.read_var_long(),
                "action_type": self.read_var_int()
            }
        if transaction["transaction_type"] == transaction_type.type_item_release:
            transaction["transaction_data"] = {
                "action_type": self.read_var_int(),
                "hotbar_slot": self.read_signed_var_int(),
                "held_item": self.read_item(),
                "head_pos": self.read_vector_3_float()
            }
        return transaction
    
    def write_transaction(self, transaction: dict) -> None:
        self.write_transaction_legacy(transaction["legacy"])
        self.write_var_int(transaction["transaction_type"])
        self.write_transaction_actions(transaction["actions"])
        if transaction["transaction_type"] == transaction_type.type_item_use:
            self.write_transaction_use_item(transaction["transaction_data"])
        if transaction["transaction_type"] == transaction_type.type_item_use_on_entity:
            self.write_var_long(transaction["transaction_data"]["entity_runtime_id"])
            self.write_var_int(transaction["transaction_data"]["action_type"])
        if transaction["transaction_type"] == transaction_type.type_item_release:
            self.write_var_int(transaction["transaction_data"]["action_type"])
            self.write_signed_var_int(transaction["transaction_data"]["hotbar_slot"])
            self.write_item(transaction["transaction_data"]["held_item"])
            self.write_vector_3_float(transaction["transaction_data"]["head_pos"])
            
    def read_item_stacks(self) -> list:
        item_stacks: list = []
        for i in range(0, self.read_var_int()):
            item_stacks.append(self.read_item())
        return item_stacks
        
    def write_item_stacks(self, value: list) -> None:
        self.write_var_int(len(value))
        for item_stack in value:
            self.write_item(item_stack)
            
    def read_recipe_ingredient(self) -> dict:
        recipe_ingredient: dict = {}
        recipe_ingredient["network_id"] = self.read_signed_var_int()
        if recipe_ingredient["network_id"] > 0:
            recipe_ingredient["network_data"] = self.read_signed_var_int()
            recipe_ingredient["count"] = self.read_signed_var_int()
        return recipe_ingredient
    
    def write_recipe_ingredient(self, recipe_ingredient: dict) -> None:
        self.write_signed_var_int(recipe_ingredient["network_id"])
        if recipe_ingredient["network_id"] > 0:
            self.write_signed_var_int(recipe_ingredient["network_data"])
            self.write_signed_var_int(recipe_ingredient["count"])
            
    def read_potion_type_recipes(self) -> list:
        potion_type_recipes: list = []
        for i in range(0, self.read_var_int()):
            potion_type_recipes.append({
                "input_item_id": self.read_signed_var_int(),
                "input_item_meta": self.read_signed_var_int(),
                "ingredient_id": self.read_signed_var_int(),
                "ingredient_meta": self.read_signed_var_int(),
                "output_item_id": self.read_signed_var_int(),
                "output_item_meta": self.read_signed_var_int()
            })
        return potion_type_recipes
        
    def write_potion_type_recipes(self, potion_type_recipes: list) -> None:
        self.write_var_int(len(potion_type_recipes))
        for potion_type_recipe in potion_type_recipes:
            self.write_signed_var_int(potion_type_recipe["input_item_id"])
            self.write_signed_var_int(potion_type_recipe["input_item_meta"])
            self.write_signed_var_int(potion_type_recipe["ingredient_id"])
            self.write_signed_var_int(potion_type_recipe["ingredient_meta"])
            self.write_signed_var_int(potion_type_recipe["output_item_id"])
            self.write_signed_var_int(potion_type_recipe["output_item_meta"])
            
    def read_potion_container_change_recipes(self) -> list:
        potion_container_change_recipes: list = []
        for i in range(0, self.read_var_int()):
            potion_container_change_recipes.append({
                "input_item_id": self.read_signed_var_int(),
                "ingredient_id": self.read_signed_var_int(),
                "output_item_id": self.read_signed_var_int()
            })
        return potion_container_change_recipes
        
    def write_potion_container_change_recipes(self, potion_container_change_recipes: list) -> None:
        self.write_var_int(len(potion_container_change_recipes))
        for potion_container_change_recipe in potion_container_change_recipes:
            self.write_signed_var_int(potion_container_change_recipe["input_item_id"])
            self.write_signed_var_int(potion_container_change_recipe["ingredient_id"])
            self.write_signed_var_int(potion_container_change_recipe["output_item_id"])

    def read_recipes(self) -> list:
        recipes: list = []
        for i in range(0, self.read_var_int()):
            recipe: dict = {}
            recipe["type"] = self.read_signed_var_int()
            if recipe["type"] == recipes_type.type_shapeless or recipe["type"] == recipes_type.type_shulker_box or recipe["type"] == recipes_type.type_shapeless_chemistry:
                recipe["recipe_id"] = self.read_string()
                recipe["input"] = []
                for i in range(0, self.read_var_int()):
                    recipe["input"].append(self.read_recipe_ingredient())
                recipe["output"] = []
                for i in range(0, self.read_var_int()):
                    recipe["output"].append(self.read_item_legacy())
                recipe["uuid"] = self.read_string()
                recipe["block"] = self.read_string()
                recipe["priority"] = self.read_signed_var_int()
                recipe["network_id"] = self.read_var_int()
            if recipe["type"] == recipes_type.type_shaped or recipe["type"] == recipes_type.type_shaped_chemistry:
                pass
            if recipe["type"] == recipes_type.type_furnace:
                pass
            if recipe["type"] == recipes_type.type_furnace_with_metadata:
                pass
            if recipe["type"] == recipes_type.type_multi:
                pass
    
    def write_recipes(self, recipes: list) -> None:
        pass
