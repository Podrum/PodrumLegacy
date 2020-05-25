#!/usr/bin/env python3
from src.Podrum.Server import Server
from os import getcwd
from threading import Thread

serverThread = Thread(target=Server, args=(getcwd(),))
serverThread.start()
