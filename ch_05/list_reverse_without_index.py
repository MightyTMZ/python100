# Reversing without index means we CANNOT use any indexing on a list

from stack import Stack
    

def reverse_without_index(values):
    copy_values = Stack()
    reversed = []

    for x in values:
        copy_values.push(x)
    
    while not copy_values.is_empty():
        reversed.append(copy_values.pop())

    return reversed



s = Stack()
s.push(1)
s.push(2)
s.push(3)

print(s.pop())  # Should print 3
print(s.pop())  # Should print 2
print(s.pop())  # Should print 1

print(reverse_without_index([1, 2, 3]))          # Expected: [3, 2, 1]
print(reverse_without_index(['a', 'b', 'c']))    # Expected: ['c', 'b', 'a']
print(reverse_without_index([10, 20, 30, 40]))   # Expected: [40, 30, 20, 10]