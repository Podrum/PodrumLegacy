################################################################################
#                                                                              #
#  ____           _                                                            #
# |  _ \ ___   __| |_ __ _   _ _ __ ___                                        #
# | |_) / _ \ / _` | '__| | | | '_ ` _ \                                       #
# |  __/ (_) | (_| | |  | |_| | | | | | |                                      #
# |_|   \___/ \__,_|_|   \__,_|_| |_| |_|                                      #
#                                                                              #
# Copyright 2021 Podrum Studios                                                #
#                                                                              #
# Permission is hereby granted, free of charge, to any person                  #
# obtaining a copy of this software and associated documentation               #
# files (the "Software"), to deal in the Software without restriction,         #
# including without limitation the rights to use, copy, modify, merge,         #
# publish, distribute, sublicense, and/or sell copies of the Software,         #
# and to permit persons to whom the Software is furnished to do so,            #
# subject to the following conditions:                                         #
#                                                                              #
# The above copyright notice and this permission notice shall be included      #
# in all copies or substantial portions of the Software.                       #
#                                                                              #
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR   #
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,     #
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE  #
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER       #
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING      #
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS #
# IN THE SOFTWARE.                                                             #
#                                                                              #
################################################################################

from protocol.mcbe.mcbe_protocol_info import mcbe_protocol_info
from protocol.mcbe.packet.game_packet import game_packet
from player.mcbe_player import mcbe_player
from rak_net.server import server as rak_net_server
from threading import Thread

class rak_net_interface(Thread):
    def __init__(self, server: object) -> None:
        super().__init__()
        self.server: object = server
        self.rak_net_server: object = rak_net_server(server.config.data["ip_address"]["hostname"], server.config.data["ip_address"]["port"])
        self.rak_net_server.interface: object = self
        self.set_status(server.config.data["motd"], 0, server.config.data["max_players"])

    def get_count(self) -> int:
        name: str = self.rak_net_server.name.split(";")
        return int(name[4])

    def get_max_count(self) -> int:
        name: str = self.rak_net_server.name.split(";")
        return int(name[5])

    def get_motd(self) -> str:
        name: str = self.rak_net_server.name.split(";")
        return name[1]

    def set_status(self, motd: str, count: int, max_count: int) -> None:
        self.rak_net_server.name: str = f"MCPE;{motd};{mcbe_protocol_info.mcbe_protocol_version};{mcbe_protocol_info.mcbe_version};{count};{max_count};0;"

    def set_motd(self, motd: str) -> None:
        self.set_status(motd, self.get_count(), self.get_max_count())

    def set_count(self, count: int) -> None:
        self.set_status(self.get_motd(), count, self.get_max_count())

    def set_max_count(self, max_count: int) -> None:
        self.set_status(self.get_motd(), self.get_count(), max_count)

    def on_frame(self, packet: object, connection: object) -> None:
        if connection.address.token in self.server.players:
            if packet.body[0] == 0xfe:
                new_packet: object = game_packet(packet.body)
                new_packet.decode()
                packets: list = new_packet.read_packets_data()
                for batch in packets:
                    self.server.players[connection.address.token].handle_packet(batch)
            
    def on_new_incoming_connection(self, connection: object) -> None:
        self.server.players[connection.address.token]: object = mcbe_player(connection, self.server, self.server.current_entity_id)
        max_float: float = 3.4028234663852886e+38
        self.server.players[connection.address.token].attributes: list = [
            {"min": 0, "max": max_float, "current": 0, "default": 0, "name": "minecraft:absorbation"},
            {"min": 0, "max": 20, "current": 20, "default": 20, "name": "minecraft:player.saturation"},
            {"min": 0, "max": 5, "current": 0, "default": 0, "name": "minecraft:player.exhaustion"},
            {"min": 0, "max": 1, "current": 0, "default": 0, "name": "minecraft:knockbask_resistance"},
            {"min": 0, "max": 20, "current": 20, "default": 20, "name": "minecraft:health"},
            {"min": 0, "max": max_float, "current": 0.10, "default": 0.10, "name": "minecraft:movement"},
            {"min": 0, "max": 2048, "current": 16, "default": 16, "name": "minecraft:follow_range"},
            {"min": 0, "max": 20, "current": 20, "default": 20, "name": "minecraft:player.hunger"},
            {"min": 0, "max": max_float, "current": 1, "default": 1, "name": "minecraft:attack_damage"},
            {"min": 0, "max": 24791, "current": 0, "default": 0, "name": "minecraft:player.level"},
            {"min": 0, "max": 1, "current": 0, "default": 0, "name": "minecraft:player.experiance"},
            {"min": 0, "max": max_float, "current": 0.02, "default": 0.02, "name": "minecraft:underwater_movement"},
            {"min": -1024, "max": 1024, "current": 0, "default": 0, "name": "minecraft:luck"},
            {"min": 0, "max": max_float, "current": 1, "default": 1, "name": "minecraft:fall_damage"},
            {"min": 0, "max": 2, "current": 0.7, "default": 0.7, "name": "minecraft:horse.jump_strength"},
            {"min": 0, "max": 1, "current": 0, "default": 0, "name": "minecraft:zombie.spawn_reinforcements"},
            {"min": 0, "max": max_float, "current": 0.02, "default": 0.02, "name": "minecraft:lava_movement"}
        ]
        self.server.current_entity_id += 1
        self.set_count(len(self.server.players))
        self.server.logger.info(f"{connection.address.token} connected.")
                   
    def on_disconnect(self, connection: object) -> None:
        del self.server.players[connection.address.token]
        self.set_count(len(self.server.players))
        self.server.logger.info(f"{connection.address.token} disconnected.")

    def start_interface(self) -> None:
        self.stopped: bool = False
        self.start()

    def stop_interface(self) -> None:
        self.stopped: bool = True

    def run(self):
        while not self.stopped:
            self.rak_net_server.handle()
