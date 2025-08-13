class BinaryTreeNode:
    def __init__(self, item):
        self.right = None
        self.left = None
        self.item = item

    def is_leaf(self):
        return self.left is None and self.right is None
    
    def __str__(self):
        return "BinaryTreeNode [item=%s, left=%s, right=%s]" % (self.item, self.left, self.right)
    
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


def inorder_iterative(start_node: BinaryTreeNode, action):
    if start_node is None:
        return
    
    nodes_to_process = Stack()
    current_node = start_node

    while not nodes_to_process.is_empty() or current_node is not None:
        if current_node is not None:
            nodes_to_process.push(current_node)
            current_node = current_node.left
        else:
            # no left succcessor, then process current node
            current_node = nodes_to_process.pop()
            action(current_node.item)

            # continue with the right successor
            current_node = current_node.right


def preorder_iterative(start_node: BinaryTreeNode, action):
    if start_node is None:
        return
    
    nodes_to_process = Stack()
    nodes_to_process.push(start_node)

    while not nodes_to_process.is_empty():
        current_node = nodes_to_process.pop()

        if current_node is not None:
            action(current_node.item)

            nodes_to_process.push(current_node.right)
            nodes_to_process.push(current_node.left)


def postorder_iterative(start_node: BinaryTreeNode, action):
    if start_node is None:
        return
    
    nodes_to_process = Stack()
    current_node = start_node
    last_node_visited = None

    while not nodes_to_process.is_empty() or current_node is not None:
        if current_node is not None:
            # descent to the left
            nodes_to_process.push(current_node)
            current_node = current_node.left
        else: 
            peek_node = nodes_to_process.peek()
            # descent to the right
            if peek_node.right is not None and last_node_visited != peek_node.right:
                current_node = peek_node.right

            else:
                last_node_visited = nodes_to_process.pop()
                action(last_node_visited.item)

        