def number_as_text(num):
    total_text = ""
    
    while num != 0:
        remainder = num % 10
        value_to_text = ""

        if remainder == 0: 
            value_to_text = "ZERO"
        if remainder == 1: 
            value_to_text = "ONE"
        if remainder == 2: 
            value_to_text = "TWO"
        if remainder == 3: 
            value_to_text = "THREE"
        if remainder == 4: 
            value_to_text = "FOUR"
        if remainder == 5: 
            value_to_text = "FIVE"
        if remainder == 6: 
            value_to_text = "SIX"
        if remainder == 7: 
            value_to_text = "SEVEN"
        if remainder == 8: 
            value_to_text = "EIGHT"
        if remainder == 9: 
            value_to_text = "NINE"

        total_text = value_to_text + " " + total_text
        num = num // 10

    return total_text
    

print(number_as_text(7)) # "SEVEN"
print(number_as_text(42)) # "FOUR TWO"
print(number_as_text(24680)) # "TWO FOUR SIX EIGHT ZERO"
print(number_as_text(13579)) # ONE THREE FIVE SEVEN NINE