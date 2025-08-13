from ..example_trees import create_example_level_sum_tree
from ..level_sum import level_sum_depth_first, level_sum


def test_level_sum():
    root = create_example_level_sum_tree()
    result = level_sum(root)

    assert result == {0: 4, 1: 8, 2: 17, 3: 16}


def test_level_sum_depth_first():
    root = create_example_level_sum_tree()
    result = level_sum_depth_first(root)

    assert result == {0: 4, 1: 8, 2: 17, 3: 16}

    