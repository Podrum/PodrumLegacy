class ServerInterface:
    @staticmethod
    def onOpenConnection(connection):
        pass
        
    @staticmethod
    def onCloseConnection(address, reason):
        pass
        
    @staticmethod
    def onEncapsulated(packet, address):
        pass
