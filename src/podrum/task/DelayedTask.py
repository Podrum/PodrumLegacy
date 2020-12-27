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
from time import sleep

class DelayedTask(Task):
    delay = None

    def __init__(self, taskObject, taskId, delay):
        self.delay = delay
        super().__init__(taskObject, taskId)

    def run(self):
        sleep(self.delay)
        self.taskObject()
