
def coinSum(target):
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    ways = [1] + [0] * target

    for coin in coins:
        for i in range(coin, target + 1):
            ways[i] += ways[i - coin]
    print(f"Ways to make change: {ways[target]}")


if __name__ == '__main__':
    coinSum(200)
