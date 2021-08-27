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
from typing import List

from podrum.forms.inputs.input_field import input_field

class step_slider(input_field):
    def __init__(self, text: str, options: list, default: int = None):
        super().__init__(text, 'step_slider')
        self.options: List[str] = options
        self.default_index: int = default
        
    @property
    def default(self) -> None:
        if self.default_index is None:
            return None
        try:
            return self.options[self.default_index]
        except IndexError:
            return None
            
    @default.setter
    def default(self, default: str) -> None:
        for index, option in enumerate(self.options):
            if option == default:
                self.default_index = index
                return
        self.default_index = None
            
    def to_dict(self) -> dict:
        return {
            'type': self.type,
            'text': self.text,
            'steps': self.options,
            'default': self.default_index or ""
        }
        
    @classmethod
    def from_dict(cls, obj) -> object:
        return cls(obj['text'], obj['steps'], obj.get('default', None))