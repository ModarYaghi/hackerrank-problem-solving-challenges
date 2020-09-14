"""Hacker Rank Problem Solving - Challenge 42;
    Lest Comprehension Solution of Electronics Shop"""

# I found this solution in the repo of sapanz/Hackerrank-Problem-Solving-Python-Solutions

# This solution has written in one line, but it is rearranged as PEP8 style to be more readable

# The idea of this solution is:
# 1. By the list comprehension way; it makes a list that contains all possible
#    prices of keyboards and drives that are less than or equal to the value of the budget.
# 2. Adding a value of [-1] to the list.
# 3. Return the maximum value in the list.
#    Thus in case, there are no values that have passed into the list,
#    let say because all of them were greater than the budget,
#    then the list will contains only the value of [-1], which will be returned in this case.


def get_money_spent(keyboards, drives, b):
    return max(
        [
            sum([keyboard, drive])
            for keyboard in keyboards
            for drive in drives
            if sum([keyboard, drive]) <= b
        ]
        + [-1]
    )


# The primary test instances
keyboards, drives, budget = [40, 50, 60], [5, 8, 12], 60
print(get_money_spent(keyboards, drives, budget))  # 58

keyboards, drives, budget = [3, 1], [5, 2, 8], 10
print(get_money_spent(keyboards, drives, budget))  # 9

keyboards, drives, budget = [5], [4], 5
print(get_money_spent(keyboards, drives, budget))  # -1
