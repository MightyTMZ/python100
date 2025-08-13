# Determine the height for both a tree and for subtrees with a single node as root

from binary_tree import BinaryTreeNode

def get_height(node: BinaryTreeNode):
    if node is None:
        return 0
    
    left_height = get_height(node.left)
    right_height = get_height(node.right)

    return 1 + max(left_height, right_height)
