"""Hacker Rank Problem Solving - Challenge 43; Cats and a Mouse"""


def cats_and_mouse(x, y, z):
    """_"""

    if abs(x - z) < abs(y - z):
        return "Cat A"
    if abs(x - z) > abs(y - z):
        return "Cat B"
    return "Mouse C"


# The primary test instances
_x, _y, _z = 2, 5, 4
print(cats_and_mouse(_x, _y, _z))  # Cat B

_x, _y, _z = 1, 2, 3
print(cats_and_mouse(_x, _y, _z))  # Cat B

_x, _y, _z = 1, 3, 2
print(cats_and_mouse(_x, _y, _z))  # Mouse C
