import random

"""
Creating random deposit and withdraw values.
"""


def rand_deposit():
    random_amount = random.randint(100, 10000)
    return str(random_amount)


def rand_withdraw():
    random_amount = random.randint(25, 100)
    return str(random_amount)
