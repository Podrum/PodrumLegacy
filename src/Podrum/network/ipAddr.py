import socket


def getIpPublicAddr():
    return socket.gethostbyname(socket.gethostname())
