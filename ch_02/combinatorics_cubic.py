# brute force

def solve_cubic():
    for a in range(1, 100):
        for b in range(1, 100):
            for c in range(1, 100):
                for d in range(1, 100):
                    if a*a + b*b == c*c + d*d:
                        print(f"{a}^2 + {b}^2 = {c}^2 + {d}^2")


solve_cubic()