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

from podrum.network.raknet.InternetAddress import InternetAddress
from podrum.utils.BinaryStream import BinaryStream
import socket

class Socket:
    address
    socket
    
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
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 1024 * 1024 * 8)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 1024 * 1024 * 8)
        
    def receive(self):
        try:
            buffer, source = self.socket.recvfrom(65535, 0)
            return (BinaryStream(buffer), InternetAddress(source[0], source[1]))
        except socket.error:
            pass
          
    def send(self, stream, address):
        try:
            buffer = stream.buffer
            source = (address.ip, address.port)
            return self.socket.sendto(buffer, source)
        except socket.error:
            pass
    
    def close(self):
        self.socket.close()
