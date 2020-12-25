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
from threading import Thread
from podrum.Server import Server

def start(withWizard, isTravisBuild = False):
    thread = Thread(target = Server, args = (withWizard, isTravisBuild))
    thread.start()          

if __name__ == "__main__":
    if len(sys.argv) >= 3:
        if sys.argv[1] == "--no_wizard" and sys.argv[2] == "-travis":
            start(False, True)
        else:
            print("[!] None valid args selected.")
            start(True)
    elif len(sys.argv) == 2:
        if sys.argv[1] == "--no_wizard":
                start(False)
        else:
            print("[!] None valid args selected.")
            start(True)
    else:
        start(True))
