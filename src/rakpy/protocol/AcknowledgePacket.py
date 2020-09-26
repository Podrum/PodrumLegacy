from binutilspy.Binary import Binary
from rakpy.protocol.Packet import Packet
from rakpy.protocol.PacketIdentifiers import PacketIdentifiers

class AcknowledgePacket(Packet):
    packets = []
    
    def encodePayload(self):
        payload = b""
        records = 0
        self.packets.sort(key=int)
        count = len(self.packets)
        if count > 0:
            pointer = 1
            start = self.packets[0]
            last = self.packets[0]
            while pointer < count:
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
        count = self.getShort()
        cnt = 0
        i = 0
        while i < count and not self.feof() and cnt < 4096:
            recordType = self.getByte()
            if recordType == 0:
                start = self.getLTriad()
                end = self.getLTriad()
                if (end - start) > 512:
                    end = start + 512
                c = start
                while c <= end:
                    self.packets.insert(cnt, c)
                    cnt += 1
                    c += 1
            else:
                self.packets.insert(cnt, self.getLTriad())
                cnt += 1
