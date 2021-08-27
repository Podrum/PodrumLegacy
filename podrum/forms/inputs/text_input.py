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

class text_input(input_field):
    def __init__(self, text: str, placeholder: str, default: str = None):
        super().__init__(text, 'input')
        self.placeholder: str = placeholder
        self.default: str = default
        
    def to_dict(self) -> dict:
        return {
            'type': self.type,
            'text': self.text,
            'placeholder': self.placeholder,
            'default': self.default or ""
        }
        
    @classmethod
    def from_dict(cls, obj: dict) -> object:
        return cls(obj['text'], obj['placeholder'], obj.get('default'))