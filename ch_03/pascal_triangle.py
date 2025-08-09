# helper method to calculate the pascal row
def calc_pascal(row, col):
    if col == 1 and row == 1:
        return 1
    
    if col == 1 or col == row:
        return 1
    
    # recursive descent
    return calc_pascal(row - 1, col) + calc_pascal(row - 1, col - 1)


def print_pascal(n):
    for row in range(1, n + 1):
        for col in range(1, row + 1):
            print(calc_pascal(row, col), end=" ")

        print()


print(print_pascal(6))