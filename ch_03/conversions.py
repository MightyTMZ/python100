def to_binary(x):
    if x < 0:
        raise ValueError("x has to be greater than or equal to 0")

    if x == 1 or x == 0:
        return str(x)

    return to_binary(x // 2) + str(x % 2)


def to_octal(x):
    if x < 0:
        raise ValueError("x has to be greater than or equal to 0")

    if x < 8:
        return str(x)

    return to_octal(x // 8) + str(x % 8)


def to_hexadecimal(x):
    if x < 0:
        raise ValueError("x has to be greater than or equal to 0")

    greater_than_nine_map = {
        10: "A",
        11: "B",
        12: "C",
        13: "D",
        14: "E",
        15: "F",
    }

    def get_hex_char(n):
        if n < 16:
            if n >= 10:
                return greater_than_nine_map[n]
            return str(n)

    if x < 16:
        return get_hex_char(x)

    return to_hexadecimal(x // 16) + get_hex_char(x % 16)
