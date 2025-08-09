import math

# helper method
def count_digits(number):
    count = 0
    remaining = number

    while remaining != 0:
        count += 1
        remaining //= 10

    return count


def calc_pow_of_ten(number):
    return math.log10(number)


def is_number_palindrome(number):
    if number < 10:
        return True
    
    factor = calc_pow_of_ten(number)
    divisor = math.pow(10, int(factor))

    if number < divisor * 10:
        left_number = number // divisor
        right_number = number % 10

        remaining_number = (number // 10) % (divisor // 10)

        return left_number == right_number and is_number_palindrome(remaining_number)
    
    return False

