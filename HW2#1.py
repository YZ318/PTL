def min_flips(coins):
    heads = coins.count(1)  # количество монеток, лежащих решкой вверх
    tails = len(coins) - heads  # количество монеток, лежащих гербом вверх
    return min(heads, tails)


coins = [1, 0, 1, 1, 0]  # 1 обозначает монетку, лежащую решкой вверх, 0 - гербом вверх
min_flips_needed = min_flips(coins)
print(min_flips_needed)
