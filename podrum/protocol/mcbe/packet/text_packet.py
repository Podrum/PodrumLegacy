#########################################################                        
#  ____           _                                     #
# |  _ \ ___   __| |_ __ _   _ _ __ ___                 #
# | |_) / _ \ / _` | '__| | | | '_ ` _ \                #
# |  __/ (_) | (_| | |  | |_| | | | | | |               #
# |_|   \___/ \__,_|_|   \__,_|_| |_| |_|               #
#                                                       #
# Copyright 2021 Podrum Team.                           #
#                                                       #
# This file is licensed under the GPL v2.0 license.     #
# The license file is located in the root directory     #
# of the source code. If not you may not use this file. #
#                                                       #
#########################################################

from podrum.protocol.mcbe.mcbe_protocol_info import mcbe_protocol_info
from podrum.protocol.mcbe.packet.mcbe_packet import mcbe_packet
from podrum.protocol.mcbe.type.text_type import text_type

class text_packet(mcbe_packet):
    def __init__(self, data: bytes = b"", pos: int = 0) -> None:
        super().__init__(data, pos)
        self.packet_id: int = mcbe_protocol_info.text_packet
 
    def decode_payload(self) -> None:
        self.type: int = self.read_unsigned_byte()
        self.needs_translation: bool = self.read_bool()
        if self.type == text_type.chat or self.type == text_type.whisper or self.type == text_type.announcement:
            self.source_name: str = self.read_string()
            self.message: str = self.read_string()
        elif self.type == text_type.raw or self.type == text_type.tip or self.type == text_type.system or self.type == text_type.json or self.type == text_type.json_whisper:
            self.message: str = self.read_string()
        elif self.type == text_type.translation or self.type == text_type.popup or self.type == text_type.jukebox_popup:
            self.message: str = self.read_string()
            self.parameters: list = []
            for i in range(0, self.read_var_int()):
                self.parameters.append(self.read_string())
        self.xuid: str = self.read_string()
        self.platform_chat_id: str = self.read_string()
 
    def encode_payload(self) -> None:
        self.write_unsigned_byte(self.type)
        self.write_bool(self.needs_translation)
        if self.type == text_type.chat or self.type == text_type.whisper or self.type == text_type.announcement:
            self.write_string(self.source_name)
            self.write_string(self.message)
        elif self.type == text_type.raw or self.type == text_type.tip or self.type == text_type.system or self.type == text_type.json or self.type == text_type.json_whisper:
            self.write_string(self.message)
        elif self.type == text_type.translation or self.type == text_type.popup or self.type == text_type.jukebox_popup:
            self.write_string(self.message)
            self.write_var_int(len(self.parameters))
            for parameter in self.parameters:
                self.write_string(parameter)
        self.write_string(self.xuid)
        self.write_string(self.platform_chat_id)
