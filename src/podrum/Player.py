"""
*  ____           _
* |  _ \ ___   __| |_ __ _   _ _ __ ___
* | |_) / _ \ / _` | '__| | | | '_ ` _ \
* |  __/ (_) | (_| | |  | |_| | | | | | |
* |_|   \___/ \__,_|_|   \__,_|_| |_| |_|
*
* This program is free software: you can redistribute it and/or modify
* it under the terms of the GNU Lesser General Public License as published by
* the Free Software Foundation, either version 3 of the License, or
* (at your option) any later version.
"""

from podrum.network.protocol.types.PlayerPermissions import PlayerPermissions
from podrum.network.PacketPool import PacketPool
from podrum.network.protocol.ProtocolInfo import ProtocolInfo
from podrum.Server import Server

class Player:

    SURVIVAL = 0
    CREATIVE = 1
    ADVENTURE = 2
    SPECTATOR = 3
    VIEW = self.SPECTATOR

    connection = None
    server = None
    logger = None
    address = None
    name = None
    username = ""
    displayName = ""
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
    platformChatId = ''
    deviceOS = None
    deviceModel = None
    deviceId = None
    gamemode = None
    autoJump = True
    allowFlight = False
    flying = False
    inAirTicks = 0

    def __init__(self, connection, address, logger, server):
        self.connection = connection
        self.address = address
        self.logger = logger
        self.server = server
        
    def handleDataPacket(packet):
        pk = None
        if packet.NID == ProtocolInfo.ADVENTURE_SETTINGS_PACKET:
            pass
        elif packet.NID == ProtocolInfo.CLIENT_TO_SERVER_HANDSHAKE_PACKET:
            pass
        elif packet.NID == ProtocolInfo.LOGIN_PACKET:
            pass
        elif packet.NID == ProtocolInfo.RESOURCE_PACKS_INFO_PACKET:
            pass
        elif packet.NID == ProtocolInfo.SERVER_TO_CLIENT_HANDSHAKE_PACKET:
            pass

    def getClientId(self):
        return self.randomId

    def isAuthenticated(self):
        return self.xuid != ""

    def getXuid(self):
        return self.xuid

    def getPlayer(self):
        return self

    def getName(self):
        return self.username

    def getDisplayName(self):
        return self.displayName

    def isOp():
        return Server.isOp(self.getName())

    def setAllowedFlight(self, value):
        self.allowFlight = value
        self.sendSettings()

    def getAllowedFlight(self):
        return self.allowFlight

    def setFlying(self, value):
        if self.flying != value:
            self.flying = value
            self.resetFallDistance()
            self.sendSettings()

    def isFlying(self):
        return self.flying

    def resetFallDistance(self):
        self.inAirTicks = 0

    def getViewDistance(self):
        return self.viewDistance

    def getInAirTicks(self):
        return self.inAirTicks

    def isSpectator(self):
        return self.gamemode == self.SPECTATOR

    def sendSettings(self):
        PacketPool.AdventureSettingsPacket.setFlag(PacketPool.AdventureSettingsPacket.WORLD_IMMUTABLE, self.isSpectator())
        PacketPool.AdventureSettingsPacket.setFlag(PacketPool.AdventureSettingsPacket.NO_PVP, self.isSpectator())
        PacketPool.AdventureSettingsPacket.setFlag(PacketPool.AdventureSettingsPacket.AUTO_JUMP, self.autoJump)
        PacketPool.AdventureSettingsPacket.setFlag(PacketPool.AdventureSettingsPacket.ALLOW_FLIGHT, self.allowFlight)
        PacketPool.AdventureSettingsPacket.setFlag(PacketPool.AdventureSettingsPacket.NO_CLIP, self.isSpectator())
        PacketPool.AdventureSettingsPacket.setFlag(PacketPool.AdventureSettingsPacket.FLYING, self.flying)

        PacketPool.AdventureSettingsPacket.commandPermission = PacketPool.AdventureSettingsPacket.PERMISSION_OPERATOR if self.isOp() else PacketPool.AdventureSettingsPacket.PERMISSION_NORMAL
        PacketPool.AdventureSettingsPacket.playerPermission = PlayerPermissions.OPERATOR if self.isOp() else PlayerPermissions.MEMBER
        PacketPool.AdventureSettingsPacket.entityUniqueId = self.getId()
