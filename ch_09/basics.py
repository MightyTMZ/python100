print([1, 2, 3, 4, 5].index(2)) # 1
print([1, 2, 3, 4, 5].index(3)) # 2
print([1, 2, 3, 4, 5].index(4)) # 3

print([i for i, val in enumerate([1, 2, 3, 4, 5, 6]) if val % 2 == 0] ) # [1, 3, 5]
print([1, 2, 3, 2, 4, 2].count(2)) # 3

people = {
    'Tom': 'Toronto',
    'Tim': "Ottawa",
}

if "Tom" in people.keys():
    print("Tom is here")


if 'Toronto' in people.values():
    print("Someone is in Toronto")

if ("Tom", 'Toronto') in people.items():
    print("Tom is in Toronto")

print(all(elem in [2, 3, 5, 7, 9] for elem in [7, 2])) # True
print(any(elem in [2, 3, 5, 7, 9] for elem in [7, 2])) # True
print(any(elem in [2, 3, 5, 7, 9] for elem in [4])) # True