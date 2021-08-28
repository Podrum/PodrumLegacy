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


class button(input_field):
    def __init__(self, text: str, icon = None):
        super().__init__(text, 'button')
        self.icon = icon
    
    def to_dict(self) -> dict:
        return {
            'text': self.text,
            'image': self.icon.to_dict() if self.icon is not None else ''
        }
        
    @classmethod
    def from_dict(cls, obj) -> object:
        return cls(obj['text'])