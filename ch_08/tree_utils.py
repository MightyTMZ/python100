from binary_tree import BinaryTreeNode

def find(current_node, search_for):
    if current_node is None:
        return None
    
    if current_node.item < search_for:
        return find(current_node.right, search_for)
    if current_node.item > search_for:
        return find(current_node.left, search_for)
    
    return current_node

def insert(current_node, value):
    if current_node is None:
        return BinaryTreeNode(value)
    
    if value < current_node.item:
        current_node.left = insert(current_node.left, value)
    elif value > current_node.item:
        current_node.right = insert(current_node.right, value)
    
    return current_node

