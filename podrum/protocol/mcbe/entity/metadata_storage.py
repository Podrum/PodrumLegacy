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

from podrum.protocol.mcbe.type.metadata_dictionary_type import metadata_dictionary_type

class metadata_storage:
    def __init__(self) -> None:
        self.metadata: dict = {}
          
    def get_entry(self, key: int) -> dict:
        if key in self.metadata:
            return self.metadata[key]
          
    def set_entry(self, key: int, value: object, entry_type: int) -> None:
        self.metadata[key] = {"value": value, "type": entry_type}
          
    def get_byte(self, key: int) -> int:
        entry: dict = self.get_entry(key)
        if (
            entry is not None
            and entry["type"] == metadata_dictionary_type.type_byte
        ):
            return entry["value"]
             
    def set_byte(self, key: int, value: int) -> None:
        self.set_entry(key, value, metadata_dictionary_type.type_byte)
        
    def get_short(self, key: int) -> int:
        entry: dict = self.get_entry(key)
        if (
            entry is not None
            and entry["type"] == metadata_dictionary_type.type_short
        ):
            return entry["value"]
             
    def set_short(self, key: int, value: int) -> None:
        self.set_entry(key, value, metadata_dictionary_type.type_short)
        
    def get_int(self, key: int) -> int:
        entry: dict = self.get_entry(key)
        if (
            entry is not None
            and entry["type"] == metadata_dictionary_type.type_int
        ):
            return entry["value"]
             
    def set_int(self, key: int, value: int) -> None:
        self.set_entry(key, value, metadata_dictionary_type.type_int)
        
    def get_float(self, key: int) -> float:
        entry: dict = self.get_entry(key)
        if (
            entry is not None
            and entry["type"] == metadata_dictionary_type.type_float
        ):
            return entry["value"]
             
    def set_float(self, key: int, value: float) -> None:
        self.set_entry(key, value, metadata_dictionary_type.type_float)
        
    def get_string(self, key: int) -> str:
        entry: dict = self.get_entry(key)
        if (
            entry is not None
            and entry["type"] == metadata_dictionary_type.type_string
        ):
            return entry["value"]
             
    def set_string(self, key: int, value: str) -> None:
        self.set_entry(key, value, metadata_dictionary_type.type_string)
        
    def get_compound(self, key: int) -> object:
        entry: dict = self.get_entry(key)
        if (
            entry is not None
            and entry["type"] == metadata_dictionary_type.type_compound
        ):
            return entry["value"]

    def set_compound(self, key: int, value: object) -> None:
        self.set_entry(key, value, metadata_dictionary_type.type_compound)
        
    def get_vector_3_int(self, key: int) -> object:
        entry: dict = self.get_entry(key)
        if (
            entry is not None
            and entry["type"] == metadata_dictionary_type.type_vector_3_int
        ):
            return entry["value"]
             
    def set_vector_3_int(self, key: int, value: object) -> None:
        self.set_entry(key, value, metadata_dictionary_type.type_vector_3_int)
        
    def get_long(self, key: int) -> int:
        entry: dict = self.get_entry(key)
        if (
            entry is not None
            and entry["type"] == metadata_dictionary_type.type_long
        ):
            return entry["value"]
             
    def set_long(self, key: int, value: int) -> None:
        self.set_entry(key, value, metadata_dictionary_type.type_long)
        
    def get_vector_3_float(self, key: int) -> object:
        entry: dict = self.get_entry(key)
        if (
            entry is not None
            and entry["type"] == metadata_dictionary_type.type_vector_3_float
        ):
            return entry["value"]
             
    def set_vector_3_float(self, key: int, value: object) -> None:
        self.set_entry(key, value, metadata_dictionary_type.type_vector_3_float)
        
    def get_flag(self, flag: int, extended: bool = False) -> bool:
        if not extended:
            flags: int = self.get_long(metadata_dictionary_type.key_flags)
        else:
            flags: int = self.get_long(metadata_dictionary_type.key_flags_extended)
        if flags is not None:
            return (flags & (1 << flag)) > 0
        
    def set_flag(self, flag: int, value: bool, extended: bool = False) -> None:
        current_value: bool = self.get_flag(flag, extended)
        if current_value is None or current_value != value:
            if current_value is None:
                flags: int = 0
            elif not extended:
                flags: int = self.get_long(metadata_dictionary_type.key_flags)
            else:
                flags: int = self.get_long(metadata_dictionary_type.key_flags_extended)
            if not extended:
                self.set_long(metadata_dictionary_type.key_flags, flags ^ (1 << flag))
            else:
                self.set_long(metadata_dictionary_type.key_flags_extended, flags ^ (1 << flag))
