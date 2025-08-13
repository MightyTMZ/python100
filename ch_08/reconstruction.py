from binary_tree import BinaryTreeNode

def reconstruct(values: list):
    if not values:
        return None
    
    mid_index = len(values) // 2
    mid_value = values[mid_index]

    new_node = BinaryTreeNode(mid_value)

    if len(values) == 1:
        # recursive base case
        return new_node

    left_part = values[0: mid_index]
    right_part = values[mid_index + 1:len(values)]

    new_node.left = reconstruct(left_part)
    new_node.right = reconstruct(right_part)

    reconstruct(left_part)
    reconstruct(right_part)

    return new_node

