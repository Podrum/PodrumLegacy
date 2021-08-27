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


class icon:
    def __init__(self, path: str, builtin: bool = False) -> None:
        self.builtin: bool = builtin
        self.data: str = path
        
    def to_dict(self) -> dict:
        return {
            'type': 0 if self.builtin else 1,
            'data': self.data
        }
        
    @classmethod
    def from_dict(cls, obj) -> object:
        return cls(bool(obj['type']), obj['data'])
        
    def __eq__(self, other):
        return other.to_dict() == self.to_dict()