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

class TaskManager:
    tasks = {}
    
    @staticmethod
    def addTask(taskId, taskThread):
        TaskManager.tasks[taskId] = taskThread
        
    @staticmethod
    def removeTask(taskId):
        if taskId in self.tasks:
            del TaskManager.tasks[taskId]
            
    @staticmethod
    def getTask(taskId):
        if taskId in self.tasks:
            return TaskManager.tasks[taskId]
