class InternetAddress:
    address = None
    port = None
    version = None

    def __init__(self, address: str, port: int, version: int = 4):
        self.address = address
        self.port = port
        self.version = version

    def getAddress(self):
        return self.address

    def getPort(self):
        return self.port

    def getVersion(self):
        return self.version
