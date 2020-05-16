from src.Podrum.Server import Server, command
from os import getcwd
from threading import Thread

serverThread = Thread(target=Server, args=(getcwd(),))
serverThread.start()

while True:
    cmd = input('> ')
    command(cmd, True)
    cmd = None