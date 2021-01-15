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
    
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.floorX = math.floor(x)
        self.floorY = math.floor(y)
        self.floorZ = math.floor(z)
        self.ceilX = math.ceil(x)
        self.ceilY = math.ceil(y)
        self.ceilZ = math.ceil(z)  
