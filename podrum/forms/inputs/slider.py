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


from podrum.forms.inputs.input_field import input_field

class slider(input_field):
    def __init__(self, text: str, min: int, max: int, step: int, default: int = None):
        super().__init__(text, 'slider')
        self.min: int = min
        self.max: int= max
        self.step: int = step
        self.default: int = default
        
    def to_dict(self) -> dict:
        return {
            'type': self.type,
            'text': self.text,
            'min': self.min,
            'max': self.max,
            'step': self.step,
            'default': self.default if self.default is not None else self.min
        }
        
    @classmethod
    def from_dict(cls, obj: dict) -> object:
        return cls(obj['text'], obj['type'])