# helper method
def find_proper_divisors(number):
    return [x for x in range(1, int(number/2) + 1) if number % x == 0]


def calc_friends(max_exclusive):
    friends = {}

    for i in range(2, max_exclusive):
        divisors1 = find_proper_divisors(i)
        sum_div1 = sum(divisors1)
        divisors2 = find_proper_divisors(sum_div1)
        sum_div2 = sum(divisors2)

        if i == sum_div2 and sum_div1 != sum_div2:
            friends[i] = sum_div1

    return friends