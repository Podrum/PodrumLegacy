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

class Reliability:
    unreliable = 0
    unreliableSequenced = 1
    reliable = 2
    reliableOrdered = 3
    reliableSequenced = 4
    unreliableAckReceipt = 5
    reliableAckReceipt = 6
    reliableOrderedAckReceipt = 7
    
    @staticmethod
    def isReliable(reliability):
        if reliability == Reliability.reliable:
            return True
        if reliability == Reliability.reliableOrdered:
            return True
        if reliability == Reliability.reliableSequenced:
            return True
        return False
        
    @staticmethod
    def isSequenced(reliability):
        if reliability == Reliability.unreliableSequenced:
            return True
        if reliability == Reliability.reliableSequenced:
            return True
        return False
       
    @staticmethod
    def isSequencedOrOrdered(reliability):
        if reliability == Reliability.unreliableSequenced:
            return True
        if reliability == Reliability.reliableOrdered:
            return True
        if reliability == Reliability.reliableSequenced:
            return True
        return False
