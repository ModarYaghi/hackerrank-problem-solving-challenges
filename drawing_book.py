"""Hacker Rank Problem Solving - Challenge 22; Drawing Book"""


def page_count(n, p):
    return min(p // 2, n // 2 - p // 2)


# The primary test instances
print(page_count(5, 4))  # 0
print(page_count(6, 2))  # 1

# More instances
print(page_count(201, 79))  # 39
print(page_count(552, 401))  # 76
