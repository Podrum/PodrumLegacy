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
from podrum.math.Facing import Facing
from podrum.math.RayTraceResult import RayTraceResult
from podrum.math.Vector3 import Vector3

class AxisAlignedBB:
    minX = None
    minY = None
    minZ = None
    maxX = None
    maxY = None
    maxZ = None

    def __init__(self, minX, minY, minZ, maxX, maxY, maxZ):
        if minX > maxX:
            raise ValueError("minX is larger than maxX")
        if minY > maxY:
            raise ValueError("minY is larger than maxY")
        if minZ > maxZ:
            raise ValueError("minZ is larger than maxZ")
        self.minX = minX
        self.minY = minY
        self.minZ = minZ
        self.maxX = maxX
        self.maxY = maxY
        self.maxZ = maxZ

    def addCoord(self, x, y, z):
        minX = self.minX
        minY = self.minY
        minZ = self.minZ
        maxX = self.maxX
        maxY = self.maxY
        maxZ = self.maxZ

        if x < 0:
            minX += x
        elif x > 0:
            maxX += x

        if y < 0:
            minY += y
        elif y > 0:
            maxY += y

        if z < 0:
            minZ += z
        elif z > 0:
            maxZ += z

    def expand(self, x, y, z):
        self.minX -= x
        self.minY -= y
        self.minZ -= z
        self.maxX += x
        self.maxY += y
        self.maxZ += z

        return self

    def expandedCopy(self, x, y, z):
        clone = self()
        return clone.expand(x, y, z)

    def offset(self, x, y, z):
        self.minX += x
        self.minY += y
        self.minZ += z
        self.maxX += x
        self.maxY += y
        self.maxZ += z

        return self

    def offsetCopy(self, x, y, z):
        clone = self()
        return clone.offset(x, y, z)

    def contract(self, x, y, z):
        self.minX += x
        self.minY += y
        self.minZ += z
        self.maxX -= x
        self.maxY -= y
        self.maxZ -= z

        return self

    def contractedCopy(self, x, y, z):
        clone = self()
        return clone.contract(x, y, z)

    def extend(self, face, distance):
        if face == Facing.DOWN:
            self.minY -= distance
        elif face == Facing.UP:
            self.maxY += distance
        elif face == Facing.NORTH:
            self.minZ -= distance
        elif face == Facing.SOUTH:
            self.maxZ += distance
        elif face == Facing.WEST:
            self.minX -= distance
        elif face == Facing.EAST:
            self.maxX += distance
        else:
            raise ValueError("Invalid face")

        return self

    def extendedCopy(self, face, distance):
        clone = self()
        return clone.extend(face, distance)

    def trim(self, face, distance):
        return self.extend(face, -distance)

    def trimmedCopy(self, face, distance):
        clone = self()
        return clone.extendedCopy(face, -distance)

    def stretch(self, axis, distance):
        if axis == Facing.AXIS_Y:
            self.minY -= distance
            self.maxY += distance
        elif axis == Facing.AXIS_Z:
            self.minZ -= distance
            self.maxZ += distance
        elif axis == Facing.AXIS_X:
            self.minX -= distance
            self.maxX += distance
        else:
            raise ValueError("Invalid axis")

    def stretchedCopy(self, axis, distance):
        clone = self()
        return clone.stretch(axis, distance)

    def squash(self, axis, distance):
        return self.stretch(axis, -distance)

    def squashedCopy(self, axis, distance):
        return self.stretchedCopy(axis, -distance)

    def calculateXOffset(self, bb, x):
        bb = self()
        if bb.maxY <= self.minY or bb.minY >= self.maxY:
            return x
        if bb.maxZ <= self.minZ or bb.minZ >= self.maxZ:
            return x

        if x > 0 and bb.maxX <= self.minX:
            x1 = self.minX - bb.maxX
            if x1 < x:
                x = x1
        elif x < 0 and bb.minX >= self.maxX:
            x2 = self.maxX - bb.minX
            if x2 > x:
                x = x2

        return x

    def calculateYOffset(self, bb, y):
        bb = self()
        if bb.maxX <= self.minX or bb.minX >= self.maxX:
            return y
        if bb.maxZ <= self.minZ or bb.minZ >= self.maxZ:
            return y
        if y > 0 and bb.maxY <= self.minY:
            y1 = self.minY - bb.maxY
            if y1 < y:
                y = y1
        elif y < 0 and bb.minY >= self.maxY:
            y2 = self.maxY - bb.minY
            if y2 > y:
                y = y2

        return y

    def calculateZOffset(self, bb, z):
        bb = self()
        if bb.maxX <= self.minX or bb.minX >= self.maxX:
            return z
        if bb.maxY <= self.minY or bb.minY >= self.maxY:
            return z
        if z > 0 and bb.maxZ <= self.minZ:
            z1 = self.minZ - bb.maxZ
            if x1 < z:
                z = z2
        elif z < 0 and bb.minZ >= self.maxZ:
            x2 = self.maxZ - bb.minZ
            if x2 > z:
                z = z2

        return z

    def intersectsWith(self, bb, epsilon = 0.00001):
        bb = self()
        if bb.maxX - self.minX > epsilon and self.maxX - bb.minX > epsilon:
            if bb.maxY - self.minY > epsilon and self.maxY - bb.minY > epsilon:
                return bb.maxZ - self.minZ > epsilon and self.maxZ - bb.minZ > epsilon

        return False

    def isVectorInside(self, vector):
        vector = Vector3()
        if vector.x <= self.minX or vector.x >= self.maxX:
            return False
        if vector.y <= self.minY or vector.y >= self.maxY:
            return False

        return vector.z > self.minZ and vector.z < self.maxZ

    def getAverageEdgeLength(self):
        return (self.maxX - self.minX + self.maxY - self.minY + self.maxZ - self.minZ) / 3

    def getXLength(self):
        return self.maxX - self.minX

    def getYLength(self):
        return self.maxY - self.minY

    def getZLength(self):
        return self.maxZ - self.minZ

    def isCube(self, epsilon = 0.000001):
        xLen = self.getXLength()
        yLen = self.getYLength()
        zLen = self.getZLength()
        return abs(xLen - yLen) < epsilon and abs(yLen - zLen) < epsilon

    def getVolume(self):
        return (self.maxX - self.minX) * (self.maxY - self.minY) * (self.maxZ - self.minZ)

    def isVectorInXZ(self, vector):
        vector = Vector3()
        return vector.y >= self.minY and vector.y <= self.maxY and vector.z >= self.minZ and vector.z <= self.maxZ

    def isVectorInXZ(self, vector):
        vector = Vector3()
        return vector.x >= self.minX and vector.x <= self.maxX and vector.z >= self.minZ and vector.z <= self.maxZ

    def isVectorInXY(self, vector):
        vector = Vector3()
        return vector.x >= self.minX and vector.x <= self.maxX and vector.y >= self.minY and vector.y <= self.maxY

    def calculateIntercept(self, pos1, pos2):
        pos1 = Vector3()
        pos2 = Vector3()
        v1 = pos1.getIntermediateWithXValue(pos2, self.minX)
        v2 = pos1.getIntermediateWithXValue(pos2, self.maxX)
        v3 = pos1.getIntermediateWithYValue(pos2, self.minY)
        v4 = pos1.getIntermediateWithYValue(pos2, self.maxY)
        v5 = pos1.getIntermediateWithZValue(pos2, self.minZ)
        v6 = pos1.getIntermediateWithZValue(pos2, self.maxY)

        if v1 != None and not self.isVectorYZ(v1):
            v1 = None

        if v2 != None and not self.isVectorYZ(v2):
            v2 = None

        if v3 != None and not self.isVectorXZ(v3):
            v3 = None

        if v4 != None and not self.isVectorXZ(v4):
            v4 = None

        if v5 != None and not self.isVectorXY(v5):
            v5 = None

        if v6 != None and not self.isVectorXY(v6):
            v6 = None

        vector = None
        distance = sys.maxint

        for v in [v1, v2, v3, v4, v5, v6]:
            d = pos1.distanceSquared(v)
            if v != None and d < distance:
                vector = v
                distance = d

        if vector == None:
            return None

        f = -1

        if vector == v1:
            f = Facing.WEST
        elif vector == v2:
            f = Facing.EAST
        elif vector == v3:
            f = Facing.DOWN
        elif vector == v4:
            f = Facing.UP
        elif vector == v5:
            f = Facing.NORTH
        elif vector == v6:
            f = Facing.SOUTH

        return RayTraceResult(self, f, vector)

    def __toString(self):
        return "AxisAlignedBB({self.minX}, {self.minY}, {self.minZ}, {self.maxX}, {self.maxY}, {self.maxZ})"

    @staticmethod
    def one():
        return AxisAlignedBB(0, 0, 0, 1, 1, 1)
