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


class input_field:
    def __init__(self, text: str, type: str) -> None:
        self.text: str = text
        self.type: str = type
        
    def to_dict(self) -> dict:
        raise NotImplementedError
        
    @classmethod
    def from_dict(cls, obj: dict) -> object:
        raise NotImplementedError
        
    def __eq__(self, other):
        return other.to_dict() == self.to_dict()