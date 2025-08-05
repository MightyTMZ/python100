value_to_text_mapping = {
    0: "ZERO",
    1: "ONE",
    2: "TWO",
    3: "THREE",
    4: "FOUR",
    5: "FIVE",
    6: "SIX",
    7: "SEVEN",
    8: "EIGHT",
    9: "NINE",
}


def number_as_text(num):
    total_text = ""

    while num != 0:
        remainder = num % 10
        value_to_text = ""

        value_to_text = value_to_text_mapping[remainder]

        total_text = value_to_text + " " + total_text
        num = num // 10

    return total_text


print(number_as_text(7))  # "SEVEN"
print(number_as_text(42))  # "FOUR TWO"
print(number_as_text(24680))  # "TWO FOUR SIX EIGHT ZERO"
print(number_as_text(13579))  # ONE THREE FIVE SEVEN NINE
