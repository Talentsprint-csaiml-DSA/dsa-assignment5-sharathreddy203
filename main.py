def min_coins(coins, target_amount):
    # Initialize a list to store the minimum number of coins for each amount up to target_amount
    dp = [float('inf')] * (target_amount + 1)
    dp[0] = 0  # Base case: 0 coins are needed to make the amount 0

    # Iterate over each coin and update the dp array
    for coin in coins:
        for amount in range(coin, target_amount + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If dp[target_amount] is still infinity, it means it's not possible to make that amount
    return dp[target_amount] if dp[target_amount] != float('inf') else -1

# Example usage
# coins = [1, 4, 6, 9, 14]
# target_amount = 26
print(min_coins(coins, target_amount))  # Output: 3

