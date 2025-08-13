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
    

## TIP: you can consider passing a custom exception for a queue or stack 
## e.g. class QueueIsEmptyException(Exception):


# Test a queue

batting_order = Queue()

batting_order.enqueue("Liam")
batting_order.enqueue("Jack")
batting_order.enqueue("Charlie")
batting_order.enqueue("Jamie")
batting_order.enqueue("Tom")
batting_order.enqueue("Brayden")
batting_order.enqueue("Eli")
batting_order.enqueue("Theo")
batting_order.enqueue("Josh")

print("Starting batting order:")
print(batting_order.values)

print("\n--- Baseball Game ---")
while not batting_order.is_empty():
    current_player = batting_order.dequeue()
    print(f"{current_player} is at bat!")
    print(f"{current_player} hits the ball and goes to the end of the line.")

print("\nEnding batting order:")
print(batting_order.values)