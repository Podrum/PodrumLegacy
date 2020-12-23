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

from podrum.task.Task import Task
from threading import Thread
import time import sleep

class RepeatingTask(Task):
    interval = None
    isRunning = True

    def __init__(self, taskObject, taskId, interval = 0):
        self.interval = interval
        super().__init__(taskObject, taskId)
        
    def stop(self):
        self.isRunning = False

    def run(self):
        while self.isRunning:
            self.taskObject()
            sleep(self.interval)
