#!/usr/bin/env python3
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

import sys
from podrum.Server import Server

def usage():
    print("Usage: \"python3 -O src/__main__.py [OPTIONS]\"\nAvaiable Options:\n  --no_wizard  Starts the Server without the Wizard")

if __name__ == "__main__":
    if len(sys.argv) == 2:
        if sys.argv[1] == "--no_wizard":
                Server(False)
        else:
            usage()
    else:
        Server(True)
