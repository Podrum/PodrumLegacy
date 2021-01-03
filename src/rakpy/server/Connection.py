from rakpy.protocol.Ack import Ack
from rakpy.protocol.ConnectedPing import ConnectedPing
from rakpy.protocol.ConnectedPong import ConnectedPong
from rakpy.protocol.ConnectionRequest import ConnectionRequest
from rakpy.protocol.ConnectionRequestAccepted import ConnectionRequestAccepted
from rakpy.protocol.DataPacket import DataPacket
from rakpy.protocol.EncapsulatedPacket import EncapsulatedPacket
from rakpy.protocol.Nack import Nack
from rakpy.protocol.NewIncomingConnection import NewIncomingConnection
from rakpy.protocol.PacketIdentifiers import PacketIdentifiers
from rakpy.protocol.Reliability import Reliability
from rakpy.utils.InternetAddress import InternetAddress
from rakpy.utils.BinaryStream import BinaryStream
from time import time as timeNow

class Connection:
    priority = {
        "Normal": 0,
        "Immediate": 1
    }

    status = {
        "Connecting": 0,
        "Connected": 1,
        "Disconnecting": 2,
        "Disconnected": 3
    }
    
    server = None
    mtuSize = None
    address = None
    state = status["Connecting"]
    nackQueue = []
    ackQueue = []
    recoveryQueue = {}
    packetToSend = []
    sendQueue = DataPacket()
    splitPackets = {}
    lastReliableIndex = 0
    lastSequenceNumber = -1
    sendSequenceNumber = 0
    messageIndex = 0
    channelIndex = []
    splitId = 0
    lastUpdate = None
    isActive = False
    
    def __init__(self, server, mtuSize, address):
        self.server = server
        self.mtuSize = mtuSize
        self.address = address
        self.lastUpdate = int(timeNow())
        self.channelIndex = [0] * 32
            
    def update(self, timestamp):
        if not self.isActive and (self.lastUpdate + 10) < timestamp:
            self.disconnect("timeout")
            return
        self.isActive = False
        if len(self.ackQueue) > 0:
            pk = Ack()
            pk.packets = self.ackQueue
            self.sendPacket(pk)
            self.ackQueue = []
        if len(self.nackQueue) > 0:
            pk = Nack()
            pk.packets = self.nackQueue
            self.sendPacket(pk)
            self.nackQueue = []
        if len(self.packetToSend) > 0:
            limit = 16
            for count, pk in enumerate(self.packetToSend):
                pk.sendTime = timestamp
                pk.encode()
                self.recoveryQueue[pk.sequenceNumber] = pk
                del self.packetToSend[count]
                self.sendPacket(pk)
                limit -= 1
                if limit <= 0:
                    break
            if len(self.packetToSend) > 2048:
                self.packetToSend = []
        for seq, pk in dict(self.recoveryQueue).items():
            if pk.sendTime < (timeNow() - 8):
                self.packetToSend.append(pk)
                del self.recoveryQueue[seq]
        self.sendTheQueue()
        
    def disconnect(self, reason = "unknown"):
        self.server.removeConnection(self, reason)
        
    def receive(self, buffer):
        self.isActive = True
        self.lastUpdate = timeNow()
        header = buffer[0]
        if (header & 0x80) == 0:
            return
        if header & 0x40:
            return self.handleAck(buffer)
        if header & 0x20:
            return self.handleNack(buffer)
        return self.handleDatagram(buffer)
        
    def handleDatagram(self, buffer):
        dataPacket = DataPacket()
        dataPacket.buffer = buffer
        dataPacket.decode()
        if dataPacket.sequenceNumber in self.receivedWindow:
            return
        if dataPacket.sequenceNumber in self.nackQueue:
            self.nackQueue.remove(dataPacket.sequenceNumber)
        self.ackQueue.append(dataPacket.sequenceNumber)
        self.receivedWindow.append(dataPacket.sequenceNumber)
        diff = dataPacket.sequenceNumber - self.lastSequenceNumber
        if diff != 1:
            i = self.lastSequenceNumber + 1
            while i < dataPacket.sequenceNumber:
                if i not in self.receivedWindow:
                    self.nackQueue.append(i)
                i += 1
        if diff >= 1:
            self.lastSequenceNumber = dataPacket.sequenceNumber
        for packet in dataPacket.packets:
            self.receivePacket(packet)
            
    def handleAck(self, buffer):
        packet = Ack()
        packet.buffer = buffer
        packet.decode()
        for seq in packet.packets:
            if seq in self.recoveryQueue:
                del self.recoveryQueue[seq]
                
    def handleNack(self, buffer):
        packet = Nack()
        packet.buffer = buffer
        packet.decode()
        for seq in packet.packets:
            if seq in self.recoveryQueue:
                pk = self.recoveryQueue[seq]
                pk.sequenceNumber = self.sendSequenceNumber
                self.sendSequenceNumber += 1
                pk.sendTime = timeNow()
                pk.encode()
                self.sendPacket(pk)
                del self.recoveryQueue[seq]
                
    def receivePacket(self, packet):
        if not Reliability.isReliable(packet.reliability):
            self.handlePacket(packet)
        else:
            holeCount = self.lastReliableIndex - packet.messageIndex
            if holeCount == 0:
                self.handlePacket(packet)
                self.lastReliableIndex += 1
                
    def addEncapsulatedToQueue(self, packet, flags = priority["Normal"]):
        if Reliability.isReliable(packet.reliability):
            packet.messageIndex = self.messageIndex
            self.messageIndex += 1
            if packet.reliability == Reliability.reliableOrdered:
                packet.orderIndex = self.channelIndex[packet.orderChannel]
                self.channelIndex[packet.orderChannel] += 1
        if packet.getTotalLength() > self.mtuSize:
            buffers = {}
            i = 0
            splitIndex = 0
            while i < len(packet.buffer):
                buffers[splitIndex] = packet.buffer[i:i + self.mtuSize]
                splitIndex += 1
                i += self.mtuSize
            for index, buffer in buffers.items():
                pk = EncapsulatedPacket()
                pk.splitId = self.splitId
                pk.splitCount = len(buffers)
                pk.reliability = packet.reliability
                pk.splitIndex = index
                pk.buffer = buffer
                if index != 0:
                    pk.messageIndex = self.messageIndex
                    self.messageIndex += 1
                if pk.reliability == 3:
                    pk.orderChannel = packet.orderChannel
                    pk.orderIndex = packet.orderIndex
                self.addToQueue(pk, flags)
            self.splitId += 1
        else:
            self.addToQueue(packet, flags)
            
    def addToQueue(self, pk, flags = priority["Normal"]):
        priority = flags & 0b1
        if priority == self.priority["Immediate"]:
            packet = DataPacket()
            packet.sequenceNumber = self.sendSequenceNumber
            self.sendSequenceNumber += 1
            packet.packets.append(pk)
            self.sendPacket(packet)
            packet.sendTime = timeNow()
            self.recoveryQueue[packet.sequenceNumber] = packet
            return
        length = self.sendQueue.length()
        if (length + pk.getTotalLength()) > self.mtuSize:
            self.sendTheQueue()
        self.sendQueue.packets.append(pk)

    def handlePacket(self, packet):
        if packet.splitCount > 0:
            self.handleSplit(packet)
            return
        pid = packet.buffer[0]
        dataPacket = None
        pk = None
        sendPacket = None
        if pid < 0x80:
            if self.state == self.status["Connecting"]:
                if pid == PacketIdentifiers.ConnectionRequest:
                    dataPacket = ConnectionRequest()
                    dataPacket.buffer = packet.buffer
                    dataPacket.decode()
                    pk = ConnectionRequestAccepted()
                    pk.clientAddress = self.address
                    pk.systemIndex = 0
                    pk.requestTime = dataPacket.time
                    pk.time = int(timeNow())
                    pk.encode()
                    sendPacket = EncapsulatedPacket()
                    sendPacket.reliability = 0
                    sendPacket.buffer = pk.buffer
                    self.addToQueue(sendPacket, self.priority["Immediate"])
                elif pid == PacketIdentifiers.NewIncomingConnection:
                    dataPacket = NewIncomingConnection()
                    dataPacket.buffer = packet.buffer
                    dataPacket.decode()
                    serverPort = self.server.socket.address.port
                    if dataPacket.address.port == serverPort:
                        self.state = self.status["Connected"]
                        self.server.interface.onOpenConnection(self)
            elif pid == PacketIdentifiers.DisconnectNotification:
                self.disconnect('client disconnect')
            elif pid == PacketIdentifiers.ConnectedPing:
                dataPacket = ConnectedPing()
                dataPacket.buffer = packet.buffer
                dataPacket.decode()
                pk = ConnectedPong()
                pk.pingTime = dataPacket.time
                pk.pongTime = int(timeNow())
                pk.encode()
                sendPacket = EncapsulatedPacket()
                sendPacket.reliability = 0
                sendPacket.buffer = pk.buffer
                self.addToQueue(sendPacket)
        elif self.state == self.status["Connected"]:
            self.server.interface.onEncapsulated(packet, self.address)
    
    def handleSplit(self, packet):
        if packet.splitId in self.splitPackets:
            value = self.splitPackets[packet.splitId]
            value[packet.splitIndex] = packet
            self.splitPackets[packet.splitId] = value
        else:
            self.splitPackets[packet.splitId] = {packet.splitIndex: packet}
        localSplits = self.splitPackets[packet.splitId]
        if len(localSplits) == packet.splitCount:
            pk = EncapsulatedPacket()
            stream = BinaryStream()
            for index, value in localSplits.items():
                stream.put(value.buffer)
            del self.splitPackets[packet.splitId]
            pk.buffer = stream.buffer
            self.receivePacket(pk)
    
    def sendTheQueue(self):
        if len(self.sendQueue.packets) > 0:
            self.sendQueue.sequenceNumber = self.sendSequenceNumber
            self.sendSequenceNumber += 1
            self.sendPacket(self.sendQueue)
            self.sendQueue.sendTime = timeNow()
            self.recoveryQueue[self.sendQueue.sequenceNumber] = self.sendQueue
            self.sendQueue = DataPacket()
            
    def sendPacket(self, packet):
        packet.encode()
        self.server.socket.sendBuffer(packet.buffer, (self.address.address, self.address.port))

    def close(self):
        self.addEncapsulatedToQueue(EncapsulatedPacket.fromBinary(BinaryStream(b"\x00\x00\x08\x15")), self.priority["Immediate"])
