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

from podrum.command.default.debug_command import debug_command
from podrum.command.default.help_command import help_command
from podrum.command.default.plugins_command import plugins_command
from podrum.command.default.reload_command import reload_command
from podrum.command.default.say_command import say_command
from podrum.command.default.stop_command import stop_command
from podrum.command.default.tell_command import tell_command
from podrum.command.default.version_command import version_command
from podrum.command.default.kick_command import kick_command
from podrum.command.default.list_command import list_command
from podrum.command.default.me_command import me_command
from podrum.command.default.seed_command import seed_command
from podrum.command.default.gamemode_command import gamemode_command
from podrum.command.default.tell_command import tell_command
from podrum.command.default.time_command import time_command
from podrum.command.default.transfer_command import transfer_command
from podrum.command.default.weather_command import weather_command
from podrum.command.default.difficulty_command import difficulty_command

__all__ = (
    "debug_command", "help_command", "plugins_command", "reload_command",
    "say_command", "stop_command", "tell_command", "version_command",
    "kick_command", "list_command", "me_command", "seed_command",
    "gamemode_command", "tell_command", "time_command", "transfer_command", "weather_command",
    "difficulty_command"
)
