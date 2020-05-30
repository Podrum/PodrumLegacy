from os import getcwd
from threading import Thread
from src.Podrum.Server import Server
from src.Podrum.utils.Utils import serverKill

serverThread = Thread(target=Server, args=(getcwd(),))
serverThread.start()
serverKill()