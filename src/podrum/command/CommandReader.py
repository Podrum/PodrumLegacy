"""
*  ____           _
* |  _ \ ___   __| |_ __ _   _ _ __ ___
* | |_) / _ \ / _` | '__| | | | '_ ` _ \
* |  __/ (_) | (_| | |  | |_| | | | | | |
* |_|   \___/ \__,_|_|   \__,_|_| |_| |_|
*
* Licensed under the Mozilla Public License, Version 2.
* Permissions of this weak copyleft license are conditioned on making
* available source code of licensed files and modifications of those files 
* under the same license (or in certain cases, one of the GNU licenses).
* Copyright and license notices must be preserved. Contributors
* provide an express grant of patent rights. However, a larger work
* using the licensed work may be distributed under different terms and without 
* source code for files added in the larger work.
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
            try:
                line = input("> ")
                if line != "":
                    args = line.split()
                    command = args[0]
                    if CommandManager.isCommand(command):
                        CommandManager.commands[command].execute(self.server, args)
                    else:
                        Logger.error(Base.getTranslation("invalidCommand"))
            except:
                pass
