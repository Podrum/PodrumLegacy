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

from podrum.forms.form import form
from podrum.forms.inputs import inputs

class modal_form(form):
    def __init__(self, title: str, content: str = None, *, button_1: object, button_2: object = None) -> None:
        super().__init__(title, 'modal')
        self.content: str = content
        self.button_1: object = button_1
        self.button_2: object = button_2
        
    def to_dict(self) -> dict:
        return {
            "type": self.type,
            "title": self.title,
            "content": self.content or "",
            "button1": self.button_1,
            "button2": self.button_2 or "",
        }
        
    @classmethod
    def from_dict(cls, obj: dict) -> object:
        return cls(
            obj['title'],
            obj['content'] or None,
            inputs.button.from_dict(obj['button1']),
            inputs.button.from_dict(obj['button2']) if 'button2' in obj else None,
        )