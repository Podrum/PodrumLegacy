class Reliability:
    unreliable = 0
    unreliableSequenced = 1
    reliable = 2
    reliableOrdered = 3
    reliableSequenced = 4
    unreliableAckReceipt = 5
    reliableAckReceipt = 6
    reliableOrderedAckReceipt = 7
    
    def isReliable(self, reliability):
        if reliability == self.reliable:
            return True
        elif reliability == self.reliableOrdered:
            return True
        elif reliability == self.reliableSequenced:
            return True
        elif reliability == self.reliableAckReceipt:
            return True
        elif reliability == self.reliableOrderedAckReceipt:
            return True
        else:
            return False
        
    def isSequenced(self, reliability):
        if reliability == self.unreliableSequenced:
            return True
        elif reliability == self.reliableSequenced:
            return True
        else:
            return False
        
    def isOrdered(self, reliability):
        if reliability == self.reliableOrdered:
            return True
        elif reliability == self.reliableOrderedAckReceipt:
            return True
        else:
            return False
        
    def isSequencedOrOrdered(self, reliability):
        if reliability == self.unreliableSequenced:
            return True
        elif reliability == self.reliableOrdered:
            return True
        elif reliability == self.reliableSequenced:
            return True
        elif reliability == self.reliableOrderedAckReceipt:
            return True
        else:
            return False
