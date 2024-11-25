



'''
题意：
Give you some numbers, each number can be selected without limit, ask how many combinations there are to form the target number

思路:
algorithm used: Dynamic Programming
1. Use a DP array dp where dp[i] represents the minimum number of coins needed to make the amount i.
2. Initialize dp[0] = 0, since 0 coins are needed to make amount 0.
3. For each amount i, iterate over each coin coin. If i - coin >= 0, update dp[i] = min(dp[i], dp[i - coin] + 1).
4. After filling the DP array, check dp[amount]. If it’s still set to infinity, return -1; otherwise, return dp[amount].

'''

# 代码
def coinChange(coins: list[int], amount: int) -> int:
    # Initialize dp array with a large number (indicating not possible to achieve that amount)
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # Base case: 0 coins needed to make amount 0

    # Fill dp array
    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0:  # If the current amount is achievable
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # Check if the amount is achievable; return the result accordingly
    return dp[amount] if dp[amount] != float('inf') else -1

'''
Time Complexity: O(amount * n), where n is the number of coin denominations, as we iterate over each coin for each amount.

Space Complexity: O(amount), since we need a DP array of size amount + 1 to store the minimum coins required for each amount. 
'''