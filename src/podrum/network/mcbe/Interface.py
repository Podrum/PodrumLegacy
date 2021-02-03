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

from podrum.BedrockPlayer import BedrockPlayer
from podrum.network.mcbe.Pool import Pool
from podrum.network.mcbe.protocol.BatchPacket import BatchPacket
from podrum.network.mcbe.protocol.Info import Info as McbeInfo
from podrum.network.mcbe.piprot.Info import Info as McpiInfo
from podrum.network.raknet.Interface import Interface as RaknetInterface
from podrum.network.raknet.InternetAddress import InternetAddress
from podrum.network.raknet.Server import Server
from podrum.utils.Logger import Logger
from threading import Thread

class Interface(RaknetInterface):
    raknet = None
    players = {}
    pool = None

    def __init__(self, address, port):
        self.raknet = Server(InternetAddress(address, port), self)
        self.pool = Pool()
        tick = Thread(target = self.tick())
        tick.setDaemon(True)
        tick.start()
        
    def tick(self):
        while True:
            self.setName("MCPE", "Dedicated Server", len(self.players), 10)
            self.setName("MCCPP", "Dedicated Server", len(self.players), 10)
        
    def setName(self, edition, motd, playerCount, playerMaxCount):
        edition = edition.upper()
        name = edition
        name += ";"
        if edition == "MCCPP":
            name += "Demo;"
        name += motd
        if edition == "MCPE":
            name += f";{McbeInfo.MCBE_PROTOCOL_VERSION};{McbeInfo.MCBE_VERSION};{playerCount};{playerMaxCount};{self.raknet.guid};"
        elif edition == "MCCPP":
            name += f" | {playerCount}/{playerMaxCount} | {McpiInfo.mcpiVersionNetwork}"
        self.raknet.name = name    

    def onOpenConnection(self, session):
        self.players[session.address.ip] = BedrockPlayer(session, session.address)
        Logger.info(f"{session.address.ip} connected")
        
    def onCloseConnection(self, address, reason):
        del self.players[address.ip] 
        Logger.info(f"{address.ip} disconnected due to {reason}")
        
    def onFrame(self, frame, address):
        if address.ip not in self.players:
            return
        player = self.players[address.ip]
        packet = BatchPacket()
        packet.buffer = frame.body
        packet.decode()
        for buffer in packet.getPackets():
            if buffer[0] in self.pool.pool:
                newPacket = self.pool.pool[buffer[0]]
                newPacket.buffer = buffer
                newPacket.decode()
                player.handleDataPacket(newPacket)
            else:
                print(hex(buffer[0]))
