"""
Project Euler Problem 1
=======================

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

def sum_multiples(n):
    """
    Find the sum of all the multiples of 3 or 5 below `n`.
    """
    factors = [3, 5]
    multiples = []

    for i in range(1, n):
        if is_multiple(factors, i):
            multiples.append(i)

    return sum(multiples)

def is_multiple(factors, n):
    """
    Returns True if `n` is a multiple of any of `factors`.
    """
    for factor in factors:
        if n % factor == 0:
            return True

    return False

print(sum_multiples(1000))