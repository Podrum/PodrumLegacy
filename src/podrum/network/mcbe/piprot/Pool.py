"""
*  ____           _
* |  _ \ ___   __| |_ __ _   _ _ __ ___
* | |_) / _ \ / _` | '__| | | | '_ ` _ \
* |  __/ (_) | (_| | |  | |_| | | | | | |
* |_|   \___/ \__,_|_|   \__,_|_| |_| |_|
*
* Licensed under the Mozilla Public License, Version 2.
* Permissions of this weak copyleft license are conditioned on making
* available source code of licensed files and modifications of those files 
* under the same license (or in certain cases, one of the GNU licenses).
* Copyright and license notices must be preserved. Contributors
* provide an express grant of patent rights. However, a larger work
* using the licensed work may be distributed under different terms and without 
* source code for files added in the larger work.
"""

from podrum.network.mcbe.piprot.LoginPacket import LoginPacket
from podrum.network.mcbe.piprot.LoginStatusPacket import LoginStatusPacket
from podrum.network.mcbe.piprot.MessagePacket import MessagePacket
from podrum.network.mcbe.piprot.ReadyPacket import ReadyPacket
from podrum.network.mcbe.piprot.SetTimePacket import SetTimePacket
from podrum.network.mcbe.piprot.StartGamePacket import StartGamePacket
 
class Pool:
    pool = {}
    
    def __init__(self):
        self.registerPackets()
        
    def registerPacket(self, packet):
        self.pool[packet.id] = packet
        
    def registerPackets(self):
        self.registerPacket(LoginPacket())
        self.registerPacket(LoginStatusPacket())
        self.registerPacket(MessagePacket())
        self.registerPacket(ReadyPacket())
        self.registerPacket(SetTimePacket())
        self.registerPacket(StartGamePacket())
