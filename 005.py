"""
Project Euler Problem 5
=======================

2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest number that is evenly divisible by all of the numbers
from 1 to 20?
"""

from functools import reduce
from math import gcd


def divisible_by(factors):
    """
    Takes a list of integers and returns the smallest number that
    can be divided by each without any remainder.

    This works because:
        lcm(x, y) == (x * y) / gcd(x, y)

    And with the commutative property of multiplication:
        lcm(x, y, z) == lcm(x, lcm(y, z))
    """
    return reduce(lambda x, y: x * y // gcd(x, y), factors)


def test_divible_by():
    assert divisible_by(range(1, 10 + 1)) == 2520


print(divisible_by(range(1, 20 + 1)))
