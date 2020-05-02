import netifaces

def getPrivateIpAddr():
    netifaces.ifaddresses('eth0')
    return netifaces.ifaddresses('eth0')[netifaces.AF_INET][0]['addr']

