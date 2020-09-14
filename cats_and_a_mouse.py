"""Hacker Rank Problem Solving - Challenge 43; Cats and a Mouse"""


def cats_and_mouse(x, y, z):
    if abs(x - z) < abs(y - z):
        return "Cat A"
    elif abs(x - z) > abs(y - z):
        return "Cat B"
    else:
        return "Mouse C"


# The primary test instances
x, y, z = 2, 5, 4
print(cats_and_mouse(x, y, z))

x, y, z = 1, 2, 3
print(cats_and_mouse(x, y, z))

x, y, z = 1, 3, 2
print(cats_and_mouse(x, y, z))
