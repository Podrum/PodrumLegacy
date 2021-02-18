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
    state = RakNet.state["Connecting"]
    channelIndex = [0] * 32
    fragmentId = 0
    sendSequenceNumber = 0
    receivedSequenceNumber = 0
    sendReliableIndex = 0
    receivedReliableIndex = 0
    recoveryQueue = {}
    frameQueue = FrameSetPacket()
    fragmentedPackets = {}
    receivedSequenceNumbers = []

    def __init__(self, server, address, mtuSize):
        self.server = server
        self.address = address
        self.mtuSize = mtuSize
        
    def disconnect(self, reason = "unknown"):
        self.server.removeSession(self.address, reason)
        
    def sendAck(self, sequenceNumber):
        packet = Ack()
        packet.sequenceNumbers = [sequenceNumber]
        self.sendPacket(packet)
        
    def sendNack(self, sequenceNumbers):
        packet = Nack()
        packet.sequenceNumbers = sequenceNumbers
        self.sendPacket(packet)
        
    def sendPacket(self, packet):
        packet.encode()
        self.server.socket.send(packet, self.address)

    def sendFrameQueue(self):
        if len(self.frameQueue.frames) > 0:
            self.frameQueue.sequenceNumber = self.sendSequenceNumber
            self.sendSequenceNumber += 1
            self.sendPacket(self.frameQueue)
            self.recoveryQueue[self.frameQueue.sequenceNumber] = self.frameQueue
            self.frameQueue = FrameSetPacket()
            
    def addToQueue(self, frame, priority = RakNet.priority["Queue"]):
        if priority == RakNet.priority["Heap"]:
            packet = FrameSetPacket()
            packet.sequenceNumber = self.sendSequenceNumber
            self.sendSequenceNumber += 1
            packet.frames.append(frame)
            self.sendPacket(packet)
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
                packet = self.recoveryQueue[sequenceNumber]
                packet.sequenceNumber = self.sendSequenceNumber
                self.sendSequenceNumber += 1
                self.sendPacket(packet)
                del self.recoveryQueue[sequenceNumber]
                
    def handleFrameSetPacket(self, packet):
        if packet.sequenceNumber in self.receivedSequenceNumbers:
            return
        self.sendAck(packet.sequenceNumber)
        self.receivedSequenceNumbers.append(packet.sequenceNumber)
        holeCount = self.receivedSequenceNumber - packet.sequenceNumber
        if holeCount == 0:
            self.receivedSequenceNumber += 1
        else:
            sequenceNumbers = []
            for sequenceNumber in range(self.receivedSequenceNumber + 1, holeCount):
                if sequenceNumber not in self.receivedSequenceNumbers:
                    sequenceNumbers.append(sequenceNumber)
            self.sendNack(sequenceNumbers)
            self.receivedSequenceNumber = packet.sequenceNumber
        for frame in packet.frames:
            self.handleFrame(frame)
            
    def handleFrame(self, frame):
        if not Reliability.isReliable(frame.reliability):
            self.handlePacket(frame)
        else:
            holeCount = self.receivedReliableIndex - frame.reliableIndex
            if holeCount == 0:
                self.handlePacket(frame)
                self.receivedReliableIndex += 1
                
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
                    self.addToQueue(newFrame, RakNet.priority["Heap"])
            elif self.state == RakNet.state["Connected"]:
                self.server.interface.onFrame(frame, self.address)
                
    def close(self):
        self.addToQueue(Frame.fromStream(BinaryStream(b"\x15")), RakNet.priority["Heap"])
