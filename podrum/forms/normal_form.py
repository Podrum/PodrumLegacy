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

class normal_form(form):
    def __init__(self, title: str, content: str = None) -> None:
        super().__init__(title, 'form')
        self.content: str = content
        self.buttons: list = []
        
    def add_button(self, item: object) -> None:
        self.buttons.append(item)
        
    def remove_button(self, index: int) -> object:
        return self.buttons.pop(index)
        
    def clear_buttons(self) -> None:
        self.buttons.clear()
        
    def to_dict(self) -> dict:
        return {
            "type": self.type,
            "title": self.title,
            "content": self.content or "",
            "buttons": [button.to_dict() for button in self.buttons]
        }
        
    @classmethod
    def from_dict(cls, obj: dict) -> object:
        form = cls(obj['title'], obj['content'] or None)
        for button in obj['buttons']:
            form.add_button(inputs.button.from_dict(button))
        return form