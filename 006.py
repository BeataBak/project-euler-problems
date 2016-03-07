"""
Project Euler Problem 6
=======================

The sum of the squares of the first ten natural numbers is,
                       1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
                    (1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten
natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one
hundred natural numbers and the square of the sum.
"""


def task(numbers):
    return sum(numbers) ** 2 - sum(n ** 2 for n in numbers)


def test_task():
    assert task(range(1, 10 + 1)) == 2640


print(task(range(1, 100 + 1)))
