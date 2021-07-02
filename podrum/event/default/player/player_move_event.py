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

from typing import Union
from podrum.event.event import event


class player_move_event(event):
    def __init__(self, player: object, toXYZ: Union[list, None]) -> None:
        self.player: object = player
        self.toX = toXYZ[0]
        self.toY = toXYZ[1]
        self.toZ = toXYZ[2]
