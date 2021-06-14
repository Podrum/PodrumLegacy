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

class plugins_command:
    def __init__(self, server: object) -> None:
        self.server: object = server
        self.name: str = "plugins"
        self.description: str = "plugins command"
        self.aliases: list = ["pl"]
    
    def execute(self, args: list, sender: object) -> None:
        sender.send_message(f"Plugins({len(self.server.managers.plugin_manager.plugins)}): {', '.join(self.server.managers.plugin_manager.plugins)}")
