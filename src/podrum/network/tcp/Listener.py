from copy import deepcopy
from podrum.network.tcp.Interface import Interface
from podrum.network.tcp.Socket import Socket
from threading import Thread

class Listener(Thread):
    address = None
    socket = None
    interface = None
    
    def __init__(self, address, interface = None):
        super().__init__()
        self.address = address
        if interface != None:
            self.interface = interface
        else:
            self.interface = Interface()
        self.start()
        
    def run(self):
        self.socket = deepcopy(Socket(self.address))
        while True:
            try:
                connection, clientAddress = self.socket.socket.accept()
                while True:
                    data = self.socket.receiveBuffer(connection)
                    if data:
                        self.interface.handle(data, connection, clientAddress, self.socket)
                    else:
                        break
            except:
                pass
