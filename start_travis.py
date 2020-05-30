from os import getcwd
from threading import Thread
from src.Podrum.Server import Server
from .src.Podrum.utils.Utils import killServer

if __name__ == "__main__":
    serverThread = Thread(target=Server, args=(getcwd(),))
    serverThread.start()