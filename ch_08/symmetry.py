def check_if_nodes_are_symmetric(left, right):
    if left is None and right is None:
        return True

    if left is None or right is None:
        return False

    # descend both trees
    return check_if_nodes_are_symmetric(left.right, left.left) and \
    check_if_nodes_are_symmetric(left.left, right.right)


def is_symmetric(node):
    if node is None:
        return True
    
    return check_if_nodes_are_symmetric(node.left, node.right)