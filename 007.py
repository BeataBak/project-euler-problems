"""
Project Euler Problem 7
=======================

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13.

What is the 10001st prime number?
"""
from itertools import count


def is_prime(number):
    """
    Takes a number and returns True if it's a prime number, otherwise returns False.
    """
    if number == 2 or number == 3:
        return True

    if number <= 0 or number % 2 == 0 or number % 3 == 0:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True


def prime_by_position(position):
    """
    Takes an integer and returns the prime number at that position.
    """
    prime_count = 0

    for i in count(start=2):
        if is_prime(i):
            prime_count += 1

            if prime_count == position:
                return i


def test_prime_by_position():
    assert prime_by_position(6) == 13

print(prime_by_position(10001))
