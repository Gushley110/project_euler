
def sum_squares(number: int) -> int:
    return int(number * (number + 1) * (2 * number + 1) / 6)


def square_sum(number: int) -> int:
    return int((number * (number + 1) / 2) ** 2)


def sum_square_difference(number: int) -> int:
    return square_sum(number) - sum_squares(number)


if __name__ == '__main__':
    print(sum_square_difference(100))
