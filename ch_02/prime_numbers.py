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

print(calc_primes_up_to(15))
print(calc_primes_up_to(25))
print(calc_primes_up_to(50))