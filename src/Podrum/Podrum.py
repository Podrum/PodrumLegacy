#!/usr/bin/env python3

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 

from os import getcwd
from threading import Thread
from Podrum.Server import Server

serverThread = Thread(target=Server, args=(getcwd(),))
serverThread.start()
