def count_digits(value):
    if value < 10:
        return 1
    return count_digits(value // 10) + 1