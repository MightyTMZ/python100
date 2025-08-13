def quick_sort(values):
    if len(values) <= 1:
        return values  

    pivot = values[len(values) // 2]  # choose middle element as pivot
    left = [x for x in values if x < pivot]
    middle = [x for x in values if x == pivot]
    right = [x for x in values if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


