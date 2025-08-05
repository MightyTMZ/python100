# reduce time complexity from O(n^3) to O(n^2)

import math

def solve_quadratic():
    for a in range(1, 100):
        for b in range(1, 100):
            c = int(math.sqrt(a * a + b * b))

            if a**2 + b**2 == c**2:
                print(f"A: {a}, B: {b}, C: {c}")


solve_quadratic()