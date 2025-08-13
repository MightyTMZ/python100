def move_tower(n, source, helper, destination):
    if n == 1:
        print(source + " -> " + destination)
    else:
        move_tower(n - 1, source, destination, helper)

        print(source + " -> " + destination)

        move_tower(n - 1, helper, source, destination)



def solve_tower_of_hanoi(n):
    print("Tower of Hanoi", n)
    move_tower(n, "A", "B", "C")


solve_tower_of_hanoi(5)