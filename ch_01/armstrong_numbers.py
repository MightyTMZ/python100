def is_armstrong_number(number):
    # three digit number
    x = (number // 100) % 10
    y = (number // 10) % 10
    z = number % 10

    return x * 100 + y * 10 + z == x**3 + y**3 + z**3


print(is_armstrong_number(152))