class Stack:
    def __init__(self):
        self.values = []

    def is_empty(self):
        return len(self.values) == 0

    def peek(self):
        return self.values[-1]

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.values.pop()
    
    def push(self, val):
        self.values.append(val)

    def size(self):
        return len(self.values)
    
    def get_at(self, pos):
        return self.values[pos]

class Tower:
    def __init__(self, name):
        self.name = name
        self.__values = Stack()

    def __str__(self):
        return "Tower [" + self.name + "]"
    
    def push(self, item):
        self.__values.push(item) 

    def pop(self):
        return self.__values.pop()
    
    def print_tower(self, max_height):
        height = self.__values.size() - 1
        
        visual = self.draw_top(max_height, height)
        visual += self.draw_slices(max_height, height)
        visual += self.draw_bottom(max_height)

        return visual

    def draw_top(self, max_height, height):
        visual = [" " * max_height + self.name + " " * max_height]

        for i in range(max_height - height - 1, 0, -1):
            visual.append(" " * max_height + "|" + " " * max_height)

        return visual
    
    def draw_slices(self, max_height, height):
        visual = []
        for i in range(height, -1, -1):
            value = self.__values.get_at(i)
            padding = max_height - value

            visual.append(" " * padding + "#" * value + "|" + "#" * value + " " * padding)

        return visual
    
    def draw_bottom(self, height):
        return ['-' * (height * 2 + 1)]


# ---------------------------------------------------------------------------------------------

def move_tower(n, source: Tower, helper: Tower, destination: Tower, action):
    if n == 1:
        element_to_move = source.pop()
        destination.push(element_to_move)

        print("Moving slice: ", element_to_move, ":", source, "->", destination)
        action()
    
    else:
        move_tower(n - 1, source, destination, helper, action)
        move_tower(1, source, helper, destination, action)
        move_tower(n - 1, helper, source, destination, action)


def solve_tower_of_hanoi(n):
    print("Tower of Hanoi", n)

    source = Tower("A")
    helper = Tower("B")
    destination = Tower("C")

    def print_towers(max_height, source, helper, destination):
        tower1 = source.print_tower(max_height)
        tower2 = helper.print_tower(max_height)
        tower3 = destination.print_tower(max_height)

        for (a, b, c) in zip(tower1, tower2, tower3):
            print(a + "   " + b + "   " + c)


    for i in range(n, 0, -1):
        source.push(i)

    action = lambda: print_towers(n + 1, source, helper, destination)
    action()

    move_tower(n, source, helper, destination, action)


solve_tower_of_hanoi(2)