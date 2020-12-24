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
from podrum.GeneralVariables import GeneralVariables
from podrum.lang.Base import Base
from podrum.network.PacketPool import PacketPool as Pool
from podrum.network.NetworkInterface import NetworkInterface
from podrum.Player import Player
from podrum.plugin.Plugin import Plugin
from podrum.utils.Logger import Logger
from podrum.utils.Utils import Utils
from time import time, sleep
from podrum.wizard.Wizard import Wizard

class Server:
    tickrate = 1000 / 20
    isTicking = True
    addr = "0.0.0.0"
    port = 19132
    players = []
    startTime = None
    endTime = None
    timeDiff = None
    mainInterface = None
    podrumLogo = """
            ____           _                      
           |  _ \ ___   __| |_ __ _   _ _ __ ___  
           | |_) / _ \ / _` | '__| | | | '_ ` _ \ 
           |  __/ (_) | (_| | |  | |_| | | | | | |
           |_|   \___/ \__,_|_|   \__,_|_| |_| |_|
    """

    def __init__(self, withWizard, isTravisBuild = False):
        super().__init__()
        if isTravisBuild:
            exit(0)
        self.startTime = time()
        if Utils.getOS() == "windows":
            Utils.enableWindowsFormating()
        if Utils.isPacked():
            print(Utils.getPodrumDir())
            Base.addFromZipDir(Utils.getPodrumDir(), "podrum/lang/languages")
        else:
            Base.addFromDir(Utils.getPodrumDir() + "/" + "podrum/lang/languages")
        if not Utils.checkAllFiles():
            Wizard.start(self)
            while Wizard.isInWizard:
                pass
        print(str(self.podrumLogo))
        Logger.info(str(Base.getTranslation("startingServer")).replace("{ip}", str(Utils.getPrivateIpAddress())).replace("{port}", str(self.port)))
        Logger.info(str(Base.getTranslation("extIpMsg")).replace("{ipPublic}", str(Utils.getPublicIpAddress())))
        Logger.info(str(Base.getTranslation("license")))
        GeneralVariables.server = self
        GeneralVariables.plugin = Plugin("./plugins", self)
        GeneralVariables.plugin.loadAll()
        self.endTime = time()
        self.mainInterface = NetworkInterface()
        self.timeDiff = "%.3f" % (self.endTime - self.startTime)
        Logger.info(f'Done in {str(self.timeDiff)}s. Type "help" to view all available commands.')
        CommandReader(self)
        while self.isTicking:
            sleep(self.tickrate)
                
    def getLogger(self):
        return Logger()
    
    def getAddress(self):
        return self.addr
    
    def getPort(self):
        return self.port

    def sendMessage(self, message):
        self.getLogger().log("info", message)
