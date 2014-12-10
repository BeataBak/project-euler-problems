"""
Project Euler Problem 4
=======================

A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
def largest_palindrome(start , end):
    """
    Takes start and stop integers and returns the largest palindrome
    product out of all the factors in the range.
    """
    palindromes = []

    for i in range(start, end + 1):
        for j in range(start, end + 1):
            m = i * j

            if is_palindrome(m):
                palindromes.append(m)

    return max(palindromes)

def is_palindrome(number):
    """
    Takes a integer and returns True if it's palindromic, otherwise
    returns False.
    """
    return str(number) == str(number)[::-1]

def test_largest_palindrome():
    assert largest_palindrome(10, 99) == 9009

def test_is_palindrome():
    assert is_palindrome(9009)
    assert not is_palindrome(12345)

print(largest_palindrome(100, 999))