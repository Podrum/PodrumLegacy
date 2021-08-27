r"""
  ____           _
 |  _ \ ___   __| |_ __ _   _ _ __ ___
 | |_) / _ \ / _` | '__| | | | '_ ` _ \
 |  __/ (_) | (_| | |  | |_| | | | | | |
 |_|   \___/ \__,_|_|   \__,_|_| |_| |_|

 Copyright 2021 Podrum Team.

 This file is licensed under the GPL v2.0 license.
 The license file is located in the root directory
 of the source code. If not you may not use this file.
"""


import os
import time
from typing import Optional

from podrum.block.block_map import block_map
from podrum.config import config
from podrum.console.logger import logger
from podrum.item.item_map import item_map
from podrum.managers import managers
from podrum.protocol.mcbe.rak_net_interface import rak_net_interface
from podrum.task.repeating_task import repeating_task
from podrum.world.world_manager import world_manager


class server:

    def __init__(self) -> None:
        self.setup_config()
        item_map.load_map()
        block_map.load_map()

        self.managers = managers(self)
        self.rak_net_interface = rak_net_interface(self)
        self.logger = logger()
        self.players: dict = {}
        self.current_entity_id: int = 1
        self.is_ticking: bool = True
        self.world_manager = world_manager(self)
        self.start()

        self.config: Optional[config] = None

    def get_plugin_main(self, name):
        if name in self.plugin_manager.plugins:
            return self.plugin_manager.plugins[name]
        
    @staticmethod
    def get_root_path():
        return os.path.abspath(os.path.dirname(__file__))

    def __ensure_conf_key(self, expected_key, default):
        if self.config.data.get(expected_key) is None:
            self.config.data[expected_key] = default

    def setup_config(self) -> None:
        path: str = os.path.join(os.getcwd(), "server.json")
        self.config = config(path)

        self.__ensure_conf_key("ip_address", {})
        self.__ensure_conf_key("motd", "Podrum Server")
        self.__ensure_conf_key("max_players", 20)
        self.__ensure_conf_key("max_view_distance", 2)
        self.__ensure_conf_key("world_provider", "anvil")
        self.__ensure_conf_key("world_name", "world")
        self.__ensure_conf_key("world_type", "default")
        self.__ensure_conf_key("seed", 421086205)
        self.__ensure_conf_key("difficulty", 0)

        if "hostname" not in self.config.data["ip_address"]:
            self.config.data["ip_address"]["hostname"] = ".".join(["0"] * 4)

        if "port" not in self.config.data["ip_address"]:
            self.config.data["ip_address"]["port"] = 19132

        self.config.save()      

    def start(self) -> None:
        start_time: float = time.time()
        self.logger.info("Podrum is starting up...")
        plugins_path: str = os.path.join(os.getcwd(), "plugins")

        if not os.path.isfile(plugins_path) and not os.path.isdir(plugins_path):
            os.mkdir(plugins_path)

        self.managers.plugin_manager.load_all(plugins_path)
        worlds_path: str = os.path.join(os.getcwd(), "worlds")

        if not os.path.isfile(worlds_path) and not os.path.isdir(worlds_path):
            os.mkdir(worlds_path)

        self.world_manager.load_world(self.config.data["world_name"])
        self.world: object = self.world_manager.get_world_from_folder_name(self.config.data["world_name"])
        self.rak_net_interface.start_interface()
        self.console_input_task: object = repeating_task(self.console_input)
        self.console_input_task.start()

        finish_time: float = time.time()

        self.logger.success(
            f"Done in {finish_time - start_time:.3f}. "
            f"Type help to view all available commands."
        )

        try:
            while self.is_ticking:
                # Add some sort of ticking?
                for world in self.world_manager.worlds.values():
                    world.set_time(world.time + 1 if world.time <= 23999 else 0)
                time.sleep(0.05)

        except KeyboardInterrupt:
            self.stop()
            
    def dispatch_command(self, user_input: str, sender: object) -> None:
        if len(user_input) <= 0:
            return

        split_input: list = user_input.split()

        try:
            command_name: str = split_input[0]
            command_args: list = split_input[1:]

        except Exception as e:
            return

        if self.managers.command_manager.has_command(command_name):
            self.managers.command_manager.execute(command_name, command_args, sender)

        elif sender == self:
            self.logger.error("Invalid command!")

        else:
            sender.send_message("Invalid command!")

    def stop(self) -> None:
        self.console_input_task.stop()
        self.rak_net_interface.stop_interface()
        self.managers.plugin_manager.unload_all()
        self.managers.world_manager.unload_all()
        self.logger.success("Server stopped.")
        self.is_ticking = False
        os.kill(os.getpid(), 15)

    def send_message(self, message: str) -> None:
        self.logger.info(message)
        
    def broadcast_message(self, message: str) -> None:
        self.send_message(message)

        for player in self.players.values():
            player.send_message(message)
            
    def send_chat_message(self, message: str) -> None:
        self.broadcast_message(f"[Server] {message}")
        
    def console_input(self) -> None:
        try:
            command: str = input()

        except EOFError:
            return

        self.dispatch_command(command, self)

    def find_player(self, username: str):
        usernames = [p.username.lower() for p in self.players.values()]
        players = list(dict(self.players).values())

        for name in usernames:
            if username.lower() == name[:len(username)]:
                return players[usernames.index(name)]

    def broadcast_packet(self, world, packet) -> None:
        for player in list(self.players.values()):
            if player.world == world:
                player.send_packet(packet.data)
