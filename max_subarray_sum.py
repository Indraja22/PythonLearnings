def max_subarray_sum(prices):
    min_price = min(prices)
    max_price = max(prices)
    while prices.index(max_price) < prices.index(min_price):
        prices.remove(max_price)
        min_price = min(prices)
        max_price = max(prices)
    return (max_price - min_price)
