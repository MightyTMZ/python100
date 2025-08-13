def order_even_before_odd(numbers):
    evens = []
    odds = []

    for num in numbers:
        if num % 2 == 0:
            evens.append(num)
        else:
            odds.append(num)

    return evens + odds


import random

x = [random.randint(1, 100) for x in range(20)]
print(x)

print(order_even_before_odd(x))
