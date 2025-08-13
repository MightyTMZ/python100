import sys

def max_revenue_brute_force(prices):
    highest = 0
    
    current_index = 0
    while current_index < len(prices) - 1:
        check_index = current_index + 1
        while check_index < len(prices):
            profit = prices[check_index] - prices[current_index]
            if profit > 0 and profit > highest:
                highest = profit
            check_index += 1
        current_index += 1
    
    return highest


def max_revenue_optimized(prices):
    current_min = sys.maxsize
    max_revenue = 0

    for current_price in prices:
        current_min = min(current_min, current_price)
        current_revenue = current_price - current_min
        max_revenue = max(max_revenue, current_revenue)

    return max_revenue
