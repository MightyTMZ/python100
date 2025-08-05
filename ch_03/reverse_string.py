def reverse_string(text):
    if len(text) <= 1:
        return text
    
    first_char = text[0]
    remaining = text[1:]

    return reverse_string(remaining) + first_char