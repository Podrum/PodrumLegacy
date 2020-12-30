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

from podrum.command.CommandReader import CommandReader
from podrum.command.vanilla.RegisterVanilla import RegisterVanilla
from podrum.GeneralVariables import GeneralVariables
from podrum.lang.Base import Base
from podrum.plugin.Plugin import Plugin
from podrum.utils.Logger import Logger
from podrum.utils.Utils import Utils
from time import time, sleep
from podrum.wizard.Wizard import Wizard

class Server:
    config = None
    ip = None
    port = None
    tickrate = 1000 / 20
    isTicking = True
    players = []
    startTime = None
    endTime = None
    timeDiff = None
    podrumLogo = """
            ____           _                      
           |  _ \ ___   __| |_ __ _   _ _ __ ___  
           | |_) / _ \ / _` | '__| | | | '_ ` _ \ 
           |  __/ (_) | (_| | |  | |_| | | | | | |
           |_|   \___/ \__,_|_|   \__,_|_| |_| |_|
    """

    def __init__(self, withWizard):
        super().__init__()
        self.startTime = time()
        if Utils.getOS() == "windows":
            Utils.enableWindowsFormating()
        if Utils.isPacked():
            print(Utils.getPodrumDir())
            Base.addFromZipDir(Utils.getPodrumDir(), "podrum/lang/languages")
        else:
            Base.addFromDir(Utils.getPodrumDir() + "/" + "podrum/lang/languages")
        if not Utils.checkAllFiles() and withWizard:
            Wizard.start()
            while Wizard.isInWizard:
                pass
        self.config = Utils.getDefaultConfig()
        self.ip = self.config.config["server-ip"]
        self.port = int(self.config.config["server-port"])
        print(str(self.podrumLogo))
        Logger.info(str(Base.getTranslation("startingServer")).replace("{ip}", str(self.ip)).replace("{port}", str(self.port)))
        Logger.info(str(Base.getTranslation("license")))
        RegisterVanilla()
        GeneralVariables.server = self
        GeneralVariables.plugin = Plugin("./plugins", self)
        GeneralVariables.plugin.loadAll()
        self.endTime = time()
        self.timeDiff = "%.3f" % (self.endTime - self.startTime)
        Logger.info(f'Done in {str(self.timeDiff)}s. Type "help" to view all available commands.')
        CommandReader(self)
        while self.isTicking:
            sleep(self.tickrate)

    def sendMessage(self, message):
        Logger.log("info", message)
