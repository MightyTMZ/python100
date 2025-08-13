def invert(root):
    if root is None:
        return None
    
    inverted_right = invert(root.right)
    inverted_left = invert(root.left)

    root.left = inverted_right
    root.right = inverted_left
    
    return root