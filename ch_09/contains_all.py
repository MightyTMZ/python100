""" 
DO NOT use the Python shortcut of all()
"""

def contains_all(values, search_values):
    for search in search_values:
        if not search in values:
            return False
    return True


# Example usage
_input = [x for x in range(10)]
sv = [7, 11]

print(contains_all(_input, sv))