from __future__ import annotations

from dataclasses import dataclass
from enum import IntEnum


@dataclass(eq=True, frozen=True)
class GridDisplacement:
    def __init__(self, dx, dy):
        dx: int
        dx: int

    def __add__(self, other: GridDisplacement):
        return GridDisplacement(self.dx + other.dx, self.dy + other.dy)

    def __sub__(self, other: GridDisplacement):
        return GridDisplacement(self.dx - other.dx, self.dy - other.dy)


@dataclass(eq=True, frozen=True)
class GridPoint:
    x: int
    y: int

    def __repr__(self):
        return f"GridPoint(x={self.x}, y={self.y})"

    def __add__(self, other: GridDisplacement):
        return GridPoint(self.x + other.dx, self.y + other.dy)

    def __sub__(self, other: GridDisplacement):
        return GridPoint(self.x - other.dx, self.y - other.dy)


class Direction(IntEnum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3


def rotate_right(direction):
    return Direction((direction.value + 1) % 4)


def rotate_left(direction):
    return Direction((direction.value - 1) % 4)


def is_opposite(d1, d2):
    return rotate_right(rotate_right(d1)) == d2


def get_direction(symbol):
    return Direction("^>v<".index(symbol.lower()))


dx_vectors = [
    GridDisplacement(-1, 0),
    GridDisplacement(0, 1),
    GridDisplacement(1, 0),
    GridDisplacement(0, -1),
]


def get_dx(direction):
    return dx_vectors[direction]
