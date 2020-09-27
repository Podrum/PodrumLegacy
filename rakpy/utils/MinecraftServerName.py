class MinecraftServerName:
    edition = ""
    motd = ""
    name = ""
    protocol = 0
    version = ""
    players = {
        "online": 0,
        "max": 0
    }
    gamemode = ""
    serverId = 0
    
    def toString(self):
        return ";".join([
            self.edition,
            self.motd,
            str(self.protocol),
            self.version,
            str(self.players["online"]),
            str(self.players["max"]),
            str(self.serverId),
            self.name,
            self.gamemode
        ]) + ";"
