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

from constant.misc import misc
from constant.vanilla_commands import vanilla_commands
from handler.command_handler import command_handler
from handler.raknet_handler import raknet_handler
from manager.command_manager import command_manager
from manager.event_manager import event_manager
from manager.plugin_manager import plugin_manager
import os
import time
from utils.logger import logger


class server:
    def __init__(self) -> None:
        self.command_manager: object = command_manager(self)
        self.command_handler: object = command_handler(self)
        self.raknet_handler: object = raknet_handler(self, ".".join(["0"] * 4), 19132, "")
        self.event_manager: object = event_manager(self)
        self.logger: object = logger()
        self.plugin_manager: object = plugin_manager(self)
        self.start()

    def register_vanilla_commands(self) -> None:
        self.command_manager.register(vanilla_commands.say, "Say Command")
        self.command_manager.register(vanilla_commands.stop, "Stop Command")
        self.command_manager.register(vanilla_commands.help, "Help Command")
        self.command_manager.register(vanilla_commands.version, "Version Command")
        self.command_manager.register(vanilla_commands.reload, "Reload Command")
        self.command_manager.register(vanilla_commands.plugins, "Plugins Command")

    def get_plugin_main(self, name):
        if name in self.plugin_manager.plugins:
            return self.plugin_manager.plugins[name]
        
    def get_root_path(self):
        return os.path.abspath(os.path.dirname(__file__))

    def start(self) -> None:
        start_time: float = time.time()
        print(misc.logo)
        self.plugin_manager.load_all(misc.plugin_dir)
        self.register_vanilla_commands()
        self.command_handler.start_handler()
        self.raknet_handler.start_handler()
        finish_time: float = time.time()
        startup_time: float = "%.3f" % (finish_time - start_time)
        self.logger.success(f"Done in {startup_time}. Type help to view all available commands.")

    def stop(self) -> None:
        self.raknet_handler.stop_handler()
        self.command_handler.stop_handler()
        self.plugin_manager.unload_all()

    def send_message(self, message: str) -> None:
        self.logger.info(message)
