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

from constant.version import version
import os

class vanilla_commands:
    @staticmethod
    def say(args: list, sender: object, server: object) -> None:
        if len(args) > 0:
            sender.send_message(" ".join(args))
        else:
            sender.send_message("say <message>")

    @staticmethod
    def stop(args: list, sender: object, server: object) -> None:
        sender.send_message("Stopping server...")
        server.stop()
        sender.send_message("Server stopped.")
        os.kill(os.getpid(), 15)
        
    @staticmethod
    def help(args: list, sender: object, server: object) -> None:
        sender.send_message("--- Showing help ---")
        for name, info in dict(server.command_manager.commands).items():
            sender.send_message(f"/{name}: {info['description']}")
          
    @staticmethod
    def version(args: list, sender: object, server: object) -> None:
        sender.send_message(f"This server is running Podrum version {version.podrum_version} {version.podrum_codename} on API {version.podrum_api_version} for mcbe {version.mcbe_version} ({version.mcbe_protocol_version}). This version is licensed under the {version.podrum_license} license.")

    @staticmethod
    def reload(args: list, sender: object, server: object) -> None:
        sender.send_message("Reloading...")
        server.plugin_manager.reload_all()
        sender.send_message("Successfully reloaded.")
                                
    @staticmethod
    def plugins(args: list, sender: object, server: object) -> None:
        sender.send_message(f"Plugins({len(server.plugin_manager.plugins)}): {', '.join(server.plugin_manager.plugins)}")
