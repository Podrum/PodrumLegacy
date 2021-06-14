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
    purple: str = "\x1b[38;5;127m"
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

    @staticmethod
    def minecraft_to_console_colors(text: str) -> str:
        return text.replace("§0", text_format.black).replace("§1", text_format.dark_blue).replace("§2", text_format.dark_green).replace("§3", text_format.dark_aqua).replace("§4", text_format.dark_red).replace("§5", text_format.dark_red).replace("§6", text_format.gold).replace("§7", text_format.gray).replace("§8", text_format.dark_gray).replace("§9", text_format.blue).replace("§a", text_format.green).replace("§b", text_format.aqua).replace("§c", text_format.red).replace("§d", text_format.light_purple).replace("§e", text_format.yellow).replace("§f", text_format.white).replace("§k", text_format.obfuscated).replace("§l", text_format.bold).replace("§m", text_format.strike_through).replace("§n", text_format.underline).replace("§o", text_format.italic).replace("§r", text_format.reset)

    @staticmethod
    def console_to_minecraft_colors(text: str) -> str:
        return text.replace(text_format.black, "§0").replace(text_format.dark_blue, "§1").replace(text_format.dark_green, "§2").replace(text_format.dark_aqua, "§3").replace(text_format.dark_red, "§4").replace(text_format.dark_red, "§5").replace(text_format.gold, "§6").replace(text_format.gray, "§7").replace(text_format.dark_gray, "§8").replace(text_format.blue, "§9").replace(text_format.green, "§a").replace(text_format.aqua, "§b").replace(text_format.red, "§c").replace(text_format.light_purple, "§d").replace(text_format.yellow, "§e").replace(text_format.white, "§f").replace(text_format.obfuscated, "§k").replace(text_format.bold, "§l").replace(text_format.strike_through, "§m").replace(text_format.underline, "§n").replace(text_format.italic, "§o").replace(text_format.reset, "§r")

