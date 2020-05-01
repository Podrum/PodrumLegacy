import socket


def getPublicIpAddr():
    return socket.gethostbyname(socket.gethostname())
