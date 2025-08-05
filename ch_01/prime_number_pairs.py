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

def compute_prime_pairs(max_value, distance):
    # distance --> 2 (twin), 4 (cousin), 6 (sexy)
    pair_distance = 0
    if distance.lower() == "twin":
        pair_distance = 2
    elif distance.lower() == "cousin":
        pair_distance = 4
    elif distance.lower() == "sexy":
        pair_distance = 6

    if max_value < 2:
        return []
            
    n  = 2
    primes_pairs = []

    while n <= max_value:
        if is_prime(n) and is_prime(n + pair_distance):
            primes_pairs.append({n : n + pair_distance})
        n += 1
    
    return primes_pairs


print(compute_prime_pairs(50, "sexy"))