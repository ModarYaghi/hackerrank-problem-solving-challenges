"""Hacker Rank Problem Solving - Challenge 06; Plus Minus"""

# I like to use as less as possible of print() function.
# I used .format() method to access the position and the form of the outputs
#   {000000:.6f} to get the output in 6 digits form after the decimal.
# "\n" To get a new line (because I used one print() function)
# I used list comprehension to make a sublists, one for possitives, negatives,
#   and zeros, from the original list.
# Then, I got the len of the sublist and divided them by the length of
#   the original list to get the required ratio


def plus_minus(arr):
    print(
        # Positives
        "{000000:.6f}".format(len([x for x in arr if x > 0]) / len(arr)),
        # Negatives
        "\n{000000:.6f}".format(len([x for x in arr if x < 0]) / len(arr)),
        # Zeros
        "\n{000000:.6f}".format(len([x for x in arr if x == 0]) / len(arr)),
    )


# The primary test instances:
arr = [1, 1, 0, -1, -1]
print(plus_minus(arr))

# 0.400000
# 0.400000
# 0.200000

arr = [-4, 3, -9, 0, 4, 1]
print(plus_minus(arr))

# 0.500000
# 0.333333
# 0.166667
