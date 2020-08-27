"""Hacker Rank Problem Solving - Challenge 22; Drawing Book"""


def page_count(n, p):
    return min(p // 2, n // 2 - p // 2)


print(page_count(5, 4))
print(page_count(6, 2))
print(page_count(201, 79))
print(page_count(552, 401))
