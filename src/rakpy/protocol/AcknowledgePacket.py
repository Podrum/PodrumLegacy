from rakpy.protocol.Packet import Packet
from rakpy.protocol.PacketIdentifiers import PacketIdentifiers
from rakpy.utils.BinaryStream import BinaryStream

class AcknowledgePacket(Packet):
    packets = []
    
    def encodePayload(self):
        stream = BinaryStream()
        records = 0
        self.packets.sort()
        if len(self.packets) > 0:
            pointer = 1
            start = self.packets[0]
            last = self.packets[0]
            while pointer < len(self.packets):
                current = self.packets[pointer]
                pointer += 1
                diff = current - last
                if diff == 1:
                    last = current
                elif diff > 1:
                    if start == last:
                        stream.putByte(1)
                        stream.putLTriad(start)
                        start = last = current
                    else:
                        stream.putByte(0)
                        stream.putLTriad(start)
                        stream.putLTriad(last)
                        start = last = current
                    records += 1
            if start == last:
                stream.putByte(1)
                stream.putLTriad(start)
            else:
                stream.putByte(0)
                stream.putLTriad(start)
                stream.putLTriad(last)
            records += 1
        self.putShort(records)
        self.put(stream.buffer)
          
    def decodePayload(self):
        self.packets = []
        recordCount = self.getShort()
        i = 0
        while i < recordCount:
            recordType = self.getByte()
            if recordType == 0:
                start = self.getLTriad()
                end = self.getLTriad()
                current = start
                while current <= end:
                    self.packets.append(current)
                    if len(self.packets) > 4096:
                        raise Exception("Max acknowledgement packet count exceed")
                    current += 1
            else:
                self.packets.append(self.getLTriad())
            i += 1
