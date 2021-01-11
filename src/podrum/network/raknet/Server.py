"""
*  ____           _
* |  _ \ ___   __| |_ __ _   _ _ __ ___
* | |_) / _ \ / _` | '__| | | | '_ ` _ \
* |  __/ (_) | (_| | |  | |_| | | | | | |
* |_|   \___/ \__,_|_|   \__,_|_| |_| |_|
*
* Licensed under the Mozilla Public License, Version 2.
* Permissions of this weak copyleft license are conditioned on making
* available source code of licensed files and modifications of those files 
* under the same license (or in certain cases, one of the GNU licenses).
* Copyright and license notices must be preserved. Contributors
* provide an express grant of patent rights. However, a larger work
* using the licensed work may be distributed under different terms and without 
* source code for files added in the larger work.
"""

import os
from podrum.network.raknet.protocol.PacketIdentifiers import PacketIdentifiers
from podrum.network.raknet.protocol.PacketPool import PacketPool
from podrum.network.raknet.RakNet import RakNet
from podrum.network.raknet.Socket import Socket
from threading import Thread
from time import sleep
from time import time

class Server(Thread):
  id = None
  name = None
  socket = None
  interface = None
  sessions = {}
  shutdown = False
  pool = None
  
  def __init__(self, address, interface = None):
    super().__init__()
    self.id = int.from_bytes(os.urandom(4), "little")
    self.socket = Socket(address)
    self.start()
