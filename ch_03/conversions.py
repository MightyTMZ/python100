def to_binary(x):
    if x < 0:
        raise ValueError("x has to be greater than or equal to 0")

    if x == 1 or x == 0:
        return str(x)
    
    return to_binary(x // 2) + str(x % 2)

