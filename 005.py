"""
Project Euler Problem 5
=======================

2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest number that is evenly divisible by all of the numbers
from 1 to 20?
"""

from functools import reduce
from fractions import gcd


def lcm(x, y):
    """
    Takes two integers and returns the `Least Common Multiple`.
    """
    return x * y // gcd(x, y)


def lcm_iter(factors):
    """
    Takes an iterable of integers and returns the smallest number that
    can be divided by each without any remainder.

    The reduce works because of the commutative property of multiplication:
        lcm(x, y, z) == lcm(x, lcm(y, z))
    """
    return reduce(lcm, factors)


def test_divible_by():
    assert lcm_iter(range(2, 10 + 1)) == 2520


print(lcm_iter(range(2, 20 + 1)))