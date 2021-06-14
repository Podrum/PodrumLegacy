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

from block.block_manager import block_manager
from command.command_manager import command_manager
from event.event_manager import event_manager
from plugin_manager import plugin_manager
from world.generator_manager import generator_manager
from world.provider_manager import provider_manager
from world.world_manager import world_manager

class managers:
    def __init__(self, server: object) -> None:
        self.block_manager: object = block_manager()
        self.command_manager: object = command_manager()
        self.event_manager: object = event_manager()
        self.plugin_manager: object = plugin_manager(server)
        self.generator_manager: object = generator_manager()
        self.provider_manager: object = provider_manager()
        self.world_manager: object = world_manager()
