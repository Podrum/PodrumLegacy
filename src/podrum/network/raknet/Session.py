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
from podrum.network.raknet.protocol.FrameSetPacket import FrameSetPacket
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
