"""Hacker Rank Problem Solving - Challenge 42; Electronics Shop"""


def get_money_spent(keyboards, drives, b):
    price = 0

    for keyboard in keyboards:
        for drive in drives:
            if sum([keyboard, drive]) <= b and sum([keyboard, drive]) > price:
                price = sum([keyboard, drive])

    return price if price > 0 else -1


# The primary test instances
keyboards, drives, budget = [40, 50, 60], [5, 8, 12], 60
print(get_money_spent(keyboards, drives, budget))  # 58

keyboards, drives, budget = [3, 1], [5, 2, 8], 10
print(get_money_spent(keyboards, drives, budget))  # 9

keyboards, drives, budget = [5], [4], 5
print(get_money_spent(keyboards, drives, budget))  # -1
