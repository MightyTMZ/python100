def pascal_rec(row, col):
    if col == 1 and row == 1:
        return 1
    
    if col == 1 and row == col:
        return 1
    
    return pascal_rec(row - 1, col) + pascal_rec(row - 1, col - 1)

# add memoization
def calc_pascal_memo(row, col, lookup_map):
    key = (row, col)

    if key in lookup_map:
        return lookup_map[key]
    
    result = 0
    if col == 1 and row == 1:
        return 1
    
    if col == 1 and row == col:
        return 1
    else:
        return calc_pascal_memo(row - 1, col, lookup_map) + calc_pascal_memo(row - 1, col - 1, lookup_map)
    

# Memoized Pascal's Triangle function 

def pascal_memoized(row, col):
    return calc_pascal_memo(row, col, {})