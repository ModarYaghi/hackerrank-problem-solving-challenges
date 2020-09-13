"""Hacker Rank Problem Solving - Challenge 23; Counting Valleys"""


def counting_valleys(n, s):
    sea_surface = 0
    valleys = 0

    for step in s:
        if step == "U":
            sea_surface += 1
            if sea_surface == 0:
                valleys += 1

        else:
            sea_surface += -1

    return valleys


# The primary test instances:
print(counting_valleys(8, "UDDDUDUU"))  # 1
print(counting_valleys(12, "DDUUDDUDUUUD"))  # 2
