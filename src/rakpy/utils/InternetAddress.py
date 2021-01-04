class InternetAddress:
    address = ""
    port = 0
    version = 0

    def __init__(self, address: str, port: int, version: int = 4):
        self.address = address
        self.port = port
        self.version = version
