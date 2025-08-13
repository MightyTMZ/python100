class BinaryTreeNode:
    def __init__(self, item):
        self.right = None
        self.left = None
        self.item = item

    def is_leaf(self):
        return self.left is None and self.right is None
    
    def __str__(self):
        return "BinaryTreeNode [item=%s, left=%s, right=%s]" % (self.item, self.left, self.right)
    

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




def create_example_tree():
    a1 = BinaryTreeNode("a1")
    b2 = BinaryTreeNode("b2")
    c3 = BinaryTreeNode("c3")
    d4 = BinaryTreeNode("d4")
    e5 = BinaryTreeNode("e5")
    f6 = BinaryTreeNode("f6")
    g7 = BinaryTreeNode("g7")

    d4.left = b2
    d4.right = f6
    b2.left = a1
    b2.right = c3
    f6.left = e5
    f6.right = g7

    return d4


def create_number_tree():
    _4 = BinaryTreeNode("4")
    insert(_4, "2")
    insert(_4, "1")
    insert(_4, "3")
    insert(_4, "6")
    insert(_4, "5")
    insert(_4, "7")

    return _4


def create_integer_number_tree():
    _4 = BinaryTreeNode(4)
    insert(_4, 2)
    insert(_4, 1)
    insert(_4, 3)
    insert(_4, 6)
    insert(_4, 5)
    insert(_4, 7)

    return _4


def create_lca_example_tree():
    _6 = BinaryTreeNode(6)
    insert(_6, 7)
    insert(_6, 4)
    insert(_6, 5)
    insert(_6, 2)
    insert(_6, 1)
    insert(_6, 3)

    return _6


def create_level_order_example_tree():
    _1 = BinaryTreeNode("1")
    _2 = BinaryTreeNode("2")
    _3 = BinaryTreeNode("3")
    _4 = BinaryTreeNode("4")
    _5 = BinaryTreeNode("5")
    _6 = BinaryTreeNode("6")
    _7 = BinaryTreeNode("7")

    _1.left = _2
    _1.right = _3
    _2.left = _4
    _2.right = _5
    _3.left = _6
    _3.right = _7

    return _1


def create_example_level_sum_tree():
    _4 = BinaryTreeNode(4)
    insert(_4, 2)
    insert(_4, 1)
    insert(_4, 3)
    insert(_4, 6)
    insert(_4, 5)
    insert(_4, 8)
    insert(_4, 7)
    insert(_4, 9)

    return _4