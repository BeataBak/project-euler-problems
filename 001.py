"""
Project Euler Problem 1
=======================

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def sum_multiples(f, n):
    """
    Find the sum of all the multiples of `f` within `n`.
    """
    return f * (n // f * (n // f + 1)) / 2


def sum_multiples_3_and_5(n):
    """
    Find the sum of all the multiples of 3 or 5 below `n`.
    """
    n -= 1

    return (
        sum_multiples(3, n) + sum_multiples(5, n) - sum_multiples(15, n)
    )


def test_sum_multiples():
    assert sum_multiples_3_and_5(10) == 23
    assert sum_multiples_3_and_5(20) == 78


print(sum_multiples_3_and_5(1000))
