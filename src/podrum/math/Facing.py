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

class Facing:
    AXIS_Y = 0
    AXIS_Z = 1
    AXIS_X = 2

    FLAG_AXIS_POSITIVE = 1

    DOWN = AXIS_Y << 1
    UP = (AXIS_Y << 1) | FLAG_AXIS_POSITIVE
    NORTH = AXIS_Z << 1
    SOUTH = (AXIS_Z << 1) | FLAG_AXIS_POSITIVE
    WEST = AXIS_X << 1
    EAST = (AXIS_X << 1) | FLAG_AXIS_POSITIVE

    ALL = [
        DOWN,
        UP,
        NORTH,
        SOUTH,
        WEST,
        EAST
    ]

    HORIZONTAL = [
        NORTH,
        SOUTH,
        WEST,
        EAST
    ]

    CLOCKWISE = {
        AXIS_Y: {
            NORTH: EAST,
            EAST: SOUTH,
            SOUTH: WEST,
            WEST: NORTH
        },
        AXIS_Z: {
            UP: EAST,
            EAST: DOWN,
            DOWN: WEST,
            WEST: UP
        },
        AXIS_X: {
            UP: NORTH,
            NORTH: DOWN,
            DOWN: SOUTH,
            SOUTH: UP
        }
    }

    @staticmethod
    def axis(direction):
        return direction >> 1

    @staticmethod
    def is_positive(direction):
        return (direction & Facing.FLAG_AXIS_POSITIVE) == Facing.FLAG_AXIS_POSITIVE

    @staticmethod
    def opposite(direction):
        return direction ^ Facing.FLAG_AXIS_POSITIVE

    @staticmethod
    def rotate(direction, axis, clockwise):
        if not Facing.CLOCKWISE[axis]:
            raise ValueError("Invalid axis {}".format(axis))

        if not Facing.CLOCKWISE[axis][direction]:
            raise ValueError("Cannot rotate direction {} around axis {}".format(direction, axis))

        rotated = Facing.CLOCKWISE[axis][direction]
        return rotated if clockwise else Facing.opposite(rotated)

    @staticmethod
    def validate(facing):
        if facing in Facing.ALL:
            raise ValueError("Invalid direction {}".format(facing))
