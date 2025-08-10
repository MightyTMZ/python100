def join(values: list[str], delimitter: str):
    joined = ""

    for value in values:
        joined += (value + delimitter)

    return joined[:len(joined) - len(delimitter)]


print(join(['hello', 'world', 'message'], "++="))

