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

from podrum.task.TaskManager import TaskManager
from threading import Thread

class Task(Thread):
    taskObject = None
    taskId = None

    def __init__(self, taskObject, taskId):
        super().__init__()
        self.taskObject = taskObject
        self.taskId = taskId
        self.setDaemon(True)
        self.start()
        TaskManager.addTask(taskId, self)

    def run(self):
        pass
