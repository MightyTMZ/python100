def insertion_sort(values):
    for i in range(1, len(values)):
        current_index = i

        while current_index > 0 and values[current_index - 1] > values[current_index]:
            values[current_index], values[current_index - 1] = (
                values[current_index - 1],
                values[current_index],
            ) # swap places

            current_index -= 1

