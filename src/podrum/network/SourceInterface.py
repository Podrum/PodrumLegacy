"""
*  ____           _
* |  _ \ ___   __| |_ __ _   _ _ __ ___
* | |_) / _ \ / _` | '__| | | | '_ ` _ \
* |  __/ (_) | (_| | |  | |_| | | | | | |
* |_|   \___/ \__,_|_|   \__,_|_| |_| |_|
*
* Licensed under the Apache License, Version 2.0 (the "License")
* you may not use this file except in compliance with the License.
* You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
"""

from podrum.Player import Player
from podrum.protocol.DataPacket import DataPacket

class SourceInterface:
    def putPacket(self, player: Player, packet: DataPacket, needACK = False, immediate = True): pass
    
    def close(self, player: Player, reason = "unknown reason"): pass
    
    def setName(self, name): pass
    
    def process(self): pass
    
    def shutdown(self): pass
    
    def emergencyShutdown(self): pass
