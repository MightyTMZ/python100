def lcm_iterative(a, b):
    larger = max(a, b)
    smaller = min(a, b)

    value = larger
    while value % smaller != 0:
        value += larger
    
    return value


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm_recursive(a, b):
    return abs(a * b) // gcd(a, b)
