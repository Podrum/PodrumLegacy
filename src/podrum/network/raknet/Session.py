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
from podrum.network.raknet.protocol.Reliability import Reliability
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
    fragmentId = 0
    sendSequenceNumber = 0
    lastSequenceNumber = -1
    sendReliableIndex = 0
    lastReliableIndex = 0
    packetToSend = []
    ackQueue = []
    nackQueue = []
    recoveryQueue = {}
    frameQueue = FrameSetPacket()
    fragmentedPackets = {}
    receivedSequenceNumbers = []

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
        if len(self.packetToSend) > 0:
            limit = 16
            for index, packet in enumerate(self.packetToSend):
                packet.sendTime = timestamp
                packet.encode()
                self.recoveryQueue[packet.sequenceNumber] = packet
                del self.packetToSend[index]
                self.sendPacket(packet)
                limit -= 1
                if limit <= 0:
                    break
            if len(self.packetToSend) > 2048:
                self.packetToSend = []
        for sequenceNumber, packet in dict(self.recoveryQueue).items():
            if packet.sendTime < time.time() - 8:
                self.packetToSend.append(packet)
                del self.recoveryQueue[sequenceNumber]
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
        priority = flags & 0b1
        if priority == RakNet.priority["Heap"]:
            packet = FrameSetPacket()
            packet.sequenceNumber = self.sendSequenceNumber
            self.sendSequenceNumber += 1
            packet.frames.append(frame)
            self.sendPacket(packet)
            packet.sendTime = time.time()
            self.recoveryQueue[packet.sequenceNumber] = packet
        else:
            if self.frameQueue.getLength() + frame.getFrameLength() > self.mtuSize:
                self.sendFrameQueue()
            self.frameQueue.frames.append(frame)
            
    def addFrameToQueue(self, frame, flags = RakNet.priority["Queue"]):
        if Reliability.isReliable(frame.reliability):
            frame.reliableIndex = self.sendReliableIndex
            self.sendReliableIndex += 1
            if frame.reliability == Reliability.reliableOrdered:
                frame.orderedIndex = self.channelIndex[frame.orderChannel]
                self.channelIndex[frame.orderChannel] += 1
        if frame.getFrameLength() > self.mtuSize:
            buffers = []
            for i in range(0, len(packet.buffer), self.mtuSize):
                buffers.append(packet.buffer[i:i + self.mtuSize])
            for index, buffer in enumerate(buffers):
                newFrame = Frame()
                newFrame.fragmentId = self.fragmentId
                newFrame.isFragmented = True
                newFrame.fragmentSize = len(buffers)
                newFrame.reliability = frame.reliability
                newFrame.fragmentIndex = index
                newFrame.body = buffer
                if index != 0:
                    newFrame.reliableIndex = self.sendReliableIndex
                    self.sendReliableIndex += 1
                if newFrame.reliability == Reliability.reliableOrdered:
                    newFrame.orderChannel = frame.orderChannel
                    newFrame.orderedIndex = frame.orderedIndex
                self.addToQueue(newFrame, flags)
            self.fragmentId += 1
        else:
            self.addToQueue(frame, flags)

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
                lostPacket.sendTime = time.time()
                self.sendPacket(lostPacket)
                del self.recoveryQueue[sequenceNumber]
                
    def handleFrameSetPacket(self, packet):
        if packet.sequenceNumber in self.receivedSequenceNumbers:
            return
        if packet.sequenceNumber in self.nackQueue:
            self.nackQueue.remove(packet.sequenceNumber)
        self.ackQueue.append(packet.sequenceNumber)
        self.receivedSequenceNumbers.append(packet.sequenceNumber)
        difference = packet.sequenceNumber - self.lastSequenceNumber
        if difference != 1:
            for i in range(self.lastSequenceNumber + 1, packet.sequenceNumber):
                if i not in self.receivedSequenceNumbers:
                    self.nackQueue.append(i)
        self.lastSequenceNumber = packet.sequenceNumber
        for frame in packet.frames:
            self.handleFrame(frame)
            
    def handleFrame(self, frame):
        if not Reliability.isReliable(frame.reliability):
            self.handlePacket(frame)
        else:
            holeCount = self.lastReliableIndex - frame.reliableIndex
            if holeCount == 0:
                self.handlePacket(frame)
                self.lastReliableIndex += 1
                
    def handleFrameFragment(self, frame):
        if frame.fragmentId not in self.fragmentedPackets:
            self.fragmentedPackets[frame.fragmentId] = {frame.fragmentIndex: frame}
        else:
            self.fragmentedPackets[frame.fragmentId][frame.fragmentIndex] = frame
        if len(self.fragmentedPackets[frame.fragmentId]) == frame.fragmentSize:
            newFrame = Frame()
            newFrame.body = b""
            for i in range(0, frame.fragmentSize):
                newFrame.body += self.fragmentedPackets[frame.fragmentId][i].body
            del self.fragmentedPackets[frame.fragmentId]
            self.handlePacket(newFrame)
                
    def handlePacket(self, frame):
        if frame.isFragmented:
            self.handleFrameFragment(frame)
        else:
            identifer = frame.body[0]
            if identifer < 0x80:
                if identifer == ConnectionRequest.id:
                    packet = ConnectionRequest()
                    packet.buffer = frame.body
                    packet.decode()
                    newPacket = ConnectionRequestAccepted()
                    newPacket.clientAddress = self.address
                    newPacket.systemIndex = 0
                    newPacket.systemAddresses = [InternetAddress("255.255.255.255", 19132)] * 20
                    newPacket.requestTimestamp = packet.timestamp
                    newPacket.timestamp = int(time.time())
                    newPacket.encode()
                    newFrame = Frame()
                    newFrame.reliability = 0
                    newFrame.body = newPacket.buffer
                    self.addToQueue(newFrame, RakNet.priority["Heap"])
                elif identifer == NewIncomingConnection.id:
                    packet = NewIncomingConnection()
                    packet.buffer = frame.body
                    packet.decode()
                    if packet.serverAddress.port == self.server.address.port:
                        self.state = RakNet.state["Connected"]
                        self.server.interface.onOpenConnection(self)
                elif identifer == DisconnectNotification.id:
                    self.disconnect("client disconnect")
                elif identifer == OnlinePing.id:
                    packet = OnlinePing()
                    packet.buffer = frame.body
                    packet.decode()
                    newPacket = OnlinePong()
                    newPacket.pingTimestamp = packet.timestamp
                    newPacket.pongTimestamp = int(time.time())
                    newPacket.encode()
                    newFrame = Frame()
                    newFrame.reliability = 0
                    newFrame.body = newPacket.buffer
                    self.addToQueue(newFrame)
            elif self.state == RakNet.state["Connected"]:
                self.server.interface.onFrame(frame, self.address)
                
    def close(self):
        self.addFrameToQueue(Frame.fromStream(BinaryStream(b"\x00\x00\x08\x15")), RakNet.priority["Heap"])
