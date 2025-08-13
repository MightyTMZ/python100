class Queue:
    def __init__(self):
        self.values = []

    def is_empty(self):
        return len(self.values) == 0

    def enqueue(self, val):
        self.values.append(val)
    
    def peek(self):
        if self.is_empty():
            return "Queue is empty"    
        return self.values[0]

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        return self.values.pop(0)


def levelorder(start_node, action):
    if start_node is None:
        return 
    
    to_process = Queue()
    to_process.enqueue(start_node)

    while not to_process.is_empty():
        current = to_process.dequeue()

    if current is not None:
        action(current.item)

        to_process.enqueue(current.left)
        to_process.enqueue(current.right)

