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


from podrum.forms.inputs.input_field import input_field

class toggle(input_field):
    def __init__(self, text: str, default: bool = False):
        super().__init__(text, 'toggle')
        self.default = default
    
    def to_dict(self) -> dict:
        return {
            'type': self.type,
            'text': self.text,
            'default': self.default
        }
        
    @classmethod
    def from_dict(cls, obj) -> object:
        return cls(obj['text'], obj.get('default', False))