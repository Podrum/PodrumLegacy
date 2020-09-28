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

class ReaderTracker:
    maxDepth = None
    currentDepth = 0
    
    def __init__(self, maxDepth: int):
        self.maxDepth = maxDepth
        
    def protectDepth(self, execute):
        self.currentDepth += 1
        if self.maxDepth > 0 and self.currentDepth > self.maxDepth:
            raise Exception("Nesting level too deep: reached max depth of " + self.maxDepth + " tags")
        try:
            execute()
        except:
            self.currentDepth -= 1
