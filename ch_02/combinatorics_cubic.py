# reduce from O(n^4) to O(n^3)

import math

def solve_cubic():
    for a in range(1, 100):
        for b in range(1, 100):
            for c in range(1, 100):
                value = a * a + b * b - c * c

                if value > 0:
                    d = int(math.sqrt(value))
                    if d < 100 and a * a + b * b == c * c + d * d:
                        print(f"{a}^2 + {b}^2 = {c}^2 + {d}^2")


solve_cubic()