#!/usr/bin/env python3
"""
*  ____           _
* |  _ \ ___   __| |_ __ _   _ _ __ ___
* | |_) / _ \ / _` | '__| | | | '_ ` _ \
* |  __/ (_) | (_| | |  | |_| | | | | | |
* |_|   \___/ \__,_|_|   \__,_|_| |_| |_|
*
* Licensed under the Apache License, Version 2.0 (the "License")
* you may not use this file except in compliance with the License.
* You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
"""

import sys
import inspect
from os import getcwd, path
from threading import Thread
sys.path.insert(0, path.dirname(path.dirname(path.abspath(inspect.getfile(inspect.currentframe())))))
from podrum.Server import Server

if __name__ == "__main__":
    if len(sys.argv) >= 3:
        if sys.argv[1] == "--no_wizard" and sys.argv[2] == "-travis":
            serverThread = Thread(target=Server, args=(getcwd(), False, True))
        else:
            print("[!] None valid args selected.")
            serverThread = Thread(target=Server, args=(getcwd(), True))
    elif len(sys.argv) == 2:
        if sys.argv[1] == "--no_wizard":
                serverThread = Thread(target=Server, args=(getcwd(), False))
        else:
            print("[!] None valid args selected.")
            serverThread = Thread(target=Server, args=(getcwd(), True))
    else:
        serverThread = Thread(target=Server, args=(getcwd(), True))

    serverThread.start()
