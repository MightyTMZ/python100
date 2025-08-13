def binary_search(values, search_for):
    left_index = 0
    right_index = len(values) - 1

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid = values[mid_index]

        if mid == search_for:
            return True
        elif mid > search_for:
            right_index = mid_index - 1
        else:  # mid < search_for
            left_index = mid_index + 1

    return False

# Example usage
a = [x for x in range(10)]
sv = 9
print(binary_search(a, sv))  # True