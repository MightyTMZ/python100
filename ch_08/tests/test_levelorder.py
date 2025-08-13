from ..example_trees import create_level_order_example_tree
from ..breadth_first import levelorder

def test_levelorder():
    root = create_level_order_example_tree()

    result = []
    levelorder(root, lambda item: result.append(item))

    assert result == ["1", "2", "3", "4", "5", "6", "7"]

