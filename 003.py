"""
Project Euler Problem 3
=======================

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""
def highest_prime_factor(number):
    """
    Takes a number and returns it's highest prime factor.
    """
    prime_factor = 1

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0 and is_prime(i):
            prime_factor = i

    return prime_factor

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

def test_highest_prime_factor():
    assert highest_prime_factor(13195) == 29

def test_is_prime_returns_true_for_primes():
    for prime in [2, 3, 5, 7, 11, 13, 29]:
        assert is_prime(prime)

def test_is_prime_returns_false_for_not_prime():
    for not_prime in [4, 9, 15]:
        assert not is_prime(not_prime)

def test_is_prime_returns_false_for_negative():
    assert not is_prime(-5)

def test_is_prime_returns_false_for_zero():
    assert not is_prime(0)

print(highest_prime_factor(600851475143))