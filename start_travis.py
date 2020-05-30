from os import getcwd
from threading import Thread
from src.Podrum.Server import Server
from src.Podrum.utils import Utils

serverThread = Thread(target=Server, args=(getcwd(),))
serverThread.start()
Utils.Utils.killServer()