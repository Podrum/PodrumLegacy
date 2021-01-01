class Interface:
    def onOpenConnection(self, connection):
        pass
        
    def onCloseConnection(self, address, reason):
        pass
        
    def onEncapsulated(self, packet, address):
        pass
