def fib_recur(n):
    if n <= 0:
        raise ValueError("Given value of n must be greater than or equal to 1")
    
    if n == 1 or n == 2:
        return 1
    
    return fib_recur(n - 1) + fib_recur(n - 2)


# Memoization version
def fibonacci_memo(n, lookup_map):
    if n <= 0:
        raise ValueError("Given value of n must be greater than or equal to 1")
    
    if n in lookup_map:
        return lookup_map.get(n)
    
    result = 0

    if n == 1 or n == 2:
        result = 1
    else:
        result = fibonacci_memo(n - 1, lookup_map) + fibonacci_memo(n - 2, lookup_map)

    lookup_map[n] = result

    return result

