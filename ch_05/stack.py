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
    

stack = Stack()
stack.push("Tom")
stack.push("Eric")

print("PEEK: " + stack.peek())
print("SIZE: " + str(stack.size()))
print("POP: " + stack.pop())
print("SIZE: " + str(stack.size()))
print("POP: " + stack.pop())
print("SIZE: " + str(stack.size()))
print("ISEMPTY: " + str(stack.is_empty()))