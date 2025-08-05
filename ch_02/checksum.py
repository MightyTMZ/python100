def calc_checksum(string):

    total = 0

    if len(string) == 1:
        return int(string)

    for x in range(1, len(string) + 1):
        total += x * int(string[x - 1])

    return total % 10


print(calc_checksum("11111"))  # 5
print(calc_checksum("87654321"))  # 0