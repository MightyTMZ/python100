def is_bst(node):
    if node is None:
        return True
    
    if node.is_leaf():
        return True
    
    # recursive descent

    is_left_bst = True
    is_right_bst = True

    if node.left is not None:
        is_left_bst = node.left.item < node.item and is_bst(node.left)

    if node.right is not None:
        is_right_bst = node.right.item > node.item and is_bst(node.right)

    return is_left_bst and is_right_bst