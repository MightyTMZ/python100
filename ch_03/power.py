def is_power_of_2(n):
    if n < 2:
        return n == 1
    if n % 2 != 0:
        return False
    
    return is_power_of_2(n // 2)


def is_power_of(n, m):
    if n == m:
        return True
    
    if m == 1:
        return False

    if n < m:
        return n == 1
    if n % m != 0:
        return False
    
    return is_power_of(n // m, m)


print(is_power_of(432434, 1.2313))