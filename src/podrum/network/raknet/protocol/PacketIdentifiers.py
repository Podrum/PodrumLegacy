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

class PacketIdentifiers:
    onlinePing = 0x00
    offlinePing = 0x01
    offlinePingOpenConnections = 0x02
    onlinePong = 0x03
    openConnectionRequest1 = 0x05
    openConnectionReply1 = 0x06
    openConnectionRequest2 = 0x07
    openConnectionReply2 = 0x08
    ConnectionRequest = 0x09
    ConnectionRequestAccepted = 0x10
    newIncommingConnection = 0x13
    disconnectNotification = 0x15
    incompatibleProtocol = 0x19
    offlinePong = 0x1c
    advertiseSystem = 0x1d
    nack = 0xa0
    ack = 0xc0
