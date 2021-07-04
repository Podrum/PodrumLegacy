import binascii
from podrum.protocol.mcbe.mcbe_protocol_info import mcbe_protocol_info
from podrum.protocol.mcbe.packet.mcbe_packet import mcbe_packet

class disconnect_packet(mcbe_packet):
    def __init__(self, data: bytes = b"", pos: int = 0) -> None:
        super().__init__(data, pos)
        self.packet_id: int = mcbe_protocol_info.disconnect_packet
        
    def decode_payload(self) -> None:
        self.hide_disconnect_screen: bool = self.read_bool()
        self.message: str = self.read_string()
        
    def encode_payload(self) -> None:
        self.write_bool(self.hide_disconnect_screen)
        self.write_string(self.message)