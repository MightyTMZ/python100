def list_add(values1, values2):
    m = max(len(values1), len(values2))
    result = []
    carry = 0

    for x in range(m - 1, -1, -1):
        sum = values1[x] + values2[x] + carry

        result.insert(0, sum % 10)

        carry = sum // 10

    if carry > 0:
        result.insert(0, 1)
    
    return result

