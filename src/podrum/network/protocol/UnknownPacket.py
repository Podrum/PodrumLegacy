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

from podrum.network.protocol.DataPacket import DataPacket

class UnknownPacket(DataPacket):
    NID = -1

    payload = None
    
    def pid(self):
        if len(self.payload if self.payload else b"") > 0:
            return self.payload[0]
        return self.NID
    
    def getName(self):
        return "unknown packet"

    def decode(self):
        self.payload = self.getRemaining()

    def encode(self):
        self.put(self.payload)
