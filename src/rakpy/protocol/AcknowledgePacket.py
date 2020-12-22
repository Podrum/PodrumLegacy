from binutilspy.Binary import Binary
from rakpy.protocol.Packet import Packet
from rakpy.protocol.PacketIdentifiers import PacketIdentifiers

class AcknowledgePacket(Packet):
    packets = []
    
    def encodePayload(self):
        payload = b""
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
                        payload += Binary.writeByte(1)
                        payload += Binary.writeLTriad(start)
                        start = last = current
                    else:
                        payload += Binary.writeByte(0)
                        payload += Binary.writeLTriad(start)
                        payload += Binary.writeLTriad(last)
                        start = last = current
                    records += 1
            if start == last:
                payload += Binary.writeByte(1)
                payload += Binary.writeLTriad(start)
            else:
                payload += Binary.writeByte(0)
                payload += Binary.writeLTriad(start)
                payload += Binary.writeLTriad(last)
            records += 1
        self.putShort(records)
        self.put(payload)
          
    def decodePayload(self):
        self.packets = []
        recordCount = self.getShort()
        for i in range(0, recordCount):
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
