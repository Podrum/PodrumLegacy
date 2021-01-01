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

from podrum.network.mcbe.protocol.BatchPacket import BatchPacket
from podrum.network.mcbe.Pool import Pool
from rakpy.server.Server import Server
from rakpy.server.Interface import Interface as RaknetInterface
from rakpy.utils.InternetAddress import InternetAddress

class Interface(RaknetInterface):
    raknet = None
    players = {}
    pool = None

    def __init__(self, address, port):
        self.raknet = Server(InternetAddress(address, port), self)
        self.raknet.name = "MCPE;Dedicated Server;390;1.14.60;0;10;13253860892328930865;Bedrock level;Survival;1;19132;19133;"
        self.pool = Pool()

    def onOpenConnection(self, connection):
        self.players[connection.address.address] = None # Not made the player class yet
        
    def onCloseConnection(self, address, reason):
        pass
        
    def onEncapsulated(self, packet, address):
        if address.address not in self.players:
            return
        player = self.players[address.address]
        pk = BatchPacket()
        pk.buffer = packet.buffer
        pk.decode()
        for buffer in pk.getPackets():
            if buffer[0] in self.pool.pool:
                packet = self.pool.pool[buffer[0]]
                packet.buffer = buffer
                packet.decode()
                # Handle data packets