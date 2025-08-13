def add_one(digits: list):
    result = digits[:] # make a copy of it to avoid modifying input list directly

    result[-1] += 1
    carry = 1 if result[-1] >= 10 else 0
    result[-1] %= 10

    current_index = len(result) - 2

    while carry > 0 and current_index >= 0:
        result[current_index] += carry
        carry = 1 if result[current_index] >= 10 else 0
        result[current_index] %= 10
        current_index -= 1

    if carry > 0:
        result.insert(0, 1)

    return result


print(add_one([9, 9, 9]))