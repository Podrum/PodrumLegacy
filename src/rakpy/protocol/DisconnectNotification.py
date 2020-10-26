from rakpy.protocol.Packet import Packet
from rakpy.protocol.PacketIdentifiers import PacketIdentifiers

class DisconnectNotification(Packet):
    id = PacketIdentifiers.DisconnectNotification
