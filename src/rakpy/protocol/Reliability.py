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
