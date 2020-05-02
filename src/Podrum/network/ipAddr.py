import netifaces

def getPublicIpAddr():
    netifaces.ifaddresses('eth0')
    ip = netifaces.ifaddresses('eth0')[netifaces.AF_INET][0]['addr']
    printf ip
