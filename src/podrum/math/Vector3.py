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

class Vector3:
    x = None
    y = None
    z = None

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_z(self):
        return self.z

    def get_floor_x(self) -> int:
        return math.floor(self.x)

    def get_floor_y(self) -> int:
        return math.floor(self.y)

    def get_floor_z(self) -> int:
        return math.floor(self.z)

    def get_chunk_x(self):
        return self.get_floor_x() >> 4

    def get_chunk_z(self):
        return self.get_floor_z() >> 4

    def get_right(self):
        return self.x

    def get_up(self):
        return self.y

    def get_forward(self):
        return self.z

    def get_south(self):
        return self.x

    def get_west(self):
        return self.z
    
    def add(self, x, y=None, z=None):
        if isinstance(x, Vector3):
            return Vector3(self.x + x.get_x(), self.y + x.get_y(), self.z + x.get_z())
        elif x is not None and y is None and z is None:
            return self.add(x, 0, 0)
        elif x is not None and y is not None and z is None:
            return self.add(x, y, 0)
        else:
            return Vector3(self.x + x, self.y + y, self.z + z)

    def substract(self, x=0, y=0, z=0):
        if isinstance(x, Vector3):
            return self.add(-x.x, -x.y, -x.z)
        else:
            return self.add(-x, -y, -z)

    def multiply(self, number):
        return Vector3(self.x * number, self.y * number, self.z * number)

    def divide(self, number):
        return Vector3(self.x / number, self.y / number, self.z / number)

    def ceil(self):
        return Vector3(math.ceil(self.x), math.ceil(self.y), math.ceil(self.z))

    def floor(self):
        return Vector3(math.floor(self.x), math.floor(self.y), math.floor(self.z))

    def round(self):
        return Vector3(round(self.x), round(self.y), round(self.z))

    def abs(self):
        return Vector3(abs(self.x), abs(self.y), abs(self.z))

    def get_side(self, side, step):
        if side is Facing.DOWN:
            return Vector3(self.x, self.y - step, self.z)
        elif side is Facing.UP:
            return Vector3(self.x, self.y + step, self.z)
        elif side is Facing.NORTH:
            return Vector3(self.x, self.y, self.z - step)
        elif side is Facing.SOUTH:
            return Vector3(self.x, self.y, self.z + step)
        elif side is Facing.WEST:
            return Vector3(self.x - step, self.y, self.z)
        elif side is Facing.EAST:
            return Vector3(self.x + step, self.y, self.z)
        else:
            return self

    def up(self, step):
        return self.get_side(Facing.UP, step)

    def down(self, step):
        return self.get_side(Facing.DOWN, step)

    def north(self, step):
        return self.get_side(Facing.NORTH, step)

    def south(self, step):
        return self.get_side(Facing.SOUTH, step)

    def east(self, step):
        return self.get_side(Facing.EAST, step)

    def west(self, step):
        return self.get_side(Facing.WEST, step)

    def distance(self, pos):
        return math.sqrt(self.distance_squared(pos))

    def distance_squared(self, pos):
        return math.pow(self.x - pos.x, 2) + math.pow(self.y - pos.y, 2) + math.pow(self.z - pos.z, 2)
