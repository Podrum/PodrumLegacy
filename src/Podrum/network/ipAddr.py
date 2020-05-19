import socket
import urllib.request

def getPrivateIpAddr():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]


def getPublicIpAddr():
    ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
    return ip
