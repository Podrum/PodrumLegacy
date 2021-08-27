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

from podrum.event.event import event

class player_form_response_event(event):
    
    # Gets called when a player submits a form.

    def __init__(self, form_id: int, data: object, player: object) -> None:
        self.form_id = form_id
        self.player = player
        self.cancelled = data is None
        self.form_type = None
        self.response = data
        if isinstance(data, list):
            self.form_type = 'custom'
            self.response = data
        elif isinstance(data, bool):
            self.form_type = 'modal'
        elif isinstance(data, int):
            self.form_type = 'normal'