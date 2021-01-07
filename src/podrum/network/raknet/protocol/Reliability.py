"""
*  ____           _
* |  _ \ ___   __| |_ __ _   _ _ __ ___
* | |_) / _ \ / _` | '__| | | | '_ ` _ \
* |  __/ (_) | (_| | |  | |_| | | | | | |
* |_|   \___/ \__,_|_|   \__,_|_| |_| |_|
*
* Licensed under the Mozilla Public License, Version 2.
* Permissions of this weak copyleft license are conditioned on making
* available source code of licensed files and modifications of those files 
* under the same license (or in certain cases, one of the GNU licenses).
* Copyright and license notices must be preserved. Contributors
* provide an express grant of patent rights. However, a larger work
* using the licensed work may be distributed under different terms and without 
* source code for files added in the larger work.
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
        if reliability == Reliability.reliableSequenced:
            return True
        if reliability == Reliability.reliableAckReceipt:
            return True
        if reliability == Reliability.reliableOrderedAckReceipt:
            return True
            
    @staticmethod
    def isSequenced(reliability):
        if reliability == Reliability.unreliableSequenced:
            return True
        if reliability == Reliability.reliableSequenced:
            return True
       
    @staticmethod
    def isOrdered(reliability):
        if reliability == Reliability.reliableOrdered:
            return True
        if reliability == Reliability.reliableOrderedAckReceipt:
            return True
        if reliability == Reliability.unreliableSequenced:
            return True
        if reliability == Reliability.reliableSequenced:
            return True
