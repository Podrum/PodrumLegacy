r"""
  ____           _
 |  _ \ ___   __| |_ __ _   _ _ __ ___
 | |_) / _ \ / _` | '__| | | | '_ ` _ \
 |  __/ (_) | (_| | |  | |_| | | | | | |
 |_|   \___/ \__,_|_|   \__,_|_| |_| |_|
 Copyright 2021 Podrum Team.
 This file is licensed under the GPL v2.0 license.
 The license file is located in the root directory
 of the source code. If not you may not use this file.
"""
from podrum.command.command_abc import Command
from podrum.protocol.mcbe.packet.transfer_packet import transfer_packet


class transfer_command(Command):

    def __init__(self, server) -> None:
        self.server = server
        self.name: str = "transfer"
        self.description: str = "Transers a player to an other server."

    def execute(self, args: list, sender) -> None:
        if not args:
            sender.send_message("/transfer <ip_address>")
            return
        if hasattr(sender, "username"):
            ip_address: list = args[0].split(":")
            packet: object = transfer_packet()
            packet.address = ip_address[0]
            packet.port = int(ip_address[1])
            packet.encode()
            sender.send_packet(packet.data)
            return
        sender.send_message("Cannot use this command as CONSOLE")
