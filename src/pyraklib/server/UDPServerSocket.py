"""
PyRakLib networking library.
   This software is not affiliated with RakNet or Jenkins Software LLC.
   This software is a port of PocketMine/RakLib <https://github.com/PocketMine/RakLib>.
   All credit goes to the PocketMine Project (http://pocketmine.net)
 
   Copyright (C) 2015  PyRakLib Project

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
import logging
import socket

class UDPServerSocket:

    logger = None
    socket = None

    def __init__(self, logger: logging.Logger, port: int = 19132, interface: str = "0.0.0.0"):
        self.logger = logger
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        try:
            self.socket.bind((interface, port))
        except Exception as e:
            logger.error("FAILED TO BIND TO PORT! Perhaps another server is running on the port?")
            logger.error(str(e))
        finally:
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
            self.socket.setblocking(False) # Non-blocking

    def close(self):
        self.socket.close()

    def readPacket(self):
        try:
            data = self.socket.recvfrom(65535)
            print("Packet IN: "+str(data))
            return data
        except Exception as e:
            pass

    def writePacket(self, buffer, dest, port):
        print("Packet OUT: "+str(buffer))
        return self.socket.sendto(buffer, (dest, port))

