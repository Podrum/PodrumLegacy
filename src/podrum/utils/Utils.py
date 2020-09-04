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

import base64
import binascii
import json
import os
import signal
import sys
import socket
import time
import urllib.request
import hmac
import hashlib

class Utils:
    @staticmethod
    def getOS():
        if sys.platform == 'linux' or sys.platform == 'linux2':
            return 'linux'
        elif sys.platform == 'darwin':
            return 'osx'
        elif sys.platform == 'win32' or sys.platform == 'win64':
            return 'windows'
        
    @staticmethod
    def killServer():
        os.kill(os.getpid(), signal.SIGTERM)
    
    @staticmethod
    def getPrivateIpAddress():
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        return ip
    
    @staticmethod
    def getPublicIpAddress():
        ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
        return ip
    
    @staticmethod
    def microtime(get_as_float = False) :
        if get_as_float:
            return time.time()
        else:
            return '%f %d' % math.modf(time.time())
     
    @staticmethod
    def hex2bin(hexdec):
        if hexdec == 'x':
            return False
        if hexdec == '':
            return False
        dec = int(hexdec, 16)
        b = binascii.unhexlify('%x' % dec)
        return b
    
    @staticmethod
    def binToHex(b):
        return binascii.hexlify(b)
    
    @staticmethod
    def bytesToInt(bytes):
        result = 0
        for b in bytes:
            result = result * 256 + int(b)
        return result
    
    @staticmethod
    def intToBytes(value, length):
        result = []
        for i in range(0, length):
            result.append(value >> (i * 8) & 0xff)
        result.reverse()
        return result
    
    @staticmethod
    def HMACSHA256(data, secret):
        encodedData = data.encode()
        byteSecret = secret.encode()
        return hmac.new(byteSecret, encodedData, hashlib.sha256).hexdigest().upper()
    
    @staticmethod
    def base64UrlEncode(data):
        return base64.urlsafe_b64encode(data.encode()).replace(b"=", b"").decode()
    
    @staticmethod
    def base64UrlDecode(data):
        return base64.urlsafe_b64decode(data).decode()
    
    @staticmethod
    def encodeJWT(header, payload, secret):
        body = Utils.base64UrlEncode(json.dumps(header)) + "." + Utils.base64UrlEncode(json.dumps(payload))
        secret = Utils.HMACSHA256(body, secret)
        return body + "." + Utils.base64UrlEncode(secret)
    
    @staticmethod
    def decodeJWT(token: str):
        [headB64, payloadB64, sigB64] = token.split(".")
        rawPayloadJSON = Utils.base64UrlDecode(payloadB64)
        if rawPayloadJSON == False:
            raise Exception("Payload base64 is invalid and cannot be decoded")
        decodedPayload = json.loads(rawPayloadJSON)
        if isinstance(decodedPayload, str):
            decodedPayload = json.loads(decodedPayload)
        if not isinstance(decodedPayload, dict):
            raise Exception("Decoded payload should be dict, " + str(type(decodedPayload).__name__)  + " received")
        return decodedPayload
    
    @staticmethod
    def searchList(lst: list, item):
        i = 0
        length = len(lst)
        while i < length:
            key = lst[i]
            if key == item:
                return True
            else:
                pass
            i += 1
        return False
    
    @staticmethod
    def getKeyInListFromItem(lst: list, item):
        i = 0
        length = len(lst)
        while i < length:
            key = lst[i]
            if key == item:
                return i
            else:
                pass
            i += 1
        return None
