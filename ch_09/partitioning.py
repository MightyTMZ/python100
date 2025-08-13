# 'text' is list of characters containing only ('A', 'B')
def partition2_easy(text):
    _list = list(text)
    return "".join(sorted(_list))


# 'text' is list of characters containing only ('A', 'B', 'C')
def partition3_easy(text):
    _list = list(text)
    return "".join(sorted(_list))

print(partition3_easy("ABCBCBBCBABCBACBCBC"))


"""
From now on, you cannot use the sort() method
"""

def partition2(text):
    # Convert to list for in-place modification
    text = list(text)
    low = 0
    high = len(text) - 1

    while low <= high:
        if text[low].upper() == 'A':
            low += 1
        else:
            # swap text[low] with text[high]
            text[low], text[high] = text[high], text[low]
            high -= 1  # move high pointer inward

    return "".join(text)


def partition3(text):
    # Convert to list for in-place modification
    text = list(text)
    low = 0
    mid = 0
    high = len(text) - 1

    while mid <= high:
        if text[mid].upper() == 'A':
            text[low], text[mid] = text[mid], text[low]
            low += 1
            mid += 1
        elif text[mid].upper() == 'B':
            mid += 1
        else:
            text[mid], text[high] = text[high], text[mid]
            high -= 1

    return "".join(text)