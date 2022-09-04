from enum import Enum

class Direction(Enum):
    north = 1
    west = 2
    east = 3
    south = 4

print(type(Direction.east))
print(Direction.east)
print(Direction.east.name)
print(Direction.east.value)