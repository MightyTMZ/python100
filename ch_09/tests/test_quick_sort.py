from ..quick_sort import quick_sort


def test_quick_sort():
    arr = [37, 82, 15, 94, 61, 23, 48, 5, 76, 59]
    assert quick_sort(arr) == [5, 15, 23, 37, 48, 59, 61, 76, 82, 94]
