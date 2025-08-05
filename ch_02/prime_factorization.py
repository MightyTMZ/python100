# Helper methods
def is_prime(number):
    x = 2

    if number < 2:
        return False

    while x <= number // 2:
        if number % x == 0:
            return False
        x += 1
    return True

def calc_primes_up_to(max_value):
    if max_value < 2:
        return []
            
    n  = 2
    primes = []

    while n <= max_value:
        if is_prime(n):
            primes.append(n)
        n += 1
    
    return primes

# Solution
def calc_prime_factors(value):
    all_primes = calc_primes_up_to(value)
    prime_factors = []

    remaining_value = value
    while remaining_value > 1:
        for current_prime in all_primes:
            while remaining_value % current_prime == 0:
                remaining_value = remaining_value // current_prime
                prime_factors.append(current_prime)
    
    return prime_factors