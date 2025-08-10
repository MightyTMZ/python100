def remove_duplicates(text):
    result = ""
    seen = set()

    for t in text:
        if not t in seen:
            seen.add(t)
            result += t

    return result
    
    