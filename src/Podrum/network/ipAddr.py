import socket
from requests import get

def getPrivateIpAddr():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

def getPublicIpAddr():
    ip = get('https://api.ipify.org').text
    return ip
