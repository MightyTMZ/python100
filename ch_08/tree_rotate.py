def rotate_left(node):
    if node.right is None:
        raise ValueError("Can't rotate left, no valid root")
    
    rc = node.right
    rlc = node.right.left

    rc.left = node
    node.right = rlc

    return rc

def rotate_right(node):
    if node.left is None:
        raise ValueError("Can't rotate right, no valid root")
    
    lc = node.left
    lrc = node.left.right

    lc.right = node
    node.left = lrc

    return lc