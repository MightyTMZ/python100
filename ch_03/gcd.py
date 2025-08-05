# not using math.gcd(**nums)

def gcd(a, b):
    if b == 0:
        return a
    
    return gcd(b, a % b)


def gcd_iterative(a, b):
    while b != 0:
        a, b = b, a % b
    return a