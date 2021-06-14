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

from version import version

class version_command:
    def __init__(self, server: object) -> None:
        self.server: object = server
        self.name: str = "version"
        self.description: str = "version command"
        self.aliases: list = ["ver", "about"]
    
    def execute(self, args: list, sender: object) -> None:
        sender.send_message(f"This server is running Podrum version {version.podrum_version} {version.podrum_codename} on API {version.podrum_api_version}. This version is licensed under the {version.podrum_license} license.")
