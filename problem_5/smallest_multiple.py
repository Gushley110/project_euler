# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def smallest_multiple(limit: int) -> int:
    number = limit

    while True:
        if check_divisibility(number, limit):
            return number
        number += limit


def check_divisibility(number: int, limit: int) -> bool:

    for i in range(2, limit + 1):
        if number % i != 0:
            return False

    return True


if __name__ == '__main__':
    print(smallest_multiple(20))

