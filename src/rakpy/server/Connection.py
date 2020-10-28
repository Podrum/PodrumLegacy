from copy import deepcopy
from binutilspy.Binary import Binary
from binutilspy.BinaryStream import BinaryStream
from rakpy.protocol.Ack import Ack
from rakpy.protocol.BitFlags import BitFlags
from rakpy.protocol.ConnectedPing import ConnectedPing
from rakpy.protocol.ConnectedPong import ConnectedPong
from rakpy.protocol.ConnectionRequest import ConnectionRequest
from rakpy.protocol.ConnectionRequestAccepted import ConnectionRequestAccepted
from rakpy.protocol.DataPacket import DataPacket
from rakpy.protocol.EncapsulatedPacket import EncapsulatedPacket
from rakpy.protocol.Nack import Nack
from rakpy.protocol.NewIncomingConnection import NewIncomingConnection
from rakpy.protocol.PacketIdentifiers import PacketIdentifiers
from rakpy.utils.InternetAddress import InternetAddress
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
    windowStart = -1
    windowEnd = 2048
    reliableWindowStart = 0
    reliableWindowEnd = 2048
    reliableWindow = {}
    lastReliableIndex = -1
    receivedWindow = []
    sequenceNumber = 0
    lastSequenceNumber = -1
    sendSequenceNumber = 0
    messageIndex = 0
    channelIndex = []
    needAck = {}
    splitId = 0
    lastUpdate = None
    isActive = False
    
    def __init__(self, server, mtuSize, address):
        self.server = server
        self.mtuSize = mtuSize
        self.address = address
        self.lastUpdate = int(timeNow())
        for i in range(0, 32):
            self.channelIndex.insert(i, 0)
            
    def update(self, timestamp):
        if not self.isActive and (self.lastUpdate + 10000) < timestamp:
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
            for key, pk in enumerate(self.packetToSend):
                pk.sendTime = timestamp
                pk.encode()
                self.recoveryQueue[pk.sequenceNumber] = pk
                del self.packetToSend[key]
                #self.sendPacket(pk) #ToDo
                limit -= 1
                if limit <= 0:
                    break
            if len(self.packetToSend) > 2048:
                self.packetToSend = []
        if len(self.needAck) > 0:
            for identifierACK, indexes in self.needAck.items():
                if len(indexes) == 0:
                    del self.needAck[identifierACK]
                    # Todo add Notify ACK
        for seq, pk in dict(self.recoveryQueue).items():
            if pk.sendTime < (timeNow() - 8):
                self.packetToSend.append(pk)
                del self.recoveryQueue[seq]
        # Should look at that later
        for seq, value in enumerate(self.receivedWindow):
            if seq < self.windowStart:
                del self.receivedWindow[seq]
            else:
                break
        self.sendTheQueue()
        
    def disconnect(self, reason = "unknown"):
        self.server.removeConnection(self, reason)
        
    def receive(self, buffer):
        self.isActive = True
        self.lastUpdate = timeNow()
        header = buffer[0]
        if (header & BitFlags.Valid) == 0:
            return
        if header & BitFlags.Ack:
            return self.handleAck(buffer)
        if header & BitFlags.Nack:
            return self.handleNack(buffer)
        else:
            return self.handleDatagram(buffer)
        
    def handleDatagram(self, buffer):
        dataPacket = DataPacket()
        dataPacket.buffer = buffer
        dataPacket.decode()
        if dataPacket.sequenceNumber < self.windowStart:
            return
        if dataPacket.sequenceNumber > self.windowEnd:
            return
        if dataPacket.sequenceNumber < len(self.receivedWindow):
            return
        diff = dataPacket.sequenceNumber - self.lastSequenceNumber
        if dataPacket.sequenceNumber < len(self.nackQueue):
            del self.nackQueue[dataPacket.sequenceNumber]
        self.ackQueue.append(dataPacket.sequenceNumber)
        self.receivedWindow.append(dataPacket.sequenceNumber)
        if diff != 1:
            i = self.lastSequenceNumber + 1
            while i < dataPacket.sequenceNumber:
                if i not in self.receivedWindow:
                    self.nackQueue.append(i)
                i += 1
        if diff >= 1:
            self.lastSequenceNumber = dataPacket.sequenceNumber
            self.windowStart += diff
            self.windowEnd += diff
        for packet in dataPacket.packets:
            self.receivePacket(packet)
            
    def handleAck(self, buffer):
        packet = Ack()
        packet.buffer = buffer
        packet.decode()
        for seq in packet.packets:
            if seq in self.recoveryQueue:
                for pk in self.recoveryQueue[seq].packets:
                    if isinstance(pk, EncapsulatedPacket) and pk.needAck and pk.messageIndex is not None:
                        del self.needAck[pk.identifierAck]
                del self.recoveryQueue[seq]
                
    def handleNack(self, buffer):
        packet = Nack()
        packet.buffer = buffer
        packet.decode()
        for seq in packet.packets:
            if seq in self.recoveryQueue:
                pk = self.recoveryQueue[seq]
                pk.sequenceNumber = self.sequenceNumber
                self.sequenceNumber += 1
                self.packetToSend.append(pk)
                del self.recoveryQueue[seq]
                
    def receivePacket(self, packet):
        if packet.messageIndex is None:
            self.handlePacket(packet)
        else:
            if packet.messageIndex < self.reliableWindowStart:
                return
            if packet.messageIndex > self.reliableWindowEnd:
                return
            if (packet.messageIndex - self.lastReliableIndex) == 1:
                self.lastReliableIndex += 1
                self.reliableWindowStart += 1
                self.reliableWindowEnd += 1
                self.handlePacket(packet)
                if len(self.reliableWindow) > 0:
                    windows = deepcopy(self.reliableWindow)
                    reliableWindow = {}
                    windows = dict(sorted(windows.items()))
                    for k, v in windows.items():
                        reliableWindow[k] = v
                    self.reliableWindow = reliableWindow
                    for seqIndex, pk in self.reliableWindow:
                        if (seqIndex - self.lastReliableIndex) != 1:
                            break
                        self.lastReliableIndex += 1
                        self.reliableWindowStart += 1
                        self.reliableWindowEnd += 1
                        self.handlePacket(pk)
                        del self.reliableWindow[seqIndex]
            else:
                self.reliableWindow[packet.messageIndex] = packet
                
    def addEncapsulatedToQueue(self, packet, flags = priority["Normal"]):
        packet.needAck = flags & 0b00001000
        if packet.needAck > 0:
            self.needAck[packet.identifierACK] = []
        if 2 <= packet.reliability <= 7:
            packet.messageIndex = self.messageIndex
            self.messageIndex += 1
            if packet.reliability == 3:
                packet.orderIndex = self.channelIndex[packet.orderChannel]
                self.channelIndex[packet.orderChannel] += 1
        if packet.getTotalLength() + 4 > self.mtuSize:
            buffers = []
            for i in range(0, len(packet.buffer), self.mtuSize - 34):
                buffers.append(packet.buffer[i:i - (self.mtuSize - 34)])
            self.splitId += 1
            splitId = self.splitId % 65536
            for count, buffer in enumerate(buffers):
                pk = EncapsulatedPacket()
                pk.splitId = splitId
                pk.split = True
                pk.splitCount = len(buffers)
                pk.reliability = packet.reliability
                pk.splitIndex = count
                pk.buffer = buffer
                if count > 0:
                    pk.messageIndex = self.messageIndex
                    self.messageIndex += 1
                else:
                    pk.messageIndex = packet.messageIndex
                if pk.reliability == 3:
                    pk.orderChannel = packet.orderChannel
                    pk.orderIndex = packet.orderIndex
                self.addToQueue(pk, flags | self.priority["Immediate"])
        else:
            self.addToQueue(packet, flags)
            
    def addToQueue(self, pk, flags = priority["Normal"]):
        priority = flags & 0b0000111
        if pk.needAck and pk.messageIndex is not None:
            self.needAck[pk.identifierAck] = pk.messageIndex
        if priority == self.priority["Immediate"]:
            packet = DataPacket()
            packet.sequenceNumber = self.sendSequenceNumber
            self.sendSequenceNumber += 1
            if pk.needAck:
                packet.packets.append(deepcopy(pk))
                pk.needAck = False
            else:
                packet.packets.append(pk.toBinary())
            self.sendPacket(packet)
            packet.sendTime = timeNow()
            self.recoveryQueue[packet.sequenceNumber] = packet
            return
        length = len(self.sendQueue)
        if (length + pk.getTotalLength()) > self.mtuSize:
            self.sendTheQueue()
        if pk.needAck:
            self.sendQueue.packets.append(deepcopy(pk))
            pk.needACK = False
        else:
            self.sendQueue.packets.append(pk.toBinary())

    def handlePacket(self, packet):
        if packet.split:
            self.handleSplit(packet)
            return
        id = packet.buffer[0]
        dataPacket = None
        pk = None
        sendPacket = None
        if id < 0x80:
            if self.state == self.status["Connecting"]:
                if id == PacketIdentifiers.ConnectionRequest:
                    dataPacket = ConnectionRequest()
                    dataPacket.buffer = packet.buffer
                    dataPacket.decode()
                    pk = ConnectionRequestAccepted()
                    pk.clientAddress = self.address
                    pk.systemIndex = 0
                    pk.requestTime = dataPacket.time
                    pk.time = Binary.flipLongEndianness(int(timeNow())) if Binary.ENDIANNESS == Binary.LITTLE_ENDIAN else int(timeNow())
                    pk.encode()
                    sendPacket = EncapsulatedPacket()
                    sendPacket.reliability = 0
                    sendPacket.buffer = pk.buffer
                    self.addToQueue(sendPacket, self.priority["Immediate"])
                elif id == PacketIdentifiers.NewIncomingConnection:
                    dataPacket = NewIncomingConnection()
                    dataPacket.buffer = packet.buffer
                    dataPacket.decode()
                    serverPort = self.server.socket.address.port
                    if dataPacket.address.port == serverPort:
                        self.state = self.status["Connected"]
                        self.server.interface.onOpenConnection(self)
            elif id == PacketIdentifiers.DisconnectNotification:
                self.disconnect('client disconnect')
            elif id == PacketIdentifiers.ConnectedPing:
                dataPacket = ConnectedPing()
                dataPacket.buffer = packet.buffer
                dataPacket.decode()
                pk = ConnectedPong()
                pk.pingTime = dataPacket.time
                pk.pongTime = Binary.flipLongEndianness(int(timeNow())) if Binary.ENDIANNESS == Binary.LITTLE_ENDIAN else int(timeNow())
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
            for count, packet in enumerate(localSplits):
                BinaryStream.put(packet.buffer)
            del self.splitPackets[packet.splitId]
            pk.buffer = BinaryStream.buffer
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
        self.server.socket.sendBuffer(packet.buffer, (self.address.getAddress(), self.address.getPort()))

    def close(self):
        self.addEncapsulatedToQueue(EncapsulatedPacket.fromBinary('\x00\x00\x08\x15'), self.priority["Immediate"])
