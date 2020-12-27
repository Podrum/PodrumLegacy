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

class Color:
    a = None
    r = None
    g = None
    b = None

    def __init__(self, r, g, b, a = 0xff):
        self.r = r & 0xff
        self.g = g & 0xff
        self.b = b & 0xff
        self.a = a & 0xff

    def getA(self):
        return self.a

    def setA(self, a):
        self.a = a & 0xff

    def getR(self):
        return self.r

    def setR(self, r):
        self.r = r & 0xff

    def getG(self):
        return self.g

    def setG(self, g):
        self.g = g & 0xff

    def getB(self):
        return self.b

    def setB(self, b):
        self.b = b & 0xff

    @staticmethod
    def mix(colors):
        count = len(colors)
        if count < 1:
            raise ValueError("No colors given")

        a = 0
        r = 0
        g = 0
        b = 0

        for color in colors:
            a += color.a
            r += color.r
            g += color.g
            b += color.b

        return Color((r / count), (g / count), (b / count), (a / count))

    @staticmethod
    def fromRGB(code):
        return Color((code >> 16) & 0xff, (code >> 8) & 0xff, code & 0xff)

    @staticmethod
    def fromARGB(code):
        return Color((code >> 16) & 0xff, (code >> 8) & 0xff, code & 0xff, (code >> 24) & 0xff)

    @staticmethod
    def fromABGR(code):
        return Color(code & 0xff, (code >> 8) & 0xff, (code >> 16) & 0xff, (code >> 24) & 0xff)

    def toARGB(self):
        return (self.a << 24) | (self.r << 16) | (self.g << 8) | self.b

    def toBGRA(self):
        return (self.b << 24) | (self.g << 16) | (self.r << 8) | self.a

    def toRGBA(self):
        return (self.r << 24) | (self.g << 16) | (self.b << 8) | self.a

    def toABGR(self):
        return (self.a << 24) | (self.b << 16) | (self.g << 8) | self.r
