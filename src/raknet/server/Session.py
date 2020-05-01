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
import math
import queue
import collections
from pyraklib import PyRakLib
from pyraklib.protocol import *
from pyraklib.protocol.ACK import ACK
from pyraklib.protocol.NACK import NACK
from pyraklib.protocol.DataPackets import DATA_PACKET_4, DATA_PACKET_0
import time as time_
import copy

def microtime(get_as_float = False):
    if get_as_float:
        return time_.time()
    else:
        return '%f %d' % math.modf(time_.time())

def str_split(s, n) -> str:
    ret = []
    for i in range(0, len(s), n):
        ret.append(s[i:i+n])
    return ret

def ksort(d):
     return [(k,d[k]) for k in sorted(d.keys())]

def isInList(item, l: list) -> bool:
    try:
        l[item]
        return True
    except NameError:
        return False
    except IndexError:
        return False
    except KeyError:
        return False

class Session:
    STATE_UNCONNECTED = 0
    STATE_CONNECTING_1 = 1
    STATE_CONNECTING_2 = 2
    STATE_CONNECTED = 3

    WINDOW_SIZE = 2048

    messageIndex = 0
    channelIndex = {}

    sessionManager = None
    address = None
    port = None
    state = STATE_UNCONNECTED
    preJoinQueue = []
    mtuSize = 548 # Min size
    id = 0
    splitID = 0

    sendSeqNumber = 0
    lastSeqNumber = -1

    lastUpdate = None
    startTime = None

    packetToSend = []

    isActive = None

    """@:type collections.deque"""
    ACKQueue = collections.deque()

    """@:type collections.deque"""
    NACKQueue = collections.deque()

    recoveryQueue = {}

    splitPackets = []

    needACK = []

    sendQueue = None

    windowStart = None
    """@:type collections.deque"""
    receivedWindow = collections.deque()
    windowEnd = None

    reliableWindowStart = None
    reliableWindowEnd = None
    reliableWindow = {}
    lastReliableIndex = -1

    def __init__(self, sessionManager, address, port):
        self.sessionManager = sessionManager
        self.address = address
        self.port = port
        self.sendQueue = DATA_PACKET_4()
        self.lastUpdate = microtime(True)
        self.startTime = microtime(True)
        self.isActive = False
        self.windowStart = -1
        self.windowEnd = self.WINDOW_SIZE

        self.reliableWindowStart = 0
        self.reliableWindowEnd = self.WINDOW_SIZE

        for i in range(0, 32):
            self.channelIndex[i] = 0

    def update(self, time):
        if not self.isActive and self.lastUpdate + 10 < time:
            self.disconnect("timeout")
            return
        self.isActive = False

        if len(self.ACKQueue) > 0:
            pk = ACK()
            pk.packets = self.ACKQueue
            self.sendPacket(pk)
            self.ACKQueue.clear()

        if len(self.NACKQueue) > 0:
            pk = NACK()
            pk.packets = self.NACKQueue
            self.sendPacket(pk)
            self.NACKQueue.clear()

        if len(self.packetToSend) > 0:
            limit = 16
            for (k, pk) in enumerate(self.packetToSend):
                pk.sendTime = time
                pk.encode()
                self.recoveryQueue[pk.seqNumber] = pk
                del self.packetToSend[k]
                self.sendPacket(pk)

                if --limit < 0 or --limit == 0:
                    break

            if len(self.packetToSend) > self.WINDOW_SIZE:
                self.packetToSend = []

        if len(self.needACK) > 0:
            for (identifierACK, indexes) in enumerate(self.needACK):
                if len(indexes) == 0:
                    del self.needACK[identifierACK]
                    self.sessionManager.notifyACK(self, identifierACK)

        for seq in copy.deepcopy(self.recoveryQueue).keys():
            pk = self.recoveryQueue.get(seq)
            if pk.sendTime is None:
                self.packetToSend.append(pk)
                del self.recoveryQueue[seq]
                continue
            if pk.sendTime < (int(time_.time()) - 8):
                self.packetToSend.append(pk)
                del self.recoveryQueue[seq]
            else:
                break

        for (seq, boolean) in enumerate(self.receivedWindow):
            if seq < self.windowStart:
                del self.receivedWindow[seq]
            else:
                break

        self.sendTheQueue()

    def disconnect(self, reason = "unknown"):
        self.sessionManager.removeSession(self, reason)

    def sendPacket(self, packet):
        self.sessionManager.sendPacket(packet, self.address, self.port)

    def sendTheQueue(self):
        if len(self.sendQueue.packets) > 0:
            self.sendSeqNumber += 1
            self.sendQueue.seqNumber = self.sendSeqNumber
            self.sendPacket(self.sendQueue)
            self.sendQueue.sendTime = microtime(True)
            self.recoveryQueue[self.sendQueue.seqNumber] = self.sendQueue
            self.sendQueue = DATA_PACKET_4()

    def addToQueue(self, pk, flags = PyRakLib.PRIORITY_NORMAL):
        priority = flags & 0b0000111
        if pk.needACK and pk.messageIndex != None:
            self.needACK[pk.identifierACK][pk.messageIndex] = pk.messageIndex
        if priority == PyRakLib.PRIORITY_IMMEDIATE: # Skip queues
            packet = DATA_PACKET_0()
            self.sendSeqNumber += 1
            packet.seqNumber = self.sendSeqNumber
            if pk.needACK:
                packet.packets.append(copy.copy(pk))
                pk.needACK = False
            else:
                packet.packets.append(pk.toBinary())
            self.sendPacket(packet)
            packet.sendTime = microtime(True)
            self.recoveryQueue[packet.seqNumber] = packet
            return

        length = self.sendQueue.length()
        if length + pk.getTotalLength() > self.mtuSize:
            self.sendTheQueue()

        if pk.needACK:
            self.sendQueue.packets.append(copy.copy(pk))
            pk.needACK = False
        else:
            self.sendQueue.packets.append(pk.toBinary())

    def addEncapsulatedToQueue(self, packet, flags = PyRakLib.PRIORITY_NORMAL):
        packet.needACK = (flags & PyRakLib.FLAG_NEED_ACK)
        if packet.needACK > 0:
            self.needACK[packet.identifierACK] = []

        r = packet.reliability
        if r == 2 or r == 3 or r == 4 or r == 6 or r == 7:
            self.messageIndex += 1
            packet.messageIndex = self.messageIndex
            if r == 3:
                self.channelIndex[packet.orderChannel] += 1
                packet.orderIndex = self.channelIndex[packet.orderChannel]

        if packet.getTotalLength() + 4 > self.mtuSize:
            buffers = str_split(packet.buffer, self.mtuSize - 34)
            self.splitID += 1
            splitID = self.splitID % 65536
            for (count, buffer) in enumerate(buffers):
                pk = EncapsulatedPacket()
                pk.splitID = splitID
                pk.hasSplit = True
                pk.splitCount = len(buffers)
                pk.reliability = packet.reliability
                pk.splitIndex = count
                pk.buffer = buffer
                if count > 0:
                    self.messageIndex += 1
                    pk.messageIndex = self.messageIndex
                else:
                    pk.messageIndex = packet.messageIndex
                if pk.reliability == 3:
                    pk.orderChannel = packet.orderChannel
                    pk.orderIndex = packet.orderIndex
                self.addToQueue(pk, flags | PyRakLib.PRIORITY_IMMEDIATE)
        else:
            self.addToQueue(packet, flags)

    def handleSplit(self, packet):
        if packet.splitCount > 128 or packet.splitCount == 128:
            return

        try:
            self.splitPackets[packet.splitID][packet.splitIndex] = packet
        except NameError:
            self.splitPackets[packet.splitID] = [packet.splitIndex]

        if len(self.splitPackets[packet.splitID]) == packet.splitCount:
            pk = EncapsulatedPacket()
            pk.buffer = ""
            for i in range(0, packet.splitCount):
                pk.buffer += self.splitPackets[packet.splitID][i].buffer

            pk.length = len(pk.buffer)

            self.handleEncapsulatedPacketRoute(pk)

    def handleEncapsulatedPacket(self, packet):
        if packet.messageIndex == None:
            self.handleEncapsulatedPacketRoute(packet)
        else:
            if packet.messageIndex < self.reliableWindowStart or packet.messageIndex > self.reliableWindowEnd:
                return

            if packet.messageIndex - self.lastReliableIndex == 1:
                self.lastReliableIndex += 1
                self.reliableWindowStart += 1
                self.reliableWindowEnd += 1
                self.handleEncapsulatedPacketRoute(packet)

                if len(self.reliableWindow) > 0:
                    ksort(self.reliableWindow)

                    for (index, pk) in enumerate(self.reliableWindow):
                        if index - self.lastReliableIndex != 1:
                            break
                        self.lastReliableIndex += 1
                        self.reliableWindowStart += 1
                        self.reliableWindowEnd += 1
                        self.handleEncapsulatedPacketRoute(pk)
                        del self.reliableWindow[index]
            else:
                self.reliableWindow[packet.messageIndex] = packet

    def handleEncapsulatedPacketRoute(self, packet):
        if self.sessionManager == None:
            return

        if packet.hasSplit:
            if self.state == self.STATE_CONNECTED:
                self.handleSplit(packet)
            return

        id = packet.buffer[0]
        if id < 0x80: # internal data packet
            if self.state == self.STATE_CONNECTING_2:
                if id == CLIENT_CONNECT_DataPacket.PID:
                    dataPacket = CLIENT_CONNECT_DataPacket()
                    dataPacket.buffer = packet.buffer
                    dataPacket.decode()
                    pk = SERVER_HANDSHAKE_DataPacket()
                    pk.address = self.address
                    pk.port = self.port
                    pk.sendPing = dataPacket.sendPing
                    pk.sendPong = dataPacket.sendPing + 1000
                    pk.encode()

                    sendPacket = EncapsulatedPacket()
                    sendPacket.reliability = 0
                    sendPacket.buffer = pk.buffer
                    self.addToQueue(sendPacket, PyRakLib.PRIORITY_IMMEDIATE)
                elif id == CLIENT_HANDSHAKE_DataPacket.PID:
                    dataPacket = CLIENT_HANDSHAKE_DataPacket()
                    dataPacket.buffer = packet.buffer
                    dataPacket.decode()

                    if dataPacket.port == self.sessionManager.getPort() or not self.sessionManager.portChecking:
                        self.state = self.STATE_CONNECTED # FINALLY!
                        self.sessionManager.openSession(self)
                        for p in self.preJoinQueue:
                            self.sessionManager.streamEncapsulated(self, p)

            elif id == CLIENT_DISCONNECT_DataPacket.PID:
                self.disconnect("client disconnect")
            elif id == PING_DataPacket.PID:
                dataPacket = PING_DataPacket()
                dataPacket.buffer = packet.buffer
                dataPacket.decode()

                pk = PONG_DataPacket()
                pk.pingID = dataPacket.pingID
                pk.encode()

                sendPacket = EncapsulatedPacket()
                sendPacket.reliability = 0
                sendPacket.buffer = pk.buffer
                self.addToQueue(sendPacket)
            elif self.state == self.STATE_CONNECTED:
                self.sessionManager.streamEncapsulated(self, packet)
                # TODO: Stream channels
            else:
                self.preJoinQueue.append(packet)

    def handlePacket(self, packet):
        self.isActive = True
        self.lastUpdate = microtime(True)
        if self.state == self.STATE_CONNECTED or self.state == self.STATE_CONNECTING_2:
            if packet.buffer[0] >= 0x80 and packet.buffer[0] <= 0x8f and isinstance(packet, DataPacket):
                packet.decode()

                """
                try:
                    self.receivedWindow[packet.seqNumber]
                    go = True
                except KeyError:
                    go = False
                """
                if packet.seqNumber < self.windowStart or packet.seqNumber > self.windowEnd or isInList(packet.seqNumber, self.receivedWindow):
                    return

                diff = packet.seqNumber - self.lastSeqNumber

                if isInList(packet.seqNumber, self.NACKQueue):
                    self.NACKQueue.remove(packet.seqNumber)

                self.ACKQueue.append(packet.seqNumber)
                self.receivedWindow[packet.seqNumber] = packet.seqNumber

                if diff != 1:
                    i = self.lastSeqNumber + 1
                    while i < packet.seqNumber:
                        try:
                            self.receivedWindow[i]
                        except IndexError:
                            self.NACKQueue[i] = i
                        i += 1

                if diff >= 1:
                    self.lastSeqNumber = packet.seqNumber
                    self.windowStart += diff
                    self.windowEnd += diff

                for pk in packet.packets:
                    self.handleEncapsulatedPacket(pk)

            elif isinstance(packet, ACK):
                packet.decode()
                for seq in packet.seqNums:
                    try:
                        for pk in self.recoveryQueue[seq]:
                            if isinstance(pk, EncapsulatedPacket) and pk.needACK and pk.messageIndex != None:
                                del self.needACK[pk.identifierACK][pk.messageIndex]
                    except NameError:
                        pass

            elif isinstance(packet, NACK):
                packet.decode()
                for seq in packet.seqNums:
                    try:
                        pk = self.recoveryQueue[seq]
                        self.sendSeqNumber += 1
                        pk.seqNumber = self.sendSeqNumber
                        self.packetToSend.append(pk)
                        del self.recoveryQueue[seq]
                    except NameError:
                        pass
        elif packet.buffer[0] > 0x00 and packet.buffer[0] < 0x80: # Not data packet :)
            packet.decode()
            if isinstance(packet, UNCONNECTED_PING):
                pk = UNCONNECTED_PONG()
                pk.serverID = 0#self.sessionManager.getID()
                pk.pingID = packet.pingID
                pk.serverName = self.sessionManager.name
                self.sendPacket(pk)
            elif isinstance(packet, OPEN_CONNECTION_REQUEST_1):
                packet.protocol # TODO: check protocol number and refuse connections
                pk = OPEN_CONNECTION_REPLY_1()
                pk.mtuSize = packet.mtuSize
                pk.serverID = self.sessionManager.getID()
                self.sendPacket(pk)
                self.state = self.STATE_CONNECTING_1
            elif self.state == self.STATE_CONNECTING_1 and isinstance(packet, OPEN_CONNECTION_REQUEST_2):
                self.id = packet.clientID
                if int(packet.serverAddress[1]) == self.sessionManager.getPort() or not self.sessionManager.portChecking:
                    self.mtuSize = min(abs(packet.mtuSize), 1464) # Max size, do not allow creating large buffers to fill server memory
                    pk = OPEN_CONNECTION_REPLY_2()
                    pk.mtuSize = self.mtuSize
                    pk.serverID = self.sessionManager.getID()
                    pk.clientAddress = self.address, self.port, 4
                    self.sendPacket(pk)
                    self.state = self.STATE_CONNECTING_2

    def close(self):
        data = "\x00\x00\x08\x15"
        self.addEncapsulatedToQueue(EncapsulatedPacket.fromBinary(data)[0], PyRakLib.PRIORITY_IMMEDIATE)
        self.sessionManager = None