import sys


def min_helper(values, pos, min_value):
    if pos >= len(values):
        return min_value
    
    value = values[pos]
    if value < min_value:
        min_value = value

    return min_helper(values, pos + 1, min_value)

def list_min(_list):
    return min_helper(_list, 0, sys.maxsize)
    # sys.maxsize means its the largest integer value it can store


