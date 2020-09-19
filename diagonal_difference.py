"""Hacker Rank Problem Solving - Challenge 05; Diagonal Difference"""


def diagonal_difference(arr):
    l_indx = 0  # Left Index
    r_indx = len(arr)  # Right Index

    dd = 0  # Diagonal Difference

    while l_indx < len(arr):
        # Adding diagonal up-left to bottom-right
        dd += arr[l_indx][l_indx]
        # subtracting diagonal up-right to bottom-left
        dd -= arr[l_indx][r_indx - 1]
        l_indx += 1
        r_indx += -1

    return abs(dd)


# The primary test instances:
arr = [[1, 2, 3], [4, 5, 6], [9, 8, 9]]
print(diagonal_difference(arr))  # |15 - 17| = 2

arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
print(diagonal_difference(arr))  # |4 - 19| = 15

# For testing 4x4 matrix:
arr = [
    [1, 2, 3, 4],
    [10, 20, 30, 40],
    [100, 200, 300, 400],
    [1000, 2000, 3000, 4000],
]  # 4321 - 1234
print(diagonal_difference(arr))  # |1234 - 4321| = 3087
