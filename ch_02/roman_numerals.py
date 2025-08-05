def to_roman_number(value):
    result = ""
    remainder = value

    int_to_roman_digit_map = {
        1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X",
        40: "XL", 50: "L", 90: "XC", 100: "C",
        400: "CD", 500: "D", 900: "CM", 1000: "M"
    }

    for i in sorted(int_to_roman_digit_map.keys(), reverse=True):
        if remainder > 0:
            multiplier = i
            roman_digit = int_to_roman_digit_map[i]

            times = remainder // multiplier
            remainder = remainder % multiplier
            result += roman_digit * times
    
    return result