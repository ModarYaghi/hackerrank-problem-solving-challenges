"""Hacker Rank Problem Solving - Challenge 03; Compare The Triplets"""


def compare_triplets(a, b):
    """_"""
    scores = [0, 0]

    for i in range(3):
        if a[i] > b[i]:
            scores[0] += 1
        elif a[i] < b[i]:
            scores[1] += 1

    return scores


# The primary test instances:
_a, _b = [1, 2, 3], [3, 2, 1]
print(compare_triplets(_a, _b))  # [1, 1]

_a, _b = [5, 6, 7], [3, 6, 10]
print(compare_triplets(_a, _b))  # [1, 1]

_a, _b = [17, 28, 30], [99, 16, 8]
print(compare_triplets(_a, _b))  # [2, 1]
