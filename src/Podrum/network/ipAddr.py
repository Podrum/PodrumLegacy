import netifaces

def getPrivateIpAddr():
    netifaces.ifaddresses('eth0')
    ip = netifaces.ifaddresses('eth0')[netifaces.AF_INET][0]['addr']
    print ip
