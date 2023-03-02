# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

from math import sqrt


def is_prime(number: int) -> bool:
    if number == 1:
        return False

    if number == 2:
        return True

    for i in range(2, int(sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


def largest_prime_factor(number: int) -> int:

    for i in range(1, number):
        if number % i == 0 and is_prime(int(number / i)):
            return int(number / i)


print(largest_prime_factor(600851475143))
