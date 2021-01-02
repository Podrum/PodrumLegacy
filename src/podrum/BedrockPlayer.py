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

class Player:
    connection = None
    address = None
    name = None
    locale = None
    randomId = None
    uuid = None
    xuid = None
    skin = None
    viewDistance = None
    gamemode = 0
    pitch = 0
    yaw = 0
    headYaw = 0
    onGround = False
    deviceOs = None
    deviceModel = None
    deviceId = None

    def __init__(self, connection, address):
        self.connection = connection
        self.address = address