#!/usr/bin/env python3

import sys
sys.path.insert(0, '..') 

from os import getcwd
from threading import Thread
from Podrum.Server import Server

serverThread = Thread(target=Server, args=(getcwd(),))
serverThread.start()
