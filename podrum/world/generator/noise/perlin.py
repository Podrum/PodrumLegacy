#########################################################
#  ____           _                                     #
# |  _ \ ___   __| |_ __ _   _ _ __ ___                 #
# | |_) / _ \ / _` | '__| | | | '_ ` _ \                #
# |  __/ (_) | (_| | |  | |_| | | | | | |               #
# |_|   \___/ \__,_|_|   \__,_|_| |_| |_|               #
#                                                       #
# Copyright 2021 Podrum Team.                           #
#                                                       #
# This file is licensed under the GPL v2.0 license.     #
# The license file is located in the root directory     #
# of the source code. If not you may not use this file. #
#                                                       #
#########################################################
# import random
import math
import numpy as np

class Perlin:
    def __init__(self, seed):
        self.m = 60000  # 100-70000 are most stable values
        p = list(range(self.m))
        np.random.RandomState(seed if seed >= 0 else -seed).shuffle(p)  # seeded shuffle
        self.p = p + p
        p = self.perlins = tuple((1 / i, i) for i in (16, 20, 22, 31, 32, 64, 512) for j in range(2))
        self.avg = 8 * len(p) / sum(f + i for f, i in p)

    def __call__(self, x, z, r=1, scale: float = 1, octaves: int = 1, persistence: float = 0.2, lacunarity: float = 2) -> int:
        amp: float = 1
        freq: float = 1
        height: float = 0

        for i in range(0, octaves):
            sample_x: float = x / scale * freq * (i+1)
            sample_z: float = z / scale * freq * (i+1)

            height += int(sum((self.noise(sample_x*s, sample_z*s) * amp)*h for s, h in self.perlins)*self.avg * 1/(i+1))

            amp *= persistence
            freq *= lacunarity

        return math.ceil(math.pow(height if height > 0 else -height, r)) * (1 if height > 0 else -1)

    @staticmethod
    def fade(t) -> float:
        return t * t * t * (t * (t * 6 - 15) + 10)

    @staticmethod
    def lerp(t, a, b) -> float:
        return a + t * (b - a)

    @staticmethod
    def grad(_hash, x, y, z) -> float:
        h = _hash & 15
        u = y if h & 8 else x
        v = (x if h == 12 or h == 14 else z) if h & 12 else y
        return (u if h & 1 else -u) + (v if h & 2 else -v)

    def noise(self, x, y, z=0) -> float:
        p, fade, lerp, grad = self.p, self.fade, self.lerp, self.grad
        xf, yf, zf = math.floor(x), math.floor(y), math.floor(z)
        X, Y, Z = xf % self.m, yf % self.m, zf % self.m
        x -= xf
        y -= yf
        z -= zf
        u, v, w = fade(x), fade(y), fade(z)
        A = p[X] + Y
        AA = p[A] + Z
        AB = p[A + 1] + Z
        B = p[X + 1] + Y
        BA = p[B] + Z
        BB = p[B + 1] + Z
        return lerp(w, lerp(v, lerp(u, grad(p[AA], x, y, z), grad(p[BA], x - 1, y, z)),
                            lerp(u, grad(p[AB], x, y - 1, z), grad(p[BB], x - 1, y - 1, z))),
                    lerp(v, lerp(u, grad(p[AA + 1], x, y, z - 1), grad(p[BA + 1], x - 1, y, z - 1)),
                         lerp(u, grad(p[AB + 1], x, y - 1, z - 1), grad(p[BB + 1], x - 1, y - 1, z - 1))))

