def calc_sum_of_digits(value):
    if value < 10:
        return value
    
    return value % 10 + calc_sum_of_digits(value // 10)