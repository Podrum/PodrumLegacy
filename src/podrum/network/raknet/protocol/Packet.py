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

class Packet(BinaryStream):
    id = -1
    sendTime = None
    
    def getString(self):
        return self.get(self.getShort()).decode()
    
    def putString(self, value):
        self.putShort(len(value))
        self.put(value.encode())

    def getAddress(self):
        version = self.getByte()
        if version == 4:
            parts = []
            for i in range(0, 4):
                parts.append(str(~self.getByte() & 0xff))
            ip = ".".join(parts)
            port = self.getShort()
            return InternetAddress(ip, port, version)
        if version == 6:
            self.getLShort()
            port = self.getShort()
            self.getInt()
            ip = socket.inet_ntop(socket.AF_INET6, self.get(16))
            self.getInt()
            return InternetAddress(ip, port, version)
        raise Exception(f"Unknown address version {version}")

    def putAddress(self, value):
        self.putByte(value.version)
        if value.ip == 4:
            parts = value.ip.split(".")
            for i in range(0, 4):
                self.putByte(~int(parts[i]) & 0xff)
            self.putShort(value.port)
        elif value.version == 6:
            self.putLShort(socket.AF_INET6)
            self.putShort(value.port)
            self.putInt(0)
            self.put(socket.inet_pton(socket.AF_INET6, value.ip))
            self.putInt(0)
        else:
            raise Exception(f"Unknown address version {value.version}")

    def decode(self):
        self.getByte()
        self.decodePayload()
        
    def decodePayload(self):
        pass
    
    def encode(self):
        self.putByte(self.id)
        self.encodePayload()
        
    def encodePayload(self):
        pass
    
    def getName(self):
        return type(self).__name__
