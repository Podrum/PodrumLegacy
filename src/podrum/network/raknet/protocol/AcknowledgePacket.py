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

from podrum.network.raknet.protocol.Packet import Packetfrom podrum.network.raknet.protocol.Packet import Packet

class AcknowledgePacket:
    def decodePayload(self):
        self.packets = []
        recordCount = self.getShort()
        for i in range(0, recordCount):
            recordType = self.getByte()
            if recordType == 0:
                start = self.getLTriad()
                end = self.getLTriad()
                for packet in range(start, end + 1):
                    self.packets.append(packet)
                    if len(self.packets) > 4096:
                        raise Exception("Maximum acknowledgement packets size exceeded")
            else:
                packet = self.getLTriad()
                self.packets.append(packet)
