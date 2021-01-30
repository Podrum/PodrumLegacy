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

from podrum.network.raknet.RakNet import RakNet
from podrum.network.raknet.InternetAddress import InternetAddress
from podrum.network.raknet.protocol.Ack import Ack
from podrum.network.raknet.protocol.ConnectionRequest import ConnectionRequest
from podrum.network.raknet.protocol.ConnectionRequestAccepted import ConnectionRequestAccepted
from podrum.network.raknet.protocol.DisconnectNotification import DisconnectNotification
from podrum.network.raknet.protocol.Frame import Frame
from podrum.network.raknet.protocol.FrameSetPacket import FrameSetPacket
from podrum.network.raknet.protocol.Nack import Nack
from podrum.network.raknet.protocol.NewIncomingConnection import NewIncomingConnection
from podrum.network.raknet.protocol.OnlinePing import OnlinePing
from podrum.network.raknet.protocol.OnlinePong import OnlinePong
from podrum.utils.BinaryStream import BinaryStream
import time

class Session:
    server = None
    address = None
    mtuSize = None
    lastUpdate = None
    isActive = False
    state = RakNet.state["Connecting"]
    channelIndex = [0] * 32
    reliableIndex = 0
    fragmentId = 0
    sendSequenceNumber = 0
    lastSequenceNumber = -1
    resendQueue = []
    ackQueue = []
    nackQueue = []
    recoveryQueue = {}
    frameQueue = FrameSetPacket()
    fragmentedPackets = {}
    windowStart = -1
    windowEnd = 2048
    receivedWindow = []
    reliableWindowStart = 0
    reliableWindowEnd = 2048
    reliableWindow = {}
    lastReliableIndex = -1

    def __init__(self, server, address, mtuSize):
        self.server = server
        self.address = address
        self.mtuSize = mtuSize
        self.lastUpdate = time.time()
        
    def update(self, timestamp):
        if not self.isActive and self.lastUpdate + 10 < timestamp:
            self.disconnect("timeout")
            return
        self.isActive = False
        if len(self.ackQueue) > 0:
            newPacket = Ack()
            newPacket.sequenceNumbers = self.ackQueue
            self.sendPacket(newPacket)
            self.ackQueue = []
        if len(self.nackQueue) > 0:
            newPacket = Nack()
            newPacket.sequenceNumbers = self.nackQueue
            self.sendPacket(newPacket)
            self.nackQueue = []
        if len(self.resendQueue) > 0:
            limit = 16
            for index, packet in enumerate(self.resendQueue):
                packet.sendTime = timestamp
                packet.encode()
                self.recoveryQueue[packet.sequenceNumber] = packet
                del self.resendQueue[index]
                self.sendPacket(packet)
                limit -= 1
                if limit <= 0:
                    break
            if len(self.resendQueue) > 2048:
                self.resendQueue = []
        for sequenceNumber, packet in dict(self.recoveryQueue).items():
            if packet.sendTime < time.time() - 8:
                self.resendQueue.append(packet)
                del self.recoveryQueue[sequenceNumber]
            else:
                break
        for index, sequenceNumber in enumerate(self.receivedWindow):
            if sequenceNumber < self.windowStart:
                del self.receivedWindow[index]
            else:
                break
        self.sendFrameQueue()
        
    def disconnect(self, reason = "unknown"):
        self.server.removeSession(self.address, reason)
        
    def sendPacket(self, packet):
        packet.encode()
        self.server.socket.send(packet, self.address)

    def sendFrameQueue(self):
        if len(self.frameQueue.frames) > 0:
            self.frameQueue.sequenceNumber = self.sendSequenceNumber
            self.sendSequenceNumber += 1
            self.sendPacket(self.frameQueue)
            self.frameQueue.sendTime = time.time()
            self.recoveryQueue[self.frameQueue.sequenceNumber] = self.frameQueue
            self.frameQueue = FrameSetPacket()
            
    def addToQueue(self, frame, flags = RakNet.priority["Queue"]):
        priority = flags & RakNet.flag["flagPriority"]
        if priority == RakNet.priority["Heap"]:
            packet = FrameSetPacket()
            packet.sequenceNumber = self.sendSequenceNumber
            self.sendSequenceNumber += 1
            packet.frames.append(frame)
            self.sendPacket(packet)
            packet.sendTime = time.time()
            self.recoveryQueue[packet.sequenceNumber] = packet
        else:
            if self.sendQueue.getLength() + frame.getFrameLength() > self.mtuSize:
                self.sendFrameQueue()
            self.frameQueue.frames.append(frame)
            
    def addFrameToQueue(self, frame, flags):
        pass

    def handleAck(self, packet):
        for sequenceNumber in packet.sequenceNumbers:
            if sequenceNumber in self.recoveryQueue:
                del self.recoveryQueue[sequenceNumber]
                
    def handleNack(self, packet):
        for sequenceNumber in packet.sequenceNumbers:
            if sequenceNumber in self.recoveryQueue:
                lostPacket = self.recoveryQueue[sequenceNumber]
                lostPacket.sequenceNumber = self.sendSequenceNumber
                self.sendSequenceNumber += 1
                self.resendQueue.append(lostPacket)
                del self.recoveryQueue[sequenceNumber]
                
    def handleFrameSetPacket(self, packet):
        if packet.sequenceNumber < self.windowStart:
            return
        if packet.sequenceNumber > self.windowEnd:
            return
        if packet.sequenceNumber in self.receivedWindow:
            return
        difference = packet.sequenceNumber - self.lastSequenceNumber
        if packet.sequenceNumber in self.nackQueue:
            self.nackQueue.remove(packet.sequenceNumber)
        self.ackQueue.append(packet.sequenceNumber)
        self.receivedWindow.append(packet.sequenceNumber)
        if difference != 1:
            for i in range(self.lastSequenceNumber + 1, packet.sequenceNumber):
                if i not in self.receivedWindow:
                    self.nackQueue.append(i)
        if difference >= 1:
            self.lastSequenceNumber = packet.sequenceNumber
            self.windowStart += difference
            self.windowEnd += difference
        for frame in packet.frames:
            self.handleFrame(frame)
            
    def handleFrame(self, frame):
        if frame.reliableIndex is None:
            self.handlePacket(frame)
        else:
            if frame.reliableIndex < self.reliableWindowStart:
                return
            if frame.reliableIndex > self.reliableWindowEnd:
                return
            if frame.reliableIndex - self.lastReliableIndex == 1:
                self.lastReliableIndex += 1
                self.reliableWindowStart += 1
                self.reliableWindowEnd += 1
                self.handlePacket(frame)
                if len(self.reliableWindow) > 0:
                    self.reliableWindow = dict(sorted(self.reliableWindow.items()))
                    for index, reliableFrame in self.reliableWindow.items():
                        if index - self.lastReliableIndex != 1:
                            break
                        self.lastReliableIndex += 1
                        self.reliableWindowStart += 1
                        self.reliableWindowEnd += 1
                        self.handlePacket(reliableFrame)
                        del self.reliableWindow[index]
            else:
                self.reliableWindow[frame.reliableIndex] = frame
                
    def handlePacket(self, frame):
        if packet.isFragmented:
            return
        identifer = frame.body[0]
        if identifer < 0x80:
            if identifer == ConnectionRequest.id:
                packet = ConnectionRequest()
                packet.buffer = frame.boby
                packet.decode()
                newPacket = ConnectionRequestAccepted()
                newPacket.clientAddress = self.address
                newPacket.systemIndex = 0
                newPacket.systemAddresses = [InternetAddress("255.255.255.255", 19132)] * 20
                newPacket.requestTimestamp = dataPacket.timestamp
                newPacket.timestamp = time.time()
                newPacket.encode()
                newFrame = Frame()
                newFrame.reliability = 0
                newFrame.body = newPacket.buffer
                self.addToQueue(newFrame, RakNet.priority["Heap"])
            elif identifer == NewIncomingConnection.id:
                packet = NewIncomingConnection()
                packet.buffer = frame.boby
                packet.decode()
                if packet.port == self.server.address.port:
                    self.state = RakNet.state["Connected"]
                    self.server.interface.onOpenConnection(self)
            elif identifer == DisconnectNotification.id:
                self.disconnect("client disconnect")
            elif identifer == OnlinePing.id:
                packet = OnlinePing()
                packet.buffer = frame.boby
                packet.decode()
                newPacket = OnlinePong()
                newPacket.pingTimestamp = packet.timestamp
                newPacket.pongTimestamp
                newPacket.encode()
                newFrame = Frame()
                newFrame.reliability = 0
                newFrame.body = newPacket.buffer
                self.addToQueue(newFrame)
        elif self.state == RakNet.state["Connected"]:
            self.server.interface.onFrame(self, frame, self.address)
                
    def close(self):
        self.addFrameToQueue(Frame.fromStream(BinaryStream(b"\x00\x00\x08\x15")), RakNet.priority["Heap"])
