"""
Task
A prime is a natural number greater than 1 that has no positive divisors other than 1 and itself. Given a number, n, determine and print whether it is  Prime or Not Prime.

Note: If possible, try to come up with a  primality algorithm, or see what sort of optimizations you come up with for an  algorithm. Be sure to check out the Editorial after submitting your code.

Input Format

The first line contains an integer,T, the number of test cases.
Each of the T subsequent lines contains an integer, , to be tested for primality.

"""

import sys


def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


T = int(input())
for _ in range(T):
    n = int(input())
    if is_prime(n):
        sys.stdout.write("Prime\n")
    else:
        sys.stdout.write("Not Prime\n")
