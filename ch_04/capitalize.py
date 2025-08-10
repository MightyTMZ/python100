def capitalize(words: list[str], ignorable_words: list[str]):
    for i, word in enumerate(words):
        if word not in ignorable_words:
            words[i] = word.capitalize()
    return words
