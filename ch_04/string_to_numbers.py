def is_binary_number(str_num: str):
    if not str_num.isdigit():
        return False

    for c in range(len(str_num)):
        if not (str_num[c] == "0" or str_num[c] == "1"):
            return False

    return True


def binary_to_decimal(str_num: str):
    length = len(str_num)
    count = 0
    number = 0

    while count < length:
        if str_num[count] == "1":
            number += 2 ** (length - count - 1)
        count += 1

    return number

def hex_to_decimal(str_num: str):
    length = len(str_num)
    count = 0
    number = 0

    HEX_MAP = {
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "A": 10,
        "B": 11,
        "C": 12,
        "D": 13,
        "E": 14,
        "F": 15,
    }

    while count < length:
        current_char = str_num[count].upper()
        number += HEX_MAP[current_char] * 16 ** (length - count - 1)
        count += 1

    return number