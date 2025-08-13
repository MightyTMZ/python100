from binary_tree import BinaryTreeNode

def inorder(node: BinaryTreeNode, action):
    if node is None: 
        return
    
    inorder(node.left, action)
    action(node.item)
    inorder(node.right, action)


def preorder(node: BinaryTreeNode, action):
    if node is None:
        return 
    
    action(node.item)
    preorder(node.left, action)
    preorder(node.right, action)


def postorder(node: BinaryTreeNode, action):
    if node is None: 
        return 
    
    postorder(node.left, action)
    postorder(node.right, action)
    action(node.item)


def to_list(start_node: BinaryTreeNode):
    # inorder
    if start_node is None:
        return []
    
    result = []

    result += to_list(start_node.left)
    result.append(start_node.item)
    result += to_list(start_node.right)

    return result

def to_list_preorder(start_node: BinaryTreeNode):
    if start_node is None:
        return []
    
    result = []

    result.append(start_node.item)
    result += to_list_preorder(start_node.left)
    result += to_list_preorder(start_node.right)


def to_list_postorder(start_node: BinaryTreeNode):
    if start_node is None:
        return []
    
    result = []

    result += to_list_postorder(start_node.left)
    result += to_list_postorder(start_node.right)
    result.append(start_node.item)

    return result