"""
*  ____           _
* |  _ \ ___   __| |_ __ _   _ _ __ ___
* | |_) / _ \ / _` | '__| | | | '_ ` _ \
* |  __/ (_) | (_| | |  | |_| | | | | | |
* |_|   \___/ \__,_|_|   \__,_|_| |_| |_|
*
* Licensed under the Apache License, Version 2.0 (the "License")
* you may not use this file except in compliance with the License.
* You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
"""

from podrum.network.raknet.utils.InternetAddress import InternetAddress
import socket

class Packet:
    id = None
    sendTime = None
    
    def decodeHeader(self):
        self.getByte()
        
    def decodePayload(self):
        pass
        
    def decode(self):
        self.decodeHeader()
        self.decodePayload()
        
    def encodeHeader(self):
        self.putByte(self.id)
        
    def encodePayload(self):
        pass
        
    def encode(self):
        self.encodeHeader()
        self.encodePayload()
        
    def getString(self):
        return self.get(self.getShort()).decode()
        
    def putString(self, value):
        self.putShort(len(value))
        self.put(value.encode())

    def getAddress(self):
        version = self.getByte()
        if version == 4:
            ipParts = []
            for i in range(0, 4):
                ipParts.append(~self.getByte() & 0xff)
            ip = ".".join(ipParts)
            port = self.getShort()
            return InternetAddress(ip, port, version)
        if version = 6:
            self.getLShort()
            port = self.getShort()
            self.getInt()
            ip = socket.inet_ntop(socket.AF_INET6, self.get(16))
            self.getInt()
            return InternetAddress(ip, port, version)
        
    def putAddress(self, address):
        version = address.version
        ip = address.ip
        port = address.port
        if version == 4:
            ipParts = ip.split(".")
            for ipPart in ipParts:
                self.putByte(~int(part) & 0xff)
            self.putShort(port)
        elif version == 6:
            self.putLShort(self.AF_INET6)
            self.putShort(port)
            self.putInt(0)
            self.put(socket.inet_pton(socket.AF_INET6, ip))
            self.putInt(0)
