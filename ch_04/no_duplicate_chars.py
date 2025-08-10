def check_no_duplicate_chars(text):
    seen = set()

    for char in text:
        if char.lower() in seen:
            return False
        seen.add(char.lower())

    return True
