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

from threading import Thread
from time import sleep

class repeating_task(Thread):
    def __init__(self, task_object: object, args: list = [], interval: int = 0, interval_before: bool = False) -> None:
        super().__init__()
        self.setDaemon(True)
        self.__task_object: object = task_object
        self.__args: list = args
        self.__interval: int = interval
        self.__interval_before: bool = interval_before

    def start(self) -> None:
        self.__is_running: bool = True
        super().start()

    def stop(self) -> None:
        self.__is_running: bool = False

    def run(self) -> None:
        while self.__is_running:
            if self.__interval_before:
                sleep(self.__interval)
            self.__task_object(*self.__args)
            if not self.__interval_before:
                sleep(self.__interval)
