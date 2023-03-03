# A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindrome(number: int) -> bool:
    str_number = str(number)
    return str_number == str_number[::-1]


def largest_palindrome_product(digits: int = 3) -> int:
    biggest_n_digit_number = int('9' * digits)
    smallest_n_digit_number = int(f'1{"0" * (digits - 1)}')

    max_value = -1

    for factor_1 in range(biggest_n_digit_number, smallest_n_digit_number, -1):
        for factor_2 in range(biggest_n_digit_number, smallest_n_digit_number, -1):
            multiplication = factor_1 * factor_2
            if multiplication > max_value and is_palindrome(multiplication):
                max_value = multiplication

    return max_value


if __name__ == '__main__':
    print(largest_palindrome_product(3))
