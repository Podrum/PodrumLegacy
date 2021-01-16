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

import math

class Vector3:
    x = None
    y = None
    z = None
    floorX = None
    floorY = None
    floorZ = None
    ceilX = None
    ceilY = None
    ceilZ = None
    absX = None
    absY = None
    absZ = None
    roundX = None
    roundY = None
    roundZ = None
    
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.floorX = int(math.floor(x))
        self.floorY = int(math.floor(y))
        self.floorZ = int(math.floor(z))
        self.ceilX = int(math.ceil(x))
        self.ceilY = int(math.ceil(y))
        self.ceilZ = int(math.ceil(z))
        self.absX = abs(x)
        self.absY = abs(y)
        self.absZ = abs(z)
        self.roundX = round(x)
        self.roundY = round(y)
        self.roundZ = round(z)
