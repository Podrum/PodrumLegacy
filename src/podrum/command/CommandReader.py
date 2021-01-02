"""
*  ____           _
* |  _ \ ___   __| |_ __ _   _ _ __ ___
* | |_) / _ \ / _` | '__| | | | '_ ` _ \
* |  __/ (_) | (_| | |  | |_| | | | | | |
* |_|   \___/ \__,_|_|   \__,_|_| |_| |_|
*
* Licensed under the Apache License, Version 2.0 (the "License")
* you may not use this file except in compliance with the License.
* You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
"""

from podrum.command.CommandManager import CommandManager
from podrum.lang.Base import Base
from podrum.utils.Logger import Logger
from threading import Thread

class CommandReader(Thread):
    server = None
    commandManager = None

    def __init__(self, server):
        super().__init__()
        self.server = server
        self.setDaemon(True)
        self.start()

    def run(self):
        while True:
            line = input()
            if line != "":
                args = line.split()
                command = args[0]
                if CommandManager.isCommand(command):
                    CommandManager.commands[command].execute(self.server, args)
                else:
                    Logger.error(Base.getTranslation("invalidCommand"))
