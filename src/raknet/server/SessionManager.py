"""
PyRakLib networking library.
   This software is not affiliated with RakNet or Jenkins Software LLC.
   This software is a port of PocketMine/RakLib <https://github.com/PocketMine/RakLib>.
   All credit goes to the PocketMine Project (http://pocketmine.net)
 
   Copyright (C) 2015  PyRakLib Project

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
import copy
import json

import random
import time
import math
import pickle
import sys
from pyraklib.PyRakLib import PyRakLib
from pyraklib.Binary import Binary
from pyraklib.protocol import *
from pyraklib.protocol.DataPackets import *
from pyraklib.server.Session import Session


def microtime(get_as_float = False) :
    if get_as_float:
        return time.time()
    else:
        return '%f %d' % math.modf(time.time())


class SessionManager:
    packetPool = {}

    server = None
    socket = None

    receiveBytes = 0
    sendBytes = 0

    sessions = {}

    name = ""

    packetLimit = 1000

    shutdown = False

    ticks = 0
    lastMeasure = None

    block = {}
    ipSec = {}

    portChecking = False

    def __init__(self, server, socket):
        self.server = server
        self.socket = socket
        self.registerPackets()

        self.serverId = random.randint(0, sys.maxsize)

        self.run()

    def run(self):
        self.tickProcessor()

    def tickProcessor(self):
        self.lastMeasure = microtime(True)

        while not self.shutdown:
            start = microtime(True)
            max = 5000

            while --max and self.receivePacket(): pass
            while self.receiveStream(): pass

            time_ = microtime(True) - start
            if time_ < 0.05:
                time.sleep((microtime(True) + 0.05 - time_) - time.time())
            self.tick()

    def tick(self):
        time_ = microtime(True)
        values = list(self.sessions.values())
        for session in values:
            session.update(time_)

        for (address, count) in self.ipSec:
            if count > self.packetLimit or count == self.packetLimit:
                self.blockAddress(address)
        self.ipSec = {}

        if (self.ticks & 0b1111) == 0:
            diff = max(0.005, time_ - self.lastMeasure)
            self.streamOption("bandwith", json.dumps({
                "up":self.sendBytes / diff,
                "down":self.receiveBytes / diff
            }))
            self.lastMeasure = time_
            self.sendBytes = 0
            self.receiveBytes = 0

            if len(self.block) > 0:
                # TODO: Remove this?
                #self.block = sorted(self.block.items(), key=lambda x: x[1])
                now = microtime(True)
                for address in self.block.keys():
                    timeout = self.block.get(address)
                    if timeout < now or timeout == now:
                        del self.block[address]
                    else:
                        break
        self.ticks += 1

    def getPort(self):
        return self.server.port

    def receivePacket(self):
        data = self.socket.readPacket()
        if data == None:
            return
        else:
            buffer, source = data
        if len(buffer) > 0:
            self.receiveBytes += len(buffer)
            try:
                self.block[source]
                return True
            except: # self.block[source] is not set
                pass

            try:
                self.ipSec[source] += 1
            except:
                self.ipSec[source] = 1

            packet = self.getPacketFromPool(buffer[0])
            if packet is not None:
                packet.buffer = buffer
                self.getSession(source[0], source[1]).handlePacket(packet)
                return True
            elif buffer is not "":
                self.streamRaw(source[0], source[1], buffer)
                return True
            else:
                return False
        return False

    def sendPacket(self, packet, dest, port):
        packet.encode()
        self.sendBytes += len(packet.buffer)
        self.socket.writePacket(packet.buffer, dest, port)

    def streamEncapsulated(self, session, packet, flags = PyRakLib.PRIORITY_NORMAL):
        id = session.address + ":" + str(session.port)
        buffer = chr(PyRakLib.PACKET_ENCAPSULATED) + chr(len(id)) + id + chr(flags) + packet.toBinary(True)
        self.server.pushThreadToMainPacket(buffer)

    def streamRaw(self, address, port, payload):
        buffer = chr(PyRakLib.PACKET_RAW) + chr(len(address)) + address + Binary.writeShort(port) + payload
        self.server.pushThreadToMainPacket(buffer)

    def streamClose(self, identifier, reason):
        buffer = chr(PyRakLib.PACKET_CLOSE_SESSION) + chr(len(identifier)) + identifier + chr(len(reason)) + reason
        self.server.pushThreadToMainPacket(buffer)

    def streamInvalid(self, identifier):
        buffer = chr(PyRakLib.PACKET_INVALID_SESSION) + chr(len(identifier)) + identifier
        self.server.pushThreadToMainPacket(buffer)

    def streamOpen(self, session):
        identifier = session.address + ":" + str(session.port)
        buffer = chr(PyRakLib.PACKET_OPEN_SESSION) + chr(len(identifier)) + identifier + chr(len(session.address))
        self.server.pushThreadToMainPacket(buffer)

    def streamACK(self, identifier, identifierACK):
        buffer = chr(PyRakLib.PACKET_ACK_NOTIFICATION) + chr(len(identifier)) + identifier + str(Binary.writeInt(identifierACK))
        self.server.pushThreadToMainPacket(buffer)

    def streamOption(self, name, value):
        buffer = chr(PyRakLib.PACKET_SET_OPTION) + chr(len(str(name))) + str(name) + str(value)
        self.server.pushThreadToMainPacket(buffer)

    def receiveStream(self):
        packet = self.server.readMainToThreadPacket()
        if packet == None:
            return False
        if len(packet) > 0:
            id = ord(packet[0])
            offset = 1
            if id == PyRakLib.PACKET_ENCAPSULATED:
                
                length = ord(packet[offset])
                identifier = packet[offset:offset+length]
                offset += length + 1
                try:
                    self.sessions[identifier]

                    flags = ord(packet[offset])
                    buffer = packet[offset:]
                    self.sessions[identifier].addEncapsulatedToQueue(EncapsulatedPacket.fromBinary(buffer, True), flags)
                except NameError:
                    self.streamInvalid(identifier)
            elif id == PyRakLib.PACKET_RAW:
                
                length = ord(packet[offset])
                address = packet[offset:offset+length]
                offset += length
                port = Binary.readShort(packet[offset:offset+2])
                offset += 2
                payload = packet[offset:]
                self.socket.writePacket(payload, address, port)
            elif id == PyRakLib.PACKET_SET_OPTION:
                
                length = ord(packet[offset])
                offset += 1
                name = packet[offset:offset+length]
                offset += length
                value = packet[offset:]
                if name == "name":
                    print(name+" "+value)
                    self.name = value
                elif name == "portChecking":
                    self.portChecking = bool(value)
                elif name == "packetLimit":
                    self.packetLimit = int(value)
                else:
                    pass
                    #self.server.logger.error("Invalid option: "+name+" "+value)
            elif id == PyRakLib.PACKET_CLOSE_SESSION:
                length = ord(packet[offset])
                offset += 1
                identifier = packet[offset:offset+length]
                offset += length + 1
                length = ord(packet[offset])
                reason = packet[offset:offset+length]
                try:
                    s = self.sessions[identifier]
                    self.removeSession(s)
                except KeyError:
                    self.streamInvalid(identifier)
            elif id == PyRakLib.PACKET_INVALID_SESSION:
                
                length = ord(packet[offset])
                offset += 1
                identifier = packet[offset:offset+length]
                try:
                    self.removeSession(self.sessions[identifier])
                except KeyError:
                    pass
            elif id == PyRakLib.PACKET_BLOCK_ADDRESS:
                
                length = ord(packet[offset])
                address = packet[offset:offset+length]
                offset += length
                timeout = Binary.readInt(packet[offset:offset+4])
                self.blockAddress(address, timeout)
            elif id == PyRakLib.PACKET_SHUTDOWN:
                for session in self.sessions:
                    del session

                self.socket.close()
                self.shutdown = True
            elif id == PyRakLib.PACKET_EMERGENCY_SHUTDOWN:
                self.shutdown = True
            else:
                return False

            return True

    def blockAddress(self, address, timeout = 300):
        final = microtime(True) + timeout
        for (i, block) in enumerate(self.block):
            if i == address: #Isset
                if block < final:
                    self.block[i] = final
                    return

        self.block[address] = final

    def getSession(self, ip, port):
        id = ip + ":" + str(port)
        try:
            return self.sessions[id]
        except KeyError or NameError:
            self.sessions[id] = Session(self, ip, port)
            return self.sessions[id]

    def removeSession(self, session, reason = "unknown"):
        id = session.address + ":" + str(session.port)
        try:
            self.sessions[id].close()
            del self.sessions[id]
            self.streamClose(id, reason)
        except NameError or KeyError:
            pass

    def openSession(self, session):
        self.streamOpen(session)

    def notifyACK(self, session, identifierACK):
        self.streamACK(session.address + ":" + str(session.port), identifierACK)

    def getID(self):
        return self.serverId

    def registerPacket(self, id, clazz):
        self.packetPool[id] = clazz()

    def getPacketFromPool(self, id):
        try:
            return copy.copy(self.packetPool[id])
        except NameError:
            return None

    def registerPackets(self):
        self.registerPacket(UNCONNECTED_PING.PID, UNCONNECTED_PING)
        self.registerPacket(UNCONNECTED_PING_OPEN_CONNECTIONS.PID, UNCONNECTED_PING_OPEN_CONNECTIONS)
        self.registerPacket(OPEN_CONNECTION_REQUEST_1.PID, OPEN_CONNECTION_REQUEST_1)
        self.registerPacket(OPEN_CONNECTION_REQUEST_2.PID, OPEN_CONNECTION_REQUEST_2)
        self.registerPacket(OPEN_CONNECTION_REPLY_1.PID, OPEN_CONNECTION_REPLY_1)
        self.registerPacket(OPEN_CONNECTION_REPLY_2.PID, OPEN_CONNECTION_REPLY_2)
        self.registerPacket(UNCONNECTED_PONG.PID, UNCONNECTED_PONG)
        self.registerPacket(ADVERTISE_SYSTEM.PID, ADVERTISE_SYSTEM)
        self.registerPacket(DATA_PACKET_0.getPID(), DATA_PACKET_0)
        self.registerPacket(DATA_PACKET_1.getPID(), DATA_PACKET_1)
        self.registerPacket(DATA_PACKET_2.getPID(), DATA_PACKET_2)
        self.registerPacket(DATA_PACKET_3.getPID(), DATA_PACKET_3)
        self.registerPacket(DATA_PACKET_4.getPID(), DATA_PACKET_4)
        self.registerPacket(DATA_PACKET_5.getPID(), DATA_PACKET_5)
        self.registerPacket(DATA_PACKET_6.getPID(), DATA_PACKET_6)
        self.registerPacket(DATA_PACKET_7.getPID(), DATA_PACKET_7)
        self.registerPacket(DATA_PACKET_8.getPID(), DATA_PACKET_8)
        self.registerPacket(DATA_PACKET_9.getPID(), DATA_PACKET_9)
        self.registerPacket(DATA_PACKET_A.getPID(), DATA_PACKET_A)
        self.registerPacket(DATA_PACKET_B.getPID(), DATA_PACKET_B)
        self.registerPacket(DATA_PACKET_C.getPID(), DATA_PACKET_C)
        self.registerPacket(DATA_PACKET_D.getPID(), DATA_PACKET_D)
        self.registerPacket(DATA_PACKET_E.getPID(), DATA_PACKET_E)
        self.registerPacket(DATA_PACKET_F.getPID(), DATA_PACKET_F)
        self.registerPacket(ACK.getPID(), ACK)
        self.registerPacket(NACK.getPID(), NACK)