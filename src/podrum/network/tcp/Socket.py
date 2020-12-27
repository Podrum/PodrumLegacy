import socket

class Socket:
    socket = None
    address = None
    
    def __init__(self, address):
        self.address = address
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.socket.bind((self.address[0], self.address[1]))
        except socket.error as e:
            print(f"Unable to bind to {str(address[1])}")
            print(str(e))
        self.socket.listen(1)
       
    def receiveBuffer(self, connection):
        try:
            return connection.recv(1446)
        except socket.error:
            return b""
          
    def sendBuffer(self, buffer, connection):
        return connection.send(buffer)
      
    def close(self):
        self.socket.close()
