from ..tree_traversal_iterative import postorder_iterative
from ..example_trees import create__example_tree

def test_postorder_iterative():
    root = create__example_tree()

    result = []
    postorder_iterative(root, lambda item: result.append(item))

    assert result == ['a1', 'c3', 'b2', 'e5', 'g7', 'f6', 'd4']