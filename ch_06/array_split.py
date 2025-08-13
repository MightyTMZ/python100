'''
Say you have a list or array of integers and you your task is to reorder so that the values
that are less than the reference element will be placed on the left and all values that are
greater than or equal to the reference value are placed on the righ. The ordering within the
subranges is not relevant and may vary 
'''

def array_split(values, reference_element):
    smaller_side = []
    larger_or_equal_to_side = []

    for v in values:
        if v < reference_element:
            smaller_side.append(v)
        else:
            larger_or_equal_to_side.append(v)

    result = smaller_side + [reference_element] + larger_or_equal_to_side

    return result

import random

x = [random.randint(1, 100) for x in range(10)]
ref = random.randint(25, 75)

print(f"Original: {x}")
print(f"Reference element {ref}")

print(f"Splitted: {array_split(x, ref)}")