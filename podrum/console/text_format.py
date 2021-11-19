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
from typing import List, Tuple


class text_format:
    bold: str = "\x1b[1m"
    obfuscated: str = ""
    italic: str = "\x1b[3m"
    underline: str = "\x1b[4m"
    strike_through: str = "\x1b[9m"
    reset: str = "\x1b[m"
    black: str = "\x1b[38;5;16m"
    dark_blue: str = "\x1b[38;5;19m"
    dark_green: str = "\x1b[38;5;34m"
    dark_aqua: str = "\x1b[38;5;37m"
    dark_red: str = "\x1b[38;5;124m"
    gold: str = "\x1b[38;5;214m"
    gray: str = "\x1b[38;5;145m"
    dark_gray: str = "\x1b[38;5;59m"
    blue: str = "\x1b[38;5;63m"
    green: str = "\x1b[38;5;83m"
    aqua: str = "\x1b[38;5;87m"
    red: str = "\x1b[38;5;203m"
    light_purple: str = "\x1b[38;5;207m"
    yellow: str = "\x1b[38;5;227m"
    white: str = "\x1b[38;5;231m"
    minecoin_gold: str = "\x1b[38;5;185m"

    __translation: List[Tuple[str, str]] = [
        (black, '§0'),
        (dark_blue, '§1'),
        (dark_green, '§2'),
        (dark_blue, '§3'),
        (dark_red, '§4'),
        (light_purple, '§5'),
        (gold, '§6'),
        (gray, '§7'),
        (dark_gray, '§8'),
        (blue, '§9'),
        (green, '§a'),
        (aqua, '§b'),
        (red, '§c'),
        (light_purple, '§d'),
        (yellow, '§e'),
        (white, '§f'),
        (minecoin_gold, '§g'),
        (obfuscated, '§k'),
        (bold, '§l'),
        (strike_through, '§m'),
        (underline, '§n'),
        (italic, '§o'),
        (reset, '§r')
    ]

    @staticmethod
    def minecraft_to_console_colors(text: str) -> str:
        for pre, aft in text_format.__translation:
            text.replace(pre, aft)

        return text

    @staticmethod
    def console_to_minecraft_colors(text: str) -> str:
        for pre, aft in text_format.__translation:
            text.replace(aft, pre)

        return text
