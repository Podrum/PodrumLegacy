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

from command.help_command import help_command
from command.plugins_command import plugins_command
from command.reload_command import reload_command
from command.say_command import say_command
from command.stop_command import stop_command
from command.version_command import version_command
from constant.misc import misc
from interface.command_interface import command_interface
from interface.rak_net_interface import rak_net_interface
from manager.command_manager import command_manager
from manager.event_manager import event_manager
from manager.plugin_manager import plugin_manager
import os
import time
from utils.logger import logger

class server:
    def __init__(self) -> None:
        self.hostname: str = ".".join(["0", "0", "0", "0"])
        self.port: int = 19132
        self.command_manager: object = command_manager(self)
        self.command_interface: object = command_interface(self)
        self.event_manager: object = event_manager(self)
        self.rak_net_interface: object = rak_net_interface(self)
        self.logger: object = logger()
        self.plugin_manager: object = plugin_manager(self)
        self.players: dict = {}
        self.start()

    def register_vanilla_commands(self) -> None:
        self.command_manager.register(help_command())
        self.command_manager.register(plugins_command())
        self.command_manager.register(reload_command())
        self.command_manager.register(say_command())
        self.command_manager.register(stop_command())
        self.command_manager.register(version_command())
        
    def register_events(self) -> None:
        pass

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
        self.register_events()
        self.command_interface.start_interface()
        self.rak_net_interface.start_interface()
        finish_time: float = time.time()
        startup_time: float = "%.3f" % (finish_time - start_time)
        self.logger.success(f"Done in {startup_time}. Type help to view all available commands.")

    def stop(self) -> None:
        self.rak_net_interface.stop_interface()
        self.command_interface.stop_interface()
        self.plugin_manager.unload_all()

    def send_message(self, message: str) -> None:
        self.logger.info(message)
