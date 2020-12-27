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
import hmac
import json
import os
from podrum.utils.Config import Config
import signal
import sys
import socket
from zipfile import ZipFile

class Utils:
    @staticmethod
    def getOS():
        if sys.platform == 'linux' or sys.platform == 'linux2':
            return 'linux'
        if sys.platform == 'darwin':
            return 'osx'
        if sys.platform == 'win32' or sys.platform == 'win64':
            return 'windows'

    @staticmethod
    def enableWindowsFormating():
        from ctypes import windll
        kernel = windll.kernel32
        kernel.SetConsoleMode(kernel.GetStdHandle(-11), 7)

    @staticmethod
    def killServer():
        os.kill(os.getpid(), signal.SIGTERM)

    @staticmethod
    def getPodrumDir():
        return os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + "/../../")

    @staticmethod
    def isPacked():
        if os.path.isfile(Utils.getPodrumDir()):
            return True
        return False

    @staticmethod
    def checkAllFiles():
        path = os.getcwd()
        serverConfig = f"{path}/server.json"
        pluginsFolder = f"{path}/plugins"
        worldsFolder = f"{path}/worlds"
        if not os.path.isfile(serverConfig):
            file = open(serverConfig, "+wb")
            if os.path.isfile(Utils.getPodrumDir()):
                zipFile = ZipFile(Utils.getPodrumDir(), "r")
                file.write(zipFile.read("podrum/resources/server.json"))
            else:
                file2 = open(Utils.getPodrumDir() + "/podrum/resources/server.json", "r")
                file.write(file2.read().encode())
            return False
        if not os.path.isdir(pluginsFolder):
            os.mkdir(pluginsFolder)
        if not os.path.isdir(worldsFolder):
            os.mkdir(worldsFolder)
        return True

    @staticmethod
    def getDefaultConfigFile():
        path = os.getcwd()
        file = open(path + "/server.json", "r+")
        return file

    @staticmethod
    def getDefaultConfig():
        config = Config()
        config.load(Utils.getDefaultConfigFile())
        return config

    @staticmethod
    def encodeJwt(header, payload, verifySigniture):
        body = []
        body.insert(0, base64.b64encode(json.dumps(header).encode()).decode())
        body.insert(1, base64.b64encode(json.dumps(payload).encode()).decode())
        body.insert(2, base64.b64encode(hmac.new(verifySigniture.encode(), ".".join(body).encode(), hashlib.sha256).hexdigest().upper().encode()).decode())
        return ".".join(body)

    @staticmethod
    def decodeJwt(token):
        header, payload, verifySigniture = token.split(".")
        payload += "=="
        json_data = base64.b64decode(payload.replace("-_", "+/")).decode()
        return json.loads(json_data)
