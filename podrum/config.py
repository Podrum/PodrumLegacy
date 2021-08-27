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

import json
import os


# :config:
# A class made to create and
# edit configuration files.
class config:

    # [__init__]
    # :return: = None
    # Initialize the configuration
    # With a specific file path.
    def __init__(self, path: str) -> None:
        self.path: str = os.path.abspath(path)
        self.data: dict = {}
        basename: str = os.path.basename(self.path)
        extension: str = basename.rsplit(".")[1].lower()
        self.extension: str = extension
        if not os.path.isfile(path):
            self.save()
        if extension == "json":
            with open(self.path, "rt") as file:
                self.data: dict = json.load(file)
                file.close()

    # [save]
    # :return: = None
    # Saves the Config
    def save(self) -> None:
        if self.extension == "json":
            with open(self.path, "wt") as file:
                json.dump(self.data, file, indent=4)
                file.close()
