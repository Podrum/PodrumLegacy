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

from podrum.forms.inputs import inputs
from podrum.forms.form import form

class custom_form(form):
    def __init__(self, title: str) -> None:
        super().__init__(title, 'custom_form')
        self.content: list = []
        
    def add_entry(self, item: object) -> None:
        self.content.append(item)
        
    def remove_entry(self, index) -> object:
        return self.content.pop(index)
        
    def clear_entries(self) -> None:
        self.content.clear()
        
    def to_dict(self) -> dict:
        return {
            "type": self.type,
            "title": self.title,
            "content": [entry.to_dict() for entry in self.content]
        }
        
    @classmethod
    def from_dict(cls, obj: dict) -> object:
        form = cls(obj['title'])
        items = {
            'dropdown': inputs.dropdown,
            'input': inputs.text_input,
            'label': inputs.label,
            'slider': inputs.slider,
            'step_slider': inputs.step_slider,
            'toggle': inputs.toggle,
            'button': inputs.button
        }
        for entry in obj['content']:
            form.add_entry(items[entry.get('type', 'button')].from_dict(entry))
        return form