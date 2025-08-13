from ..selection_sort import selection_sort
import random


def test_selection_sort():
    values = [random.randint(1, 100) for _ in range(20)]
    expected = sorted(values)
    
    sorted_values = selection_sort(values)
    
    assert sorted_values == expected