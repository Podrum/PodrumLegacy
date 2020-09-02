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

from copy import deepcopy
import pickle

from podrum.network.PacketPool import PacketPool
from podrum.utils.Binary import Binary

from pyraklib.protocol.EncapsulatedPacket import EncapsulatedPacket
from pyraklib.server.PyRakLibServer import PyRakLibServer
from pyraklib.server.ServerHandler import ServerHandler

class NetworkInterface:
    server = None
    players = []
    identifers = None
    identifiersACK = []
    interface = None
    tickTask = None
    upload = 0
    download = 0
    
    def __init__(self, server):
        self.server = server
        self.identifers = []
        server = PyRakLibServer(port = 19132, interface = "0.0.0.0")
        self.interface = ServerHandler(server, self)
        self.setName("Podrum powered server");
        loop = asyncio.get_event_loop()
        loop.call_later(5, stop)
        self.tickTask = loop.create_task(doTick())
        try:
            loop.run_until_complete(self.tickTask)
        except asyncio.CancelledError:
            pass 
        
    async def doTick(self):
        while True:
            self.interface.sendTick()
            await asyncio.sleep(1)
            
    def process(self):
        return self.interface.handlePacket()
    
    def closeSession(self, identifier, reason: str):
        try:
            self.players[identifier]
        except:
            pass
        else:
            self.player = self.players[identifier]
            del self.identifers[player]
            del self.players[identifier]
            del self.identifiersACK[identifier]
            #player.close(TextFormat.YELLOW + player.getName() + " has left the game", reason)
      
    def shutdown(self):
        self.tickTask.cancel()
        self.interface.shutdown()
        
    def emergencyShutdown(self):
        self.tickTask.cancel()
        self.interface.emergencyShutdown()
        
    def openSession(self, identifier, address, port, clientID):
        player = Player(self, clientID, address, port)
        self.players.insert(identifier, player)
        self.identifiersACK.insert(identifier, 0)
        self.identifers.insert(identifier, player)
        self.server.addPlayer(identifier, player)
        
    def handleEncapsulated(self, identifier, packet: EncapsulatedPacket, flags):
        try:
            self.players[identifier]
        except:
            pass
        else:
            pk = PacketPool.getPacket(packet.buffer)
            pk.decode()
            self.players[identifier].handleDataPacket(pk)
            
    def handleRaw(self, address: str, port: int, payload):
        self.server.handlePacket(address, port, payload)
        
    def putRaw(self, address, port, payload):
        self.interface.sendRaw(address, port, payload)
        
    def notifyACK(self, identifier, identifierACK):
        try:
            self.players[identifier]
        except:
            pass
        else:
            self.players[identifier].handleACK(identifierACK)
        
    def setName(self, name: str):
        self.interface.sendOption("name", f"MCPE;{name};407;1.16.0;0;0;0;PodrumPoweredServer;0")

    def handleOption(self, name: str, value: bytes):
        if name == "bandwidth":
            v = loads(value)
            self.upload = v["up"]
            self.download = v["down"]
            
    def getUploadUsage(self):
        return self.upload
    
    def getDownloadUsage(self):
        return self.download
