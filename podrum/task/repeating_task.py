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
        self.task_object: object = task_object
        self.args: list = args
        self.interval: int = interval
        self.interval_before: bool = interval_before

    # [start]
    # :return: = None
    # Starts the task
    def start(self) -> None:
        self.is_running: bool = True
        super().start()

    # [stop]
    # :return:
    # Stops the thread
    def stop(self) -> None:
        self.is_running: bool = False

    # [run]
    # :return: = None
    # The main function of the thread.
    def run(self) -> None:
        while self.is_running:
            if self.interval_before:
                sleep(self.interval)
            self.task_object(*self.args)
            if not self.interval_before:
                sleep(self.interval)