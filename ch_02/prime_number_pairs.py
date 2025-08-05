from prime_numbers import calc_primes_up_to


# helper method
def is_prime(number):
    x = 2

    if number < 2:
        return False

    while x <= number // 2:
        if number % x == 0:
            return False
        x += 1
    return True


# Solution (based on dictonary pairs NOT on a list of objects)
def main_v1():
    bound = 50

    def is_twin_pair(n):
        return is_prime(n) and is_prime(n + 2)

    def is_cousin_pair(n):
        return is_prime(n) and is_prime(n + 4)

    def is_sexy_pair(n):
        return is_prime(n) and is_prime(n + 6)

    # Dict comprehension
    twin_pairs = {i: i + 2 for i in range(1, bound) if is_twin_pair(i)}
    cousin_pairs = {i: i + 4 for i in range(1, bound) if is_cousin_pair(i)}
    sexy_pairs = {i: i + 6 for i in range(1, bound) if is_sexy_pair(i)}

    print("Twins: ", twin_pairs)
    print("Cousins: ", cousin_pairs)
    print("Sexy: ", sexy_pairs)


# More optimized
# No more repeated calls for primes
# Boosts performance
# More clear program structure


def main_v2():
    bound = 50

    def is_prime_improved(n, _list):
        return n in _list

    def calc_pairs(max_value, distance):
        primes = calc_primes_up_to(max_value + distance)

        return {
            number: number + distance
            for number in range(1, max_value)
            if is_prime_improved(number, primes) and is_prime_improved(number + distance, primes)
        }


    # Dict comprehension
    twin_pairs = calc_pairs(bound, 2)
    cousin_pairs = calc_pairs(bound, 4)
    sexy_pairs = calc_pairs(bound, 6)

    print("Twins: ", twin_pairs)
    print("Cousins: ", cousin_pairs)
    print("Sexy: ", sexy_pairs)