import math

class Noise:
    f2 = 0.5 * (math.sqrt(3) - 1)
    g2 = (3 - math.sqrt(3)) / 6
    f3 = 1 / 3
    g3 = 1 / 6

    perm = []
    permMod12 = []

    p = [
        151, 160, 137, 91, 90, 15, 131, 13, 201, 95, 96, 53, 194, 233, 7,
        225, 140, 36, 103, 30, 69, 142, 8, 99, 37, 240, 21, 10, 23, 190,
        6, 148, 247, 120, 234, 75, 0, 26, 197, 62, 94, 252, 219, 203, 117,
        35, 11, 32, 57, 177, 33, 88, 237, 149, 56, 87, 174, 20, 125, 136,
        171, 168, 68, 175, 74, 165, 71, 134, 139, 48, 27, 166, 77, 146, 158,
        231, 83, 111, 229, 122, 60, 211, 133, 230, 220, 105, 92, 41, 55, 46,
        245, 40, 244, 102, 143, 54, 65, 25, 63, 161, 1, 216, 80, 73, 209,
        76, 132, 187, 208, 89, 18, 169, 200, 196, 135, 130, 116, 188, 159, 86,
        164, 100, 109, 198, 173, 186, 3, 64, 52, 217, 226, 250, 124, 123, 5,
        202, 38, 147, 118, 126, 255, 82, 85, 212, 207, 206, 59, 227, 47, 16,
        58, 17, 182, 189, 28, 42, 223, 183, 170, 213, 119, 248, 152, 2, 44,
        154, 163, 70, 221, 153, 101, 155, 167, 43, 172, 9, 129, 22, 39, 253,
        19, 98, 108, 110, 79, 113, 224, 232, 178, 185, 112, 104, 218, 246, 97,
        228, 251, 34, 242, 193, 238, 210, 144, 12, 191, 179, 162, 241, 81, 51,
        145, 235, 249, 14, 239, 107, 49, 192, 214, 31, 181, 199, 106, 157, 184,
        84, 204, 176, 115, 121, 50, 45, 127, 4, 150, 254, 138, 236, 205, 93,
        222, 114, 67, 29, 24, 72, 243, 141, 128, 195, 78, 66, 215, 61, 156, 180
    ]

    grad3 = [
        1, 1, 0, -1, 1, 0, 1, -1, 0, -1, -1, 0,
        1, 0, 1, -1, 0, 1, 1, 0, -1, -1, 0, -1,
        0, 1, 1, 0, -1, 1, 0, 1, -1, 0, -1, -1
    ]

    def __init__(self):
        for i in range(0, 256):
            self.p.insert(i, abs(~~int(self.seed(i) * 256)))
        for i in range(0, 512):
            self.perm.insert(i, self.p[i & 255])
            self.permMod12.insert(i, self.perm[i] % 12)

    def seed(self, value):
        value = (value << 13) ^ value
        return ( 1 - ( (value * (value * value * 15731 + 789221) + 1376312589) & 0x7fffffff) / 1073741824)

    def fade(self, t):
        return t * t * t * (t * (t * 6 - 15) + 10)

    def lerp(self, a, b, t):
        return (1 - t) * a + t * b

    def simplex2(self, x, y):
        s = (x + y) * self.f2
        i = math.floor(x + s)
        j = math.floor(y + s)
        t = (i + j) * self.g2
        x0 = x - i - t
        y0 = y - j - t
        if x0 > y0:
            i1 = 1
            j1 = 0
        else:
            i1 = 0
            j1 = 1
        x1 = x0 - i1 + self.g2
        y1 = y0 - j1 + self.g2
        x2 = x0 - 1 + 2 * self.g2
        y2 = y0 - 1 + 2 * self.g2
        i = i & 255
        j = j & 255
        gi0 = self.permMod12[i + self.perm[j]]
        gi1 = self.permMod12[i + i1 + self.perm[j + j1]]
        gi2 = self.permMod12[i + 1 + self.perm[j + 1]]
        t0 = 0.5 - x0 * x0 - y0 * y0
        if t0 < 0:
            n0 = 0
        else:
            t0 *= t0
            n0 = t0 * t0 * (self.grad3[gi0] * x0 + self.grad3[gi0 + 1] * y0)
        t1 = 0.5 - x1 * x1 - y1 * y1
        if t1 < 0:
            n1 = 0
        else:
            t1 *= t1
            n1 = t1 * t1 * (self.grad3[gi1] * x1 + self.grad3[gi1 + 1] * y1)
        t2 = 0.5 - x2 * x2 - y2 * y2
        if t2 < 0:
            n2 = 0
        else:
            t2 *= t2
            n2 = t2 * t2 * (self.grad3[gi2] * x2 + self.grad3[gi2 + 1] * y2)
        return 70 * (n0 + n1 + n2)

    def perlin2(self, x, y):
        X = math.floor(x) & 255
        Y = math.floor(y) & 255
        x -= math.floor(x)
        y -= math.floor(y)
        u = self.fade(x)
        v = self.fade(y)
        n00 = self.perm[X + self.perm[Y]] % 12
        n01 = self.perm[X + self.perm[Y + 1]] % 12
        n10 = self.perm[X + 1 + self.perm[Y + 1]] % 12
        n11 = self.perm[X + 1 + self.perm[Y + 1]] % 12
        gi00 = self.grad3[n00] * x * self.grad3[n00] * y
        gi01 = self.grad3[n01] * x * self.grad3[n01] * (y - 1)
        gi10 = self.grad3[n10] * (x - 1) * self.grad3[n10] * y
        gi11 = self.grad3[n11] * (x - 1) * self.grad3[n11] * (y - 1)
        return self.lerp(self.lerp(gi00, gi10, u), self.lerp(gi01, gi11, u), v)
