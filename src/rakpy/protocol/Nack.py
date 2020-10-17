from rakpy.protocol.AcknowledgePacket import AcknowledgePacket
from rakpy.protocol.PacketIdentifiers import PacketIdentifiers

class Nack(AcknowledgePacket):
    id = PacketIdentifiers.NacknowledgePacket
