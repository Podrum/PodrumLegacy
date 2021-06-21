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

import asyncio
from block.block_map import block_map
from config import config
from console.logger import logger
from managers import managers
import os
from protocol.mcbe.rak_net_interface import rak_net_interface
import sys
import time

class server:
    def __init__(self) -> None:
        self.setup_config()
        block_map.load_map()
        self.managers: object = managers(self)
        self.rak_net_interface: object = rak_net_interface(self)
        self.logger: object = logger()
        self.players: dict = {}
        self.current_entity_id: int = 1
        self.event_loop: object = asyncio.get_event_loop()
        self.server_task: object = self.event_loop.create_task(self.start())
        self.event_loop.run_forever()

    def get_plugin_main(self, name):
        if name in self.plugin_manager.plugins:
            return self.plugin_manager.plugins[name]
        
    def get_root_path(self):
        return os.path.abspath(os.path.dirname(__file__))
    
    def setup_config(self) -> None:
        path: str = os.path.join(os.getcwd(), "server.json")
        self.config: object = config(path)
        if "ip_address" not in self.config.data:
            self.config.data["ip_address"]: dict = {}
        if "hostname" not in self.config.data["ip_address"]:
            self.config.data["ip_address"]["hostname"]: str = ".".join(["0"] * 4)
        if "port" not in self.config.data["ip_address"]:
            self.config.data["ip_address"]["port"]: int = 19132
        if "motd" not in self.config.data:
            self.config.data["motd"]: str = "Podrum Server"
        if "max_players" not in self.config.data:
            self.config.data["max_players"]: int = 20
        if "max_view_distance" not in self.config.data:
            self.config.data["max_view_distance"]: int = 8
        if "world_provider" not in self.config.data:
            self.config.data["world_provider"]: int = "anvil"
        if "world_name" not in self.config.data:
            self.config.data["world_name"]: int = "world"
        self.config.save()      

    async def start(self) -> None:
        start_time: float = time.time()
        self.logger.info("Podrum is starting up...")
        plugins_path: str = os.path.join(os.getcwd(), "plugins")
        if not os.path.isfile(plugins_path) and not os.path.isdir(plugins_path):
            os.mkdir(plugins_path)
        await self.managers.plugin_manager.load_all(plugins_path)
        worlds_path: str = os.path.join(os.getcwd(), "worlds")
        if not os.path.isfile(worlds_path) and not os.path.isdir(worlds_path):
            os.mkdir(worlds_path)
        self.managers.world_manager.load_world(self.config.data["world_name"])
        self.world: object = self.managers.world_manager.get_world_from_folder_name(self.config.data["world_name"])
        self.rak_net_interface.start_interface()
        self.console_input_task: object = self.event_loop.create_task(self.console_input())
        finish_time: float = time.time()
        startup_time: float = "%.3f" % (finish_time - start_time)
        self.logger.success(f"Done in {startup_time}. Type help to view all available commands.")
        while True:
            # Add some sort of ticking?
            await asyncio.sleep(0.0001)

    async def stop(self) -> None:
        self.console_input_task.cancel()
        self.rak_net_interface.stop_interface()
        await self.managers.plugin_manager.unload_all()
        self.managers.world_manager.unload_all()
        self.server_task.cancel()
        self.event_loop.stop()
        self.logger.success("Server stopped.")
        os.kill(os.getpid(), 15)

    def send_message(self, message: str) -> None:
        self.logger.info(message)
        
    async def console_input(self) -> None:
        if platform.system() == "Windows":
            import msvcrt
        else:
            import fcntl
            fcntl.fcntl(sys.stdin, fcntl.F_SETFL, fcntl.fcntl(sys.stdin, fcntl.F_GETFL) | os.O_NONBLOCK)
        result: str = ""
        while True:
            if platform.system() == "Windows":
                if msvcrt.kbhit():
                    user_input: str = msvcrt.getch().decode()
                    if user_input == "\b":
                        result = result[0:-1]
                    else:
                        result += user_input
                    if user_input == "\r":
                        print("")
                    else:
                        print("\r\x1b[K" + result, end = "")
                    if result.endswith("\r"):
                        command: str = result[:-1]
                        self.managers.event_manager.call_event("execute_command", command, self, self)
                        result: str = ""
            else:
                result += sys.stdin.read(1)
                if result.endswith("\n"):
                    command: str = result[:-1]
                    self.managers.event_manager.call_event("execute_command", command, self, self)
                    result: str = ""
            await asyncio.sleep(0.0001)
