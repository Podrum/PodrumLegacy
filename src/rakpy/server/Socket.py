import socket

class Socket:
    socket = None
    address = None
    
    def __init__(self, address):
        self.address = address
        self.socket = socket.socket(socket.AF_INET if address.version == 4 else socket.AF_INET6, socket.SOCK_DGRAM, socket.SOL_UDP)
        if address.version == 6:
            self.socket.setsockopt(socket.IPPROTO_IPV6, socket.IPV6_V6ONLY, 1)
        try:
            self.socket.bind((self.address.address, self.address.port))
        except socket.error as e:
            print(f"Unable to binto to {str(address.port)}")
            print(str(e))
        try:
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 1024 * 1024 * 8)
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 1024 * 1024 * 8)
        except socket.error:
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
       
    def receiveBuffer(self):
        try:
            return self.socket.recvfrom(65535, 0)
        except socket.error:
            pass
          
    def sendBuffer(self, buffer, address):
        return self.socket.sendto(buffer, address)
    
    def closeSocket(self):
        self.socket.close()
