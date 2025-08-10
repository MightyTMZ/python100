def is_blank(text: str):
    return not (text and text.strip())

def calc_permutations(text):
    if not text or len(text) == 1:
        return {text}
    
    combinations = set()

    for i, new_first in enumerate(text):
        permutations = calc_permutations(text[0:i] + text[i + 1:])

        for perm in permutations:
            combinations.add(new_first + perm)

    return combinations

print(calc_permutations("ABC"))