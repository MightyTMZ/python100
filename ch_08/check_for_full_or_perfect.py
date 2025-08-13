def __is_full_helper(left_node, right_node):
    if left_node is None and right_node is None:
        return True
    
    if left_node is not None and right_node is not None:
        return is_full(left_node) and is_full(right_node)
    
    return False


def is_full(node):
    if node is None:
        return True
    
    return __is_full_helper(node.left, node.right)

