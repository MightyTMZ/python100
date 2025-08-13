def reverse_inplace(original):
    left = 0
    right = len(original) - 1

    # Swapping elements modifies the array in-place without creating or returning a new array.

    while left < right:
        left_elem = original[left]
        right_elem = original[right]

        original[left] = right_elem
        original[right] = left_elem

        left += 1
        right -= 1

    return original

