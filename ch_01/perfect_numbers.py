def calc_perfect_numbers(max_exclusive):

    if max_exclusive < 6:
        return []
    
    elif max_exclusive == 6:
        return [6]

    n = 6 # smallest perfect number
    perfect_numbers = []

    # helper method
    def is_perfect_number(number):
        divisors = []

        d = 1

        while d <= number // 2:
            if number % d == 0:
                divisors.append(d)
            d += 1
        
        return sum(divisors) == number

    while n < max_exclusive:
        if is_perfect_number(n):
            perfect_numbers.append(n)
        n += 1

    return perfect_numbers



print(calc_perfect_numbers(100)) # [6, 28]
print(calc_perfect_numbers(1000)) # [6, 28, 496]
print(calc_perfect_numbers(10000)) # [6, 28, 496. 8128]