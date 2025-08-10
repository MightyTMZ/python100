def calc_text_frequency(text: str):
    char_counts = {}

    for char in text.lower():
        if char in char_counts:
            char_counts[char] += 1
        else: 
            char_counts[char] = 1
    
    return char_counts


def calc_text_frequency_no_spaces(text: str):
    char_counts = {}

    for char in text.lower():
        if char in char_counts:
            char_counts[char] += 1
        else: 
            char_counts[char] = 1

    char_counts.pop(" ")
    
    return char_counts


def is_anagram(text1, text2):
    return calc_text_frequency(text1) == calc_text_frequency(text2)

def is_anagram_with_no_spaces(text1, text2):
    return calc_text_frequency_no_spaces(text1) == calc_text_frequency_no_spaces(text2)