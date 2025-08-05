def fib_rec(n):
    if n <= 0:
        raise ValueError("n must be greater than or equal to 1")

    if n == 1 or n == 2:
        return 1

    return fib_rec(n - 1) + fib_rec(n - 2)


def fib_iterative(n):
    if n <= 0:
        raise ValueError("n must be greater than or equal to 1")

    if n == 1 or n == 2:
        return 1

    prev2 = 1
    prev1 = 1
    count = 2

    while count < n:
        new_fib = prev2 + prev1
        prev2 = prev1
        prev1 = new_fib
        count += 1

    return new_fib
