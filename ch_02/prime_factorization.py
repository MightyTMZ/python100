# Helper method
def is_prime(number):
    x = 2

    if number < 2:
        return False

    while x <= number // 2:
        if number % x == 0:
            return False
        x += 1
    return True


def calc_prime_factors(value):
    if is_prime(value):
        return value
    
    if value % 2 == 0:
        return calc_prime_factors(value / 2)
    elif value % 2 == 1:
        return calc_prime_factors
