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

from podrum.math.AxisAlignedBB import AxisAlignedBB
from podrum.math.Vector3 import Vector3

class RaycastResult:
    bb = None
    hitFace = None
    hitVector = None

    def __init__(self, bb, hitFace, hitVector):
        bb = AxisAlignedBB()
        hitVector = Vector3()
        self.bb = bb
        self.hitFace = hitFace
        self.hitVector = hitVector

    def getBoundingBox(self):
        return self.bb

    def getHitFace(self):
        return self.hitFace

    def getHitVector(self):
        return self.hitVector
