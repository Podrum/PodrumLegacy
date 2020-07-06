"""
*  ____           _                      
* |  _ \ ___   __| |_ __ _   _ _ __ ___  
* | |_) / _ \ / _` | '__| | | | '_ ` _ \ 
* |  __/ (_) | (_| | |  | |_| | | | | | |
* |_|   \___/ \__,_|_|   \__,_|_| |_| |_|
*
* This program is free software: you can redistribute it and/or modify
* it under the terms of the GNU Lesser General Public License as published by
* the Free Software Foundation, either version 3 of the License, or
* (at your option) any later version.
"""
import base64
import binascii
import json
import os
import signal
import sys
import socket
import time
import urllib
import hmac
import hashlib

class Utils:

    def getOS():
        if sys.platform == 'linux' or sys.platform == 'linux2':
            return 'linux'
        elif sys.platform == 'darwin':
            return 'osx'
        elif sys.platform == 'win32' or sys.platform == 'win64':
            return 'windows'
        
    def killServer():
        os.kill(os.getpid(), signal.SIGTERM)
    
    def getPrivateIpAddress():
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        return ip
    
    def getPublicIpAddress():
        ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
        return ip
    
    def microtime(get_as_float = False) :
        if get_as_float:
            return time.time()
        else:
            return '%f %d' % math.modf(time.time())
        
    def substr(string, start, length = None):
        if start < 0:
            start = start + len(string)
        if not length:
            return string[start:]
        elif length > 0:
            return string[start:start + length]
        else:
            return string[start:length]
        
    def hex2bin(hexdec):
        if hexdec == 'x':
            return False
        if hexdec == '':
            return False
        dec = int(hexdec, 16)
        b = binascii.unhexlify('%x' % dec)
        return b
    
    def binToHex(b):
        return binascii.hexlify(b)
    
    def HMACSHA256(data, secret):
        encodedData = data.encode()
        byteSecret = secret.encode()
        return hmac.new(byteSecret, encodedData, hashlib.sha256).hexdigest().upper()
    
    def base64UrlEncode(data):
        return base64.b64encode(data.encode("utf-8")).decode("utf-8").translate(str.maketrans('+/', '-_')).rstrip("=")
    
    def base64UrlDecode(data):
        return base64.b64decode(data.translate(str.maketrans('-_', '+/'))).decode("utf-8")
    
    def encodeJWT(header, payload, secret):
        body = Utils.base64UrlEncode(json.dumps(header)) + "." + Utils.base64UrlEncode(json.dumps(payload))
        secret = Utils.HMACSHA256(body, secret)
        return str(body) + "." + str(secret)
    
    def decodeJWT(token: str):
        [headB64, payloadB64, sigB64] = token.split(".")
        rawPayloadJSON = Utils.base64UrlDecode(payloadB64)
        if rawPayloadJSON == False:
            raise Exception("Payload base64 is invalid and cannot be decoded")
        decodedPayload = json.loads(rawPayloadJSON)
        if not isinstance(decodedPayload, (list, dict, tuple)):
            raise Exception("Decoded payload should be array, " + str(type(decodedPayload).__name__)  + " received")
        return decodedPayload
