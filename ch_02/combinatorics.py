# brute force
# O(n^3)
def solve_quadratic():
    for a in range(1, 100):
        for b in range(1, 100):
            for c in range(1, 100):
                if a**2 + b**2 == c**2:
                    print(f"A: {a}, B: {b} C: {c}")


solve_quadratic()