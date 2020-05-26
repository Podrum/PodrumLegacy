#!/usr/bin/env python3

import os
os.chdir("..")

from os import getcwd
from threading import Thread
from .Server import Server

serverThread = Thread(target=Server, args=(getcwd(),))
serverThread.start()
