import socket

class ServerSocket:
    socket = None
    address = None
    
    def __init__(self, address):
        self.address = address
        self.socket = socket.socket(socket.AF_INET if address.getVersion() == 4 else socket.AF_INET6, socket.SOCK_DGRAM, socket.SOL_UDP)
        if address.getVersion() == 6:
            self.socket.setsockopt(socket.IPPROTO_IPV6, socket.IPV6_V6ONLY, 1)
        try:
            self.socket.bind((self.address.getAddress(), self.address.getPort()))
        except socket.error as e:
            print(f"Unable to binto to {str(address.getPort())}")
            print(str(e))
        else:
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
       
    def receiveBuffer(self):
        data = self.socket.recvfrom(65535, 0)
        print(f"IN -> {data}")
        return data
          
    def sendBuffer(self, buffer, address):
        data = self.socket.sendto(buffer, address)
        print(f"OUT -> {data}")
        return data
      
    def closeSocket(self):
        self.socket.close()
