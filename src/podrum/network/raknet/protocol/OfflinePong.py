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

from podrum.network.raknet.protocol.OfflinePacket import OfflinePacket
from podrum.network.raknet.protocol.PacketIdentifiers import PacketIdentifiers

class OfflinePong(OfflinePacket):
    id = PacketIdentifiers.offlinePong
    timestamp = None
    serverGuid = None
    serverName = None
    
    def decodePayload(self):
        self.timestamp = self.getLong()
        self.serverGuid = self.getLong()
        self.getMagic()
        self.serverName = self.getString()
        
    def encodePayload(self):
        self.putLong(self.timestamp)
        self.putLong(self.serverGuid)
        self.putMagic()
        self.putString(self.serverName)
