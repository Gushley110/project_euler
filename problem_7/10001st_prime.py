# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?
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


def nth_prime(n) -> int:
    position = 0
    value = 2

    while position != n:
        if is_prime(value):
            value = value
            position += 1
        value += 1

    return value - 1


if __name__ == '__main__':
    print(nth_prime(10001))