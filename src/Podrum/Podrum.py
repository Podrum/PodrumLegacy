#!/usr/bin/env python3

from os import getcwd
from threading import Thread
from Server import Server

serverThread = Thread(target=Server, args=(getcwd(),))
serverThread.start()
