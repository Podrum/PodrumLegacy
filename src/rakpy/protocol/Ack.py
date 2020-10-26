from rakpy.protocol.AcknowledgePacket import AcknowledgePacket
from rakpy.protocol.PacketIdentifiers import PacketIdentifiers

class Ack(AcknowledgePacket):
    id = PacketIdentifiers.AcknowledgePacket
