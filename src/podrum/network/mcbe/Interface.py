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
from podrum.network.mcbe.protocol.BatchPacket import BatchPacket
from podrum.network.mcbe.Pool import Pool
from podrum.network.raknet.Interface import Interface as RaknetInterface
from podrum.network.raknet.InternetAddress import InternetAddress
from podrum.network.raknet.Server import Server
from podrum.utils.Logger import Logger

class Interface(RaknetInterface):
    raknet = None
    players = {}
    pool = None

    def __init__(self, address, port):
        self.raknet = Server(InternetAddress(address, port), self)
        self.raknet.name = "MCPE;Dedicated Server;390;1.14.60;0;10;13253860892328930865;Bedrock level;Survival;1;19132;19133;"
        self.pool = Pool()

    def onOpenConnection(self, session):
        self.players[session.address.ip] = BedrockPlayer(session, session.address)
        
    def onCloseConnection(self, address, reason):
        Logger.info(f"{address.ip} disconnected due to {reason}")
        
    def onFrame(self, packet, address):
        if address.ip not in self.players:
            return
        player = self.players[address.ip]
        pk = BatchPacket()
        pk.buffer = packet.body
        pk.decode()
        for buffer in pk.getPackets():
            if buffer[0] in self.pool.pool:
                packet = self.pool.pool[buffer[0]]
                packet.buffer = buffer
                packet.decode()
                player.handleDataPacket(packet)
            else:
                print(hex(buffer[0]))
