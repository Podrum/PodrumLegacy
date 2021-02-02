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

from podrum.network.mcbe.piprot.Info import Info
from podrum.network.mcbe.piprot.Packet import Packet

class LoginPacket(Packet):
    id = Info.loginPacket
    username = None
    protocol1 = None
    protocol2 = None
    
    def decodePayload(self):
        self.username = self.getString()
        self.protocol1 = self.getInt()
        self.protocol2 = self.getInt()
        
    def encodePayload(self):
        self.putString(self.username)
        self.putInt(self.protocol1)
        self.putInt(self.protocol2)
