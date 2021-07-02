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

from collections import deque
import math
from podrum.block.block_map import block_map
from podrum.geometry.vector_2 import vector_2
from podrum.task.immediate_task import immediate_task

class world:
    def __init__(self, provider: object, server: object):
        self.provider: object = provider
        self.server: object = server
        self.chunks: dict = {}
        self.mark_as_loading: object = deque()
        self.world_path: str = provider.world_dir
            
    def load_chunk(self, x: int, z: int) -> None:
        if f"{x} {z}" not in self.mark_as_loading:
            self.mark_as_loading.append(f"{x} {z}")
            chunk: object = self.provider.get_chunk(x, z)
            if chunk is None:
                generator: object = self.server.managers.generator_manager.get_generator(self.get_generator_name())
                chunk: object = generator.generate(x, z, self)
            self.chunks[f"{x} {z}"] = chunk
            self.mark_as_loading.remove(f"{x} {z}")
            
    def load_radius(self, x: int, z: int, radius: int) -> None:
        tasks: list = []
        chunk_x_start: int = (math.floor(x) >> 4) - radius
        chunk_x_end: int = (math.floor(x) >> 4) + radius
        chunk_z_start: int = (math.floor(z) >> 4) - radius
        chunk_z_end: int = (math.floor(z) >> 4) + radius
        for chunk_x in range(chunk_x_start, chunk_x_end):
            for chunk_z in range(chunk_z_start, chunk_z_end):
                if not self.has_loaded_chunk(chunk_x, chunk_z):
                    chunk_task: object = immediate_task(self.load_chunk, [chunk_x, chunk_z])
                    chunk_task.start()
                    tasks.append(chunk_task)
        for task in tasks:
            task.join()
            
    def send_radius(self, x: int, z: int, radius: int, player: object) -> None:
        self.load_radius()
        chunk_x_start: int = (math.floor(x) >> 4) - radius
        chunk_x_end: int = (math.floor(x) >> 4) + radius
        chunk_z_start: int = (math.floor(z) >> 4) - radius
        chunk_z_end: int = (math.floor(z) >> 4) + radius
        for chunk_x in range(chunk_x_start, chunk_x_end):
            for chunk_z in range(chunk_z_start, chunk_z_end):
                if not self.has_loaded_chunk(chunk_x, chunk_z):
                    chunk: object = self.get_chunk(x, z)
                    send_task: object = immediate_task(player.send_chunk, [chunk])
                    send_task.start()
                    tasks.append(send_task)
        for task in tasks:
            task.join()
            
    def unload_chunk(self, x: int, z: int) -> None:
        self.provider.save_chunk(x, z)
        del self.chunks[f"{x} {z}"]
        
    def has_loaded_chunk(self, x: int, z: int) -> bool:
        if f"{x} {z}" in self.chunks:
            return True
        return False
            
    def get_chunk(self, x: int, z: int) -> object:
        return self.chunks[f"{x} {z}"]
        
    def save_chunk(self, x: int, z: int) -> None:
        self.provider.set_chunk(self.get_chunk(x, z))
        
    def get_block(self, x: int, y: int, z: int, block: object) -> None:
        block_and_meta: tuple = block_map.get_name_and_meta(self.chunks[f"{x >> 4} {z >> 4}"].get_block_runtime_id(x & 0x0f, y & 0x0f, z & 0x0f))
        return self.server.managers.block_manager.get_block(block_and_meta[0], block_and_meta[1])
        
    def set_block(self, x: int, y: int, z: int, block: object) -> None:
        self.chunks[f"{x >> 4} {z >> 4}"].set_block_runtime_id(x & 0x0f, y & 0x0f, z & 0x0f, block.runtime_id)
        
    def get_highest_block_at(self, x: int, z: int) -> int:
        return self.chunks[f"{x >> 4} {z >> 4}"].get_highest_block_at(x & 0x0f, z & 0x0f)
        
    def save(self) -> None:
        for chunk in self.chunks.values():
            self.save_chunk(chunk.x, chunk.z)
            
    def get_world_name(self) -> str:
        return self.provider.get_world_name()
        
    def set_world_name(self, world_name: str) -> None:
        self.provider.set_world_name(world_name)
        
    def get_spawn_position(self) -> object:
        return self.provider.get_spawn_position()
        
    def set_spawn_position(self, world_name: object) -> None:
        self.provider.set_spawn_position(world_name)
        
    def get_world_gamemode(self) -> str:
        return self.provider.get_world_gamemode()
        
    def set_world_gamemode(self, world_name: str) -> None:
        self.provider.set_world_gamemode(world_name)
        
    def get_player_position(self, uuid: str) -> object:
        return self.provider.get_player_position(uuid)
        
    def set_player_position(self, uuid: str, position: object) -> None:
        self.provider.set_player_position(uuid, position)

    def get_player_gamemode(self, uuid: str) -> int:
        return self.provider.get_player_gamemode(uuid)
        
    def set_player_gamemode(self, uuid: str, gamemode: int) -> None:
        self.provider.set_player_gamemode(uuid, gamemode)
        
    def create_player(self, uuid: str) -> None:
        self.provider.create_player_file(uuid)
        
    def has_player(self, uuid: str) -> bool:
        return self.provider.has_player_file(uuid)
        
    def get_generator_name(self) -> str:
        return self.provider.get_generator_name()
    
    def set_generator_name(self, generator_name: str) -> None:
        self.provider.set_generator_name(generator_name)
