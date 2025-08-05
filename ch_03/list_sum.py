def list_sum(_list):
    if not _list:
        return 0

    if len(_list) == 1:
        return _list[0]

    first_num = _list[0]
    remaining = _list[1:]

    return first_num + list_sum(remaining)
