"""
*  ____           _
* |  _ \ ___   __| |_ __ _   _ _ __ ___
* | |_) / _ \ / _` | '__| | | | '_ ` _ \
* |  __/ (_) | (_| | |  | |_| | | | | | |
* |_|   \___/ \__,_|_|   \__,_|_| |_| |_|
*
* This program is free software: you can redistribute it and/or modify
* it under the terms of the GNU Lesser General Public License as published by
* the Free Software Foundation, either version 3 of the License, or
* (at your option) any later version.
"""
#!/usr/bin/env python3

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
