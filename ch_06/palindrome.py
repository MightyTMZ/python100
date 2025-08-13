def is_palindrome(values):
    left = 0
    right = len(values) - 1

    while right > left:
        if values[left] != values[right]:
            return False
        right -= 1
        left += 1
        
    return True
