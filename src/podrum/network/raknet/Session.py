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
    reliableIndex = 0
    fragmentId = 0
    sendSequenceNumber = 0
    lastSequenceNumber = -1
    packetToSend = []
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
            frame.reliableIndex = self.reliableIndex
            self.reliableIndex += 1
            if frame.reliability == Reliability.reliableOrdered:
                frame.orderedIndex = self.channelIndex[frame.orderChannel]
                self.channelIndex[frame.orderChannel] += 1
        if frame.getFrameLength() > self.mtuSize:
            buffers = []
            for i in range(0, len(packet.buffer), self.mtuSize):
                buffers.append(packet.buffer[i:i + self.mtuSize])
            self.fragmentId += 1
            fragmentId = self.fragmentId % 65536
            for count, buffer in enumerate(buffers):
                newFrame = Frame()
                newFrame.fragmentId = splitID
                newFrame.isFragmented = True
                newFrame.fragmentSize = len(buffers)
                newFrame.reliability = frame.reliability
                newFrame.fragmentIndex = count
                newFrame.body = buffer
                if count > 0:
                    newFrame.reliableIndex = self.reliableIndex
                    self.reliableIndex += 1
                else:
                    newFrame.reliableIndex = frame.reliableIndex
                if newFrame.reliability == Reliability.reliableOrdered == 3:
                    newFrame.orderChannel = frame.orderChannel
                    newFrame.orderedIndex = frame.orderedIndex
                self.addToQueue(newFrame, flags | RakNet.priority["Heap"])
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
