from ..partitioning import partition2, partition3

def test_partition2():
    assert partition2(list('ABABABABABABA')) == 'AAAAAAABBBBBB'


def test_partition3():
    assert partition3(list("ABCBCBBCBABCBACBCBC")) == "AAABBBBBBBBBCCCCCCC"