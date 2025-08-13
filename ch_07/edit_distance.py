# For two strings, how many changes they are (case insensitive) apart 

# Add a character
# Delete a character
# Change a character


def __edit_distance_helper(str1, str2, pos1, pos2):
    if pos1 < 0:
        return pos2 + 1
    
    if pos2 < 0:
        return pos1 + 1
    
    if str1[pos1] == str2[pos2]:
        return __edit_distance_helper(str1, str2, pos1 - 1, pos2 - 1)
    else:
        insert_in_first = __edit_distance_helper(str1, str2, pos1, pos2 - 1)
        delete_in_first = __edit_distance_helper(str1, str2, pos1 - 1, pos2)
        change = __edit_distance_helper(str1, str2, pos1 - 1, pos2 - 1)

        return 1 + min(insert_in_first, delete_in_first, change)

def edit_distance(str1: str, str2: str):
    return __edit_distance_helper(str1.lower(), str2.lower(), len(str1) - 1, len(str2) - 1)