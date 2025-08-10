def to_morse_code(text: str):
    converted_message = ""

    morse_code_map = {
        "E": ".",
        "O": "---",
        "S": "...",
        "T": "-",
        "W": ".--",
    }

    for t in text.upper():
        converted_message += morse_code_map[t] + " "
    
    return converted_message.strip()