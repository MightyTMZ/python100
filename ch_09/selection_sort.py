def selection_sort(values):
    n = len(values)
    for i in range(n):
        min_index = i
        # find the smallest value in the rest of the list
        for j in range(i + 1, n):
            if values[j] < values[min_index]:
                min_index = j
        # find the smallest with the first unsorted element
        values[i], values[min_index] = values[min_index], values[i]
    return values
